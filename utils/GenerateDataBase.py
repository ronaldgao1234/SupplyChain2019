import pandas as pd

# Dates
from random import randrange
from datetime import timedelta
from datetime import datetime

# Names
import names

# Location/Countries
import pycountry
import random

# User Id
import string


def generateRandomDates(count=100):
    def random_date(start, end):
        """
        This function will return a random datetime between two datetime
        objects.
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60)
        random_second = randrange(int_delta)
        ret = start + timedelta(seconds=random_second)
        return ret.date()

    start = datetime.strptime('1/1/2008', '%m/%d/%Y')
    end = datetime.strptime('1/1/2009', '%m/%d/%Y')
    return [random_date(start, end) for _ in range(count)]


def generateRandomNames(count=100):
    return [names.get_full_name() for _ in range(count)]


def generateRandomOrganizations(count=100):
    companies = ['85C Bakery Cafe', 'ABN AMRO', 'Accenture', 'Acer Inc.', 'Activision Blizzard', 'AccorHotels',
                 'Acumen', 'Adidas', 'Aditi Technologies', 'Aditya Birla Group', 'Advanced Micro Devices', 'Aegon',
                 'Affiliated Computer Services', 'Ahold Delhaize', 'Air France-KLM', 'Airbus',
                 'Aitken Spence', 'AkzoNobel', 'Alcatel-Lucent',
                 'Alfa Laval', 'Alliance Global Group Inc.',
                 'Allianz', 'Alstom', 'Altice', 'Altria Group', 'Amazon', 'American International Group',
                 'American MNCS Inc', 'A New India Angel', 'All Nippon Airways',
                 'Andritz AG', 'Aon', 'Apollo Tyres', 'Apple', 'Arcor', 'Assicurazioni Generali', 'Asus', 'Atari',
                 'AT&T', 'Avast Software', 'Avianca', 'AXA', 'Axiata Group',
                 'Axis Bank Ltd', 'Bacardi', 'Banco Bilbao Vizcaya Argentaria', 'Banco Santander', 'Bank of Kaohsiung',
                 'Bank of Montreal', 'Barclays', 'Barilla Group',
                 'Barrick Gold Corporation', 'BASF', 'Baskin-Robbins', 'Bata', 'Bayer', 'Becton Dickinson', 'Beko',
                 'Bic', 'BIDV', 'Bharti Airtel', 'Bharti Enterprises', 'Billabong',
                 'Black & Decker', 'BMW', 'BNP Paribas', 'FJ CRUISER', 'Boeing', 'Bombardier Inc.', 'Bouygues', 'BRAC',
                 'Bridgestone', 'BT Group', 'British Airways', 'British Petroleum', 'Bihl', 'BYD', 'Cadbury Schweppes',
                 'Canon Inc', 'CapGemini', 'Capital One', 'Cargill', 'Caribbean Airlines', 'Caterpillar Inc.',
                 'Celestica', 'Chatime', 'Chevron', 'China Merchants Bank', 'CIMC', 'Cisco Systems', 'Citigroup',
                 'Coca-Cola', 'Cognizant Technology Solutions', 'Colgate-Palmolive Company', 'Comac', 'Concentrix',
                 'ConocoPhillips', 'Costco', 'Creative Labs', 'Crédit Agricole', 'Credit Suisse', 'Cummins', 'Cyient',
                 'Dabur', 'Daikin', 'Daimler AG', 'Danish Refugee Council', 'Dangote Group', 'Danone',
                 'Decathlon Group', 'Dell', 'Deloitte', 'Delta Air Lines', 'Deutsche Bank', 'Deutsche Telekom', 'Durex',
                 'Disney', 'Dow Chemical', "Dunkin' Donuts", 'DXC Technology', 'easyJet', 'Einzton', 'EDF',
                 'Electrolux', 'Electronic Arts', 'Electronic Data Systems', 'Embraer', 'Emerson Electric', 'Enel',
                 'Eni', 'Epson', 'Ericsson', 'EY', 'Etisalat', 'Eva Air', 'Evergreen Marine', 'ExxonMobil',
                 'Faber-Castell', 'Facebook', 'FedEx Express', 'Ferrero', 'Fiat', 'Ficosa', 'FIS (company)',
                 'Ford Motor Company', 'FPT Group', 'France Télécom', 'Fujitsu', 'Future Group', 'Gap Inc.', 'Garmin',
                 'Gazprom', 'General Electric', 'General Motors', 'Generali', 'Gerdau', 'Giant Bicycles', 'Gillette',
                 'Glaxo Smith Kline', 'Goodyear Tire and Rubber Company', 'Google', 'Haier', 'Halliburton',
                 'Hankook Tire', 'Hasee', 'HCL Technologies', 'Hearst Corporation', 'Heineken',
                 'Hewlett Packard Enterprise', 'Hilti', 'Hindustan Computers Limited', 'Hitachi', 'Honda', 'Honeywell',
                 'HP Inc', 'HSBC', 'HTC', 'Huawei', 'Hutchison Whampoa Limited', 'Hytera', 'Hyundai Motor Company',
                 'IBM', 'ICAP', 'ICICI Bank', 'IKEA', 'Illinois Tool Works', 'Indesit', 'Indofood', 'Indiraman',
                 'Infosys', "infiCare Software's", 'ING Group', 'Ingersoll Rand', 'Impex', 'Intel Corporation',
                 'Intesa Sanpaolo', 'Isuzu', 'Instagram', 'Japan Airlines', 'Jardine Matheson', 'JG Summit Holdings',
                 'Jimmy Choo', 'Johnson & Johnson', 'Jollibee', 'JPMorgan Chase & Co.', 'JXD', 'Kawasaki',
                 'Kenya Airways', 'KFC', 'Kia Motors', 'Kingston Technology', 'Knorr', 'Komatsu Limited', 'Konami',
                 'KPMG', 'Krispy Kreme', 'Lactalis', 'Lagardère', 'Larsen & Toubro', 'Lear', 'Lenovo', 'Leonardo',
                 'Leoni AG', 'Lexmark', 'LG', 'LG Electronics', 'Linde', 'LiuGong', 'Lockheed Martin', "L'Oréal",
                 'Lotte Group', 'Lotus Biz Grp', 'Lukoil', 'Lupin', 'Luxgen', 'Luxottica', 'LyondellBasell Industries',
                 'Mahindra Group', 'Maggi', 'Marriott', 'Martini & Rossi', 'Masterfoods', 'Mattel', 'Maxxis',
                 "McDonald's", 'MediaTek', 'Meizu', 'Mercedes-AMG', 'Mercedes-Benz', 'Michelin',
                 'Micro-Star International', 'Micromax Informatics', 'Microsoft', 'Microsoft Mobile',
                 'Millipore Corporation', 'Mindtree', 'Mitsubishi Electric', 'Mobil', 'Monsanto Company', 'Motorola',
                 'Mustek', 'Nagarro', 'Namco Bandai Games', 'Namco Bandai Holdings', 'Nestlé', 'NetApp Inc.',
                 'News Corporation', 'Nike, Inc.', 'Nikon', 'Nintendo', 'Nissan', 'Novartis', 'Nokia', 'Oknoplast',
                 'Ooredoo', 'Oracle Corporation', 'Panasonic Corporation', 'Parmalat', 'Partners In Health',
                 'Pepper Lunch', 'PepsiCo', 'Perficient', 'Petronas', 'Petrovietnam', 'Pfizer', 'Philips',
                 'Ping An Bank', 'Ping An Insurance', 'Pirelli', 'Pladis', 'Pornhub', 'Procter & Gamble', 'Proton',
                 'Prudential Financial', 'PSA Peugeot Citroën', 'PwC', 'QNB Group', 'Ranbaxy', 'Reckitt Benckiser',
                 'Red Bull', 'Regus', 'Renault', 'Repsol', 'Ricoh', 'Robert Bosch GmbH', 'Rockstar Energy',
                 'Rohde & Schwarz', 'Royal Bank of Canada', 'Royal Bank of Scotland', 'Royal Dutch Shell', 'RPG Group',
                 'Rusal', 'SABMiller plc', 'Samsung Electronics', 'San Miguel Corporation', 'SanDisk', 'Sandvik',
                 'Sanofi Aventis', 'SAP SE', 'Sapient Corporation', 'SAS', 'Sasken Communication Technologies Limited',
                 'Sasol', 'Schlumberger', 'Schneider Electric', 'Scotiabank', 'Sears', 'Seco Tools',
                 'Sega Sammy Holdings', 'Servcorp', 'SF Express', 'Shenzhen Airlines', 'Siemens', 'Singapore Airlines',
                 'Singtel', 'Sinopec', 'Snapchat', 'SM Investments Corporation', 'Société Générale', 'Sogou',
                 'Solaris Bus & Coach', 'Sony', 'Sony Computer Entertainment', 'Sony Music Entertainment',
                 'Sony Pictures Entertainment', 'Southwest Airlines', 'Square Enix', 'Standard Chartered',
                 'State Bank of India', 'Starbucks', 'Suzuki', 'Swinkels Family Brewers', 'Tagged', 'Taiwan Beer',
                 'Tata Motors', 'Tate & Lyle', 'TCS', 'TCL Corporation', 'Tech Mahindra', 'Technicolor', 'TekeGldMpire',
                 'Telefonica', 'Tencent', 'Tesco', 'Tetra Pak', 'Textron', 'Thomson Reuters',
                 'The Coffee Bean & Tea Leaf', 'THIG, llc', 'Tissot', 'TKK Fried Chicken', 'Toshiba', 'Total S.A.',
                 'Towers Watson', 'Toyota', 'Trend Micro', 'TRW Automotive', 'TSMC', 'Tyco', 'Ülker', 'Uber', 'UMC',
                 'Unicredit', 'Unilever', 'Unisys', 'United Airlines', 'Vanke', 'Vestel', 'Viettel Mobile', 'Vitol',
                 'Vimpelcom', 'Virgin Group', 'VNPT', 'Vizio', 'Vodafone', 'Voith', 'Wal-Mart', 'Whirlpool Corporation',
                 'Wikimedia Foundation', 'Wirecard', 'Wipro', 'Yahoo', 'Yakult', 'Yamaha Corporation',
                 'Yamaha Motor Company', 'Zensar Technologies', 'Zhujiang Beer', 'ZTE', 'Zyxel']
    return [companies[random.randint(1, len(companies) - 1)] for i in range(count)]


def generateRandomLocations(count=100):
    countries = list(pycountry.countries)
    result = list()
    while len(result) != count:
        try:
            i = random.randint(1, len(countries))
            result.append(countries[i].official_name)
        except:
            pass
    return result


def generateUserId(count=100):
    def makeId(): return ''.join(random.choice(string.digits) for _ in range(10))

    return [makeId() for _ in range(count)]


def generateSGNs(count=100):
    '''Assume we only have 20 accounts for now. This is reasonable since SGN Numbers don't change for companies too.
    These numbers were generated with the same function as user id to make the problem clear that it can mix with user id'''
    sgns = ['2024325165', '5604708139', '6615103222', '8835287208', '7622913289', '1814333750', '2286097042',
            '6584064527', '4817018328', '2493572310', '1488329390', '6408533139', '1282533127', '0907475130',
            '4694824237', '1981929724', '8231448388', '5950924397', '7826636506', '8003003043']
    return [random.choice(sgns) for _ in range(count)]


def generateDatabase(count=100) -> pd.DataFrame:
    '''Generates a pd.DataFrame as a mock database'''
    db = pd.DataFrame({
        'Date': generateRandomDates(count),
        'Name': generateRandomNames(count),
        'Organization': generateRandomOrganizations(count),
        'Location': generateRandomLocations(count),
        'Phone Number': generateUserId(count),
        'SGN': generateSGNs(count)
    })
    return db


generateDatabase(5)
