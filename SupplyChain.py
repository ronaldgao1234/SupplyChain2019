import os
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import requests
# pprint is used to format the JSON response
from pprint import pprint

subscription_key = "6d325fae5e154556a079af1cfc1a8422"
endpoint = "https://westcentralus.api.cognitive.microsoft.com/text/analytics"

credentials = CognitiveServicesCredentials(subscription_key)

entities_url = endpoint + "/v2.1/entities"

documents = {"documents": [
    {"id": "1",
     "language": "en",
     "text": "April 4, 1975, 4 September, 1992"}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(entities_url, headers=headers, json=documents)
entities = response.json()
pprint(entities)