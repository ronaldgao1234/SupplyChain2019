from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import requests
# pprint is used to format the JSON response
from pprint import pprint
import pandas as pd
import dateutil.parser
from nameparser import HumanName

# input files
import os
import glob

# DataBase
from utils.GenerateDataBase import generateDatabase

# Number
import difflib
import numpy as np

################## Text Analytics API #########################
subscription_key = "6d325fae5e154556a079af1cfc1a8422"
endpoint = "https://westcentralus.api.cognitive.microsoft.com/text/analytics"
credentials = CognitiveServicesCredentials(subscription_key)
entities_url = endpoint + "/v2.1/entities"
###############################################################

################## File Names #################################
input_path = 'G:/My Drive/Hackathon/SupplyChain2019/input'
original_database = 'G:/My Drive/Hackathon/SupplyChain2019/orig_db.csv'  # Output of original randomly generated database
new_database = 'G:/My Drive/Hackathon/SupplyChain2019/new_db.csv'
###############################################################

def _parseColumn(col):
    '''Parses the matches for each item in that column'''
    d = dict()
    for match in col:
        type = match['type']
        if type in d:
            d[type] += 1
        else: d[type] = 1

    # calculate probabilities
    total_count = sum(d.values())
    l=list()
    for type, count in d.items():
        l.append(f'{type}: {count/total_count}')

    # either 1 value or multiple values but they are all different
    probs = d.values()
    if len(probs) == 1 or (len(set(probs)) == len(probs)) :
        most_likely = max(d, key=d.get)
        print(f"Column most likely type: {most_likely}  Probabilities: {str(l)}")
    else:
        print(f"Not sure Column type. Max probabilities are equal")
        return 'split on number'
    return most_likely

def EntityRecognition(file_name: str):
    '''Reads input file and performs TextAnalytics on it'''
    if file_name == 'data.csv':
        header_exists = True
        data = pd.read_csv(file_name)  # important there is no header
    else:
        header_exists = False
        data = pd.read_csv(file_name, header=None)  # important there is no header

    # Create Post Request
    document = []
    for col in data:
        document.append(
            {"id": f'{col}',
             "language": "en",
             "text": str(data[col].tolist())})
    inputs = {"documents": document}

    # Send POST Request
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(entities_url, headers=headers, json=inputs)
    entities = response.json()
    # pprint(entities)
    return entities, data, header_exists

def phone_format(n):
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]

def value_method(data_col, db):
    '''checks which col of db has value'''
    value = data_col[0]
    for c in db.columns:
        if str(value) in db[c].to_list():
            return pd.Series(data_col, name=c)
    return pd.Series([phone_format(str(x)) for x in data_col], name='Phone Number')

def analyzeFile(file_name : str, db):
    '''Send Post Request of file, return a dataframe that you can append to database
    '''
    entities, data, header_exists = EntityRecognition(file_name)
    df = pd.DataFrame()
    for i, column in enumerate(entities['documents']):
        type = _parseColumn(column['entities'])
        data_col = data.iloc[:,i].to_list()
        if type == 'DateTime':
            new_column = pd.Series([dateutil.parser.parse(x).date() for x in data_col], name='Date')
        elif type == 'Person':
            new_column = pd.Series([str(HumanName(x)) for x in data_col], name='Name')
        elif type == 'Organization':
            new_column = pd.Series(data_col, name='Organization')
        elif type == 'Location':
            new_column = pd.Series(data_col, name='Location')
        elif type == 'split on number':
            if header_exists:  # first check field names
                closeness = [difflib.SequenceMatcher(None, data.columns[i], c).ratio() * 100 for c in db.columns]
                max_index = np.argmax(closeness)
                if db.columns[max_index] == 'Phone Number':
                    new_column = pd.Series([phone_format(str(x)) for x in data_col], name='Phone Number')
                else:
                    new_column = pd.Series(data_col, name=db.columns[max_index])
            else:
                new_column = value_method(data_col, db)
        else:
            print('Type error')
            pass
        df = pd.concat([df, new_column], axis=1)
    print(df)
    return df

def main(input_files, db):
    # Get csv files from a folder
    extension = 'csv'
    os.chdir(input_path)
    input_files = glob.glob('*.{}'.format(extension))
    # db = generateDatabase(10)  # arg is just length
    db.to_csv(original_database)   # overwrites csv

    for file_name in input_files:
        df = analyzeFile(file_name, db)
        db = pd.concat([db,df], sort=False)

    print(db)
    db.reset_index(inplace=True, drop=True)
    db = db.loc[:, ~db.columns.str.contains('^Unnamed')]
    db.to_csv(new_database)   # overwrites csv
    return db