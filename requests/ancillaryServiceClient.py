import pandas as pd 
import requests
import json
from datetime import timedelta 
from datetime import datetime
import validate as val

class ancillaryServicesClient:

    def get_request_result(self, query):

        #main_url = "https://seffaflik.epias.com.tr/transparency/service/market/"

        url = "https://seffaflik.epias.com.tr/transparency/service/"+query

        payload = {}
        headers = {
        'Cookie': 'TS01f69930=01cbc7c0b229af3f9e170f80092f828abac28c9cacff2f44fbd6391713e0e3f0af97eecc2694f5fc77aefc033595cc62fe9c469b52'
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        json_data = json.loads(response.text.encode('utf8'))

        return json_data


def pfc_amount(self, startDate, endDate):

        '''
        This function returns 3 lists including;
            -Date list for specified date as first item.
            -Hour information as second item.
            -Primary Frequancy Reserve Amounts as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "market/pfc-amount?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        hour_list = []
        amount_list = []

        for item in response_list:
            date_list.append(item['effectiveDate'])
            hour_list.append(item['hour'])
            amount_list.append(item['totalAmount'])

        return date_list, hour_list, amount_list

    def pfc_price(self, startDate, endDate):

        '''
        This function returns 3 lists including;
            -Date list for specified date as first item.
            -Hour information as second item.
            -Primary Frequancy Price values as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "market/pfc-price?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        hour_list = []
        price_list = []

        for item in response_list:
            date_list.append(item['effectiveDate'])
            hour_list.append(item['hour'])
            price_list.append(item['price'])

        return date_list, hour_list, price_list

    def sfc_amount(self, startDate, endDate):

        '''
        This function returns 3 lists including;
            -Date list for specified date as first item.
            -Hour information as second item.
            -Secondary Frequancy Reserve amounts as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "market/sfc-amount?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        hour_list = []
        amount_list = []

        for item in response_list:
            date_list.append(item['effectiveDate'])
            hour_list.append(item['hour'])
            amount_list.append(item['totalAmount'])

        return date_list, hour_list, amount_list

    def sfc_price(self, startDate, endDate):

        '''
        This function returns 3 lists including;
            -Date list for specified date as first item.
            -Hour information as second item.
            -Secondary Frequancy Reserve amounts as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "market/sfc-price?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        hour_list = []
        price_list = []

        for item in response_list:
            date_list.append(item['effectiveDate'])
            hour_list.append(item['hour'])
            price_list.append(item['price'])

        return date_list, hour_list, price_list

ancillary = ancillaryServicesClient()