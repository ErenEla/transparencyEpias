import pandas as pd 
import requests
import json
from datetime import timedelta 
from datetime import datetime
from markets import validate as val

class gasTransmissionClient:

    def get_request_result(self, query):

        #main_url = "https://seffaflik.epias.com.tr/transparency/service/market/"

        url = "https://seffaflik.epias.com.tr/transparency/service/"+query

        response = requests.request("GET", url)

        json_data = json.loads(response.text.encode('utf8'))

        return json_data
    
    def stock_amoutn(self, startDate, endDate):

        '''
        This function returns 2 lists including;
            -Gas day informatin as first item.
            -Pipe stock amount values as second item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp-transmission/actualization?"+"startDate="+f'{startDate}'+"endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        day_list = []
        pipe_stock = []

        for item in response_list:
            day_list.append(item['gasDay'])
            pipe_stock.append(item['pipeStock'])

        return day_list, pipe_stock
    
    def transport(self, startDate, endDate):

        '''
        This function returns 3 lists including;
            -Gas day informatin as first item.
            -Entry nomination amount values as second item.
            -Exit nomination amount values as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp-transmission/transport?"+"startDate="+f'{startDate}'+"endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        day_list = []
        entry_list = []
        exit_list = []

        for item in response_list:
            day_list.append(item['gasDay'])
            entry_list.append(item['entryNomination'])
            exit_list.append(item['exitNomination'])

        return day_list, entry_list, exit_list
    
gas_transmission = gasTransmissionClient()


class gasClient:

    def get_request_result(self, query):

        #main_url = "https://seffaflik.epias.com.tr/transparency/service/market/"

        url = "https://seffaflik.epias.com.tr/transparency/service/"+query

        response = requests.request("GET", url)

        json_data = json.loads(response.text.encode('utf8'))

        return json_data

    def notification_additional(self, startDate, endDate):

            '''
            This function returns 4 lists including;
                -Date informatin as first item.
                -Id information as second item.
                -Message information as third item.
                -Subject information as fourth item.

            Parameters:

            startDate: Start date in YYYY-MM-DD format.
            endDate: End date in YYYY-MM-DD format.

            '''

            val.date_check(startDate, endDate)

            query = "stp/additional-notification?"+"startDate="+f'{startDate}'+"endDate="+f'{endDate}'

            json_result = self.get_request_result(query)

            key_list = list(json_result['body'].keys())

            key_name = key_list[0]

            response_list = json_result['body'][f'{key_name}']

            date_list = []
            message_list = []
            subject_list = []
            id_list = []

            for item in response_list:
                date_list.append(item['date'])
                message_list.append(item['messageEn'])
                subject_list.append(item['subjectEn'])
                id_list.append(item['id'])

            return date_list, id_list, message_list, subject_list
        
    def allowance(self, startDate, endDate):

        '''
        This function returns a dictionary including;
            -GasDay
            -InputDataPyhsical
            -InputDataVirtual
            -NegativeImbalance
            -NegativeImbalanceTradeValue
            -Opsiyonel
            -OutputDataPyhsical
            -OutputDataVirtual
            -PositiveImbalance
            -PositiveImbalanceTradeValue
            -SystemDirection
            -Type


        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp/allowance?"+"startDate="+f'{startDate}'+"endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list

    def balancing_gas_price(self, startDate, endDate):

            '''
            This function returns a dictionary including;
                -additionalBalancingPurchase
                -additionalBalancingSale
                -balancingGasPurchase
                -balancingGasSale
                -finalAbp
                -finalAbs
                -finalBgp
                -finalBgs
                -gasDay


            Parameters:

            startDate: Start date in YYYY-MM-DD format.
            endDate: End date in YYYY-MM-DD format.

            '''

            val.date_check(startDate, endDate)

            query = "stp/balancing-gas-price?"+"startDate="+f'{startDate}'+"endDate="+f'{endDate}'

            json_result = self.get_request_result(query)

            key_list = list(json_result['body'].keys())

            key_name = key_list[0]

            response_list = json_result['body'][f'{key_name}']

            return response_list
    
    # null response
    def bluecode(self, startDate, endDate):

        '''
        This function returns 4 lists including;
            -Gas day informatin as first item.
            -Contract Name information as second item.
            -Amount values as third item.
            -Weighted average values as fourth item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp/bluecode-operation?"+"startDate="+f'{startDate}'+"endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        day_list = []
        contract_list = []
        amount_list = []
        wAvg_list = []

        for item in response_list:
            day_list.append(item['gasDay'])
            contract_list.append(item['contractName'])
            amount_list.append(item['amount'])
            wAvg_list.append(item['weightedAverage'])

        return day_list, contract_list, amount_list, wAvg_list
    
    def contract_amount(self, startDate, endDate, date=None):

        '''
        This function returns 5 lists including;
            -Gas day informatin as first item.
            -Matched quantitiy amount as second item.
            -Period information as third item.
            -Period Type information  as fourth item.
            -Trade volume amount as fifth item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.
        date (Optional): Specific date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)
        val.date_format_check(date)

        query = "stp/bluecode-operation?"+"startDate="+f'{startDate}'+"endDate="+f'{endDate}'+"period="+f'{date}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        day_list = []
        matched_list = []
        period_list = []
        periodType_list = []
        trade_list = []

        for item in response_list:
            day_list.append(item['gasDay'])
            matched_list.append(item['matchingQuantity'])
            period_list.append(item['period'])
            periodType_list.append(item['periodType'])
            trade_list.append(item['tradeValue'])

        return day_list, matched_list, period_list, periodType_list, trade_list
    
    def price_daily(self, startDate, endDate):

        '''
        This function returns 7 lists including;
            -Gas day informatin as first item.
            -Contract name information as second item.
            -Intraday price values as third item.
            -Day after price values as fourth item.
            -Dayahead price values as fifth item.
            -Weighted Average price values as sixth item.
            -Gas reference price values as seventh item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)
        val.date_format_check(date)

        query = "stp/daily-price?"+"startDate="+f'{startDate}'+"endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        day_list = []
        contact_list = []
        intraday_list = []
        dayAfter_list = []
        dayahead_list = []
        wavg_list = []
        gas_ref_price = []

        for item in response_list:
            day_list.append(item['gasDay'])
            contact_list.append(item['contractName'])
            intraday_list.append(item['intraDayPrice'])
            dayAfter_list.append(item['dayAfterPrice'])
            dayahead_list.append(item['dayAheadPrice'])
            wavg_list.append(item['weightedAverage'])
            gas_ref_price.append(item['gasReferencePrice'])

        return day_list, contact_list, intraday_list, dayAfter_list, dayahead_list, wavg_list, gas_ref_price

gas = gasClient()