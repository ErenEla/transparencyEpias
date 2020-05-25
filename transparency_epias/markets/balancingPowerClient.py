import pandas as pd 
import requests
import json
from datetime import timedelta 
from datetime import datetime
from transparency_epias.markets import validate as val

class balancingPowerClient:

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

    def smp(self, startDate, endDate):

        '''
        This function returns 3 lists including;
            -Date list for specified date as first item.
            -System Position information as second item.
            -Price values as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "market/smp?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        direction_list = []
        price_list = []

        for item in response_list:
            date_list.append(item['date'])
            direction_list.append(item['smpDirection'])
            price_list.append(item['price'])

        return date_list, direction_list, price_list
    
    def bpm_orders(self, startDate, endDate):

        '''
        This function returns a dictionary including;
            -Date information.
            -Net position amount.
            -Zero coded up regulation amount.
            -One coded up regulation amount.
            -Two coded up regulation amount.
            -Zero coded down regulation amount.
            -One coded down regulation amount.
            -Two coded down regulation amount.
            -System direction information.
            -Next hour infromation as datetime.


        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "market/bpm-order-summary?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[1]

        response_list = json_result['body'][f'{key_name}']

        return response_list

balancingPower = balancingPowerClient()