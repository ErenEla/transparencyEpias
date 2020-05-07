import pandas as pd 
import requests
import json
from datetime import timedelta 
from datetime import datetime
import validate as val

class IntradayClient:

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

    
    def weighted_average_price(self, startDate, endDate):

        '''
        This function returns 2 lists including;
            -Date list for specified date as first item.
            -Intraday weighted average price values as second item 

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "market/intra-day-aof?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        price_list = []

        for item in response_list:
            date_list.append(item['date'])
            price_list.append(item['price'])

        return date_list, price_list
    

    def income_intraday(self, startDate, endDate):

        '''
        This function returns 2 lists including;
            -Date list for specified range of date as first item.
            -Intraday income values for specified range of date as second item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "market/intra-day-aof?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        income_list = []

        for item in response_list:
            date_list.append(item['date'])
            income_list.append(item['income'])

        return date_list, income_list

    def block_offer_prices(self, startDate, endDate):

        '''
        This function returns a dictionary which includes the following information;
            -Date
            -Minimum ask price
            -Maximum ask pirce
            -Minimum bid price
            -Maximum bid pirce
            -Minimum matched price
            -Maximum matched price


        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        Warning! For hourly offer values look for hourly_offer_prices

        '''
        val.date_check(startDate, endDate)

        query = "market/intra-day-min-max-price?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'+"&offerType=BLOCK"

        json_result = self.get_request_result(query)

        response_list = json_result['body']

        return response_list

    def hourly_offer_prices(self, startDate, endDate):

        '''
        This function returns a dictionary which includes the following information;
            -Date
            -Minimum ask price
            -Maximum ask pirce
            -Minimum bid price
            -Maximum bid pirce
            -Minimum matched price
            -Maximum matched price


        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        Warning! For block offer values look for block_offer_prices
    
        '''
        val.date_check(startDate, endDate)

        query = "market/intra-day-min-max-price?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'+"&offerType=HOURLY"

        json_result = self.get_request_result(query)

        response_list = json_result['body']

        return response_list

    def hourly_quantities(self, startDate, endDate):

        '''
        This function returns 3 lists including;
            -Effective date information as first item.
            -Hourly sell quantities as second item. 
            -Hourly buy quantities as third item.


        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        Warning! For block offer values look for block_offer_prices
    
        '''
        val.date_check(startDate, endDate)

        query = "market/intra-day-min-max-price?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        response_list = json_result['body']

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        sell_quantity = []
        buy_quantity = []

        for item in response_list:
            date_list.append(item['effectiveDate'])
            sell_quantity.append(item['blockPurchaseQuantity'])
            buy_quantity.append(item['blockSaleQuantity'])

        return date_list, sell_quantity, buy_quantity

    
    def trade_history(self, startDate, endDate, contract_type):

        '''
        This function returns 5 lists according to contract_type argument which including:
            -Datetime information as first item.
            -Contract id infromation as second item. 
            -Contract name information as third item.
            -Quantity values as fourth item.
            -Price values as fifth item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.
        contract_type: Block or Hourly

        '''
        val.date_check(startDate, endDate)

        query = "market/intra-day-trade-history?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        response_list = json_result['body']

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']
        
        hourly_date_list = []
        houry_id_list = []
        hourly_quantity = []
        hourly_price = []
        houryl_contract_list = []

        block_date_list = []
        block_id_list = []
        block_quantity = []
        block_price = []
        block_contract_list = []

        block_key = 'PB'
        
        for item in response_list:
            contract_name = item['conract']
            
            if block_key in contract_name:
                block_quantity.append(item['quantity'])
                block_price.append(item['price'])
                block_id_list.append(item['id'])
                block_date_list.append(item['date'])
                block_contract_list.append(item['conract'])
            else:
                hourly_quantity.append(item['quantity'])
                hourly_price.append(item['price'])
                houry_id_list.append(item['id'])
                hourly_date_list.append(item['date'])
                houryl_contract_list.append(item['conract'])

        if contract_type == 'Block':
            return block_date_list, block_id_list, block_contract_list, block_quantity, block_price
        elif contract_type == 'Hourly':
            return hourly_date_list, houry_id_list, houryl_contract_list, hourly_quantity, hourly_price
        else:
            raise Exception('contract_type argument has to be Block or Hourly!')

intraday = IntradayClient()