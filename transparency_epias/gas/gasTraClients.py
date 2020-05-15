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

            query = "stp/additional-notification?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

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

        query = "stp/allowance?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

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

            query = "stp/balancing-gas-price?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

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

        query = "stp/bluecode-operation?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

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
        
        if date != None:
            val.date_format_check(date)
        else:
            pass

        query = "stp/bluecode-operation?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'+"&period="+f'{date}'

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

        query = "stp/daily-price?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        day_list = []
        contract_list = []
        intraday_list = []
        dayAfter_list = []
        dayahead_list = []
        wavg_list = []
        gas_ref_price = []

        for item in response_list:
            day_list.append(item['gasDay'])
            contract_list.append(item['contractName'])
            intraday_list.append(item['intraDayPrice'])
            dayAfter_list.append(item['dayAfterPrice'])
            dayahead_list.append(item['dayAheadPrice'])
            wavg_list.append(item['weightedAverage'])
            gas_ref_price.append(item['gasReferencePrice'])

        return day_list, contract_list, intraday_list, dayAfter_list, dayahead_list, wavg_list, gas_ref_price
    
    def fourcode(self, startDate, endDate):

        '''
        This function returns 6 lists including;
            -Gas day informatin as first item.
            -Contract name information as second item.
            -Amount values (x1000 sm3) values as third item.
            -Weigthed average values as fourth item.
            

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp/fourcode-operation?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        day_list = []
        amount_list = []
        contract_list = []
        wavg_list = []

        for item in response_list:
            day_list.append(item['gasDay'])
            contract_list.append(item['contractName'])
            amount_list.append(item['amount'])
            wavg_list.append(item['weightedAverage'])

        return day_list, contract_list, amount_list, wavg_list
    
    def greencode(self, startDate, endDate):

        '''
        This function returns 6 lists including;
            -Gas day informatin as first item.
            -Contract name information as second item.
            -Amount values (x1000 sm3) values as third item.
            -Weigthed average values as fourth item.
            -Transaction date information as fifth item.
            -Contract name information as sixth item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp/greencode-operation?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        day_list = []
        amount_list = []
        contract_list = []
        wavg_list = []
        transactiondate_list = []
        c_day_list = []

        for item in response_list:
            day_list.append(item['gasDay'])
            contract_list.append(item['contractName'])
            amount_list.append(item['amount'])
            wavg_list.append(item['weightedAverage'])
            transactiondate_list.append(item['transactionDate'])
            c_day_list.append(item['contractGasDay'])

        return day_list, contract_list, amount_list, wavg_list, transactiondate_list, c_day_list
    
    def price_reference(self, startDate, endDate, date=None):

        '''
        This function returns 4 lists including;
            -Gas day informatin as first item.
            -Period information as second item.
            -Period type as third item.
            -Reference price values as fourth item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.
        date (Optional): Specific date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        if date != None:
            val.date_format_check(date)
        else:
            pass

        query = "stp/grf?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'+"&period="+f'{date}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        day_list = []
        period_list = []
        price_list = []
        p_type = []
        

        for item in response_list:
            day_list.append(item['gasDay'])
            period_list.append(item['period'])
            price_list.append(item['price'])
            p_type.append(item['periodType'])

        return day_list, period_list, p_type, price_list
    
    def imbalance_montly(self, startDate, endDate):

        '''
        This function returns a dictionary including;
            -negativeImbalance
            -negativeImbalanceTradeValue
            -period
            -positiveImbalance
            -positiveImbalanceTradeValue
            -type

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp/imbalance-monthly?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list
    
    def quantitiy_matched(self, startDate, endDate):

        '''
        This function returns a dictionary including;
            -contractMatchingQuantity
            -contractName
            -dayAfterMatchingQuantity
            -dayAheadMatchingQuantity
            -gasDay
            -gasReferenceMatchingQuantity
            -intraDayMatchingQuantity

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp/matching-quantity?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list

    def quantitiy_matched_additional(self, startDate, endDate):

        '''
        This function returns 3 lists including;
            -Quantity amount as first item.
            -Gas day information as second item.
            -Other quantity amount as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp/matching-quantity/additional-quantity?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        quant_list = []
        day_list = []
        otherQuant_list = []

        for item in response_list:
            quant_list.append(item['additionalQuantity'])
            day_list.append(item['gasDay'])
            otherQuant_list.append(item['otherQuantity'])

        return quant_list, day_list, otherQuant_list
    
    def price_mobile(self, startDate, endDate):

        '''
        This function returns 5 lists including;
            -Balancing gas purchase amount as first item.
            -Balancing gas sale amount as second item.
            -Gas reference price values as third item.
            -Gas day information as fourth item.
            -Imbalance amount as sixth item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp/mobile/price?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        b_purch_list = []
        b_sale_list = []
        gas_refp_list = []
        day_list = []
        imb_list = []

        for item in response_list:
            b_purch_list.append(item['balancingGasPurchase'])
            day_list.append(item['gasDay'])
            b_sale_list.append(item['balancingGasPurchase'])
            gas_refp_list.append(item['otherQuantity'])
            imb_list.append(item['imbalance'])

        return b_purch_list, b_sale_list, gas_refp_list, day_list, imb_list
    
    def orangecode(self, startDate, endDate):

        '''
        This function returns a dictionary including;
            -amount
            -contractGasDay
            -contractName
            -gasDay
            -transactionDate
            -weightedAverage

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp/orangecode-operation?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list
    
    # Price type validation needed!
    def price_stp(self, startDate, endDate, price_type=None):

        '''
        This function returns 4 lists including;
            -Gas day information as first item.
            -Price values as second item.
            -Price type information as third item.
            -State information as fourht item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp/price?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'+"&priceType="+f'{price_type}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        g_day_list = []
        price_list = []
        priceType_list = []
        state_list = []

        for item in response_list:
            g_day_list.append(item['gasDay'])
            price_list.append(item['price'])
            priceType_list.append(item['priceType'])
            state_list.append(item['state'])

        return g_day_list, price_list, priceType_list, state_list
    
    def trade_value(self, startDate, endDate):

        '''
        This function returns a dictionary including;
            -contractName
            -contractTradeValue
            -dayAfterTradeValue
            -dayAheadTradeValue
            -gasDay
            -gasReferenceTradeValue
            -intraDayTradeValue

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp/trade-value?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list
    
    def transaction_history(self, startDate, endDate):

        '''
        This function returns a dictionary including;
            -contractName
            -id
            -mathcingDate
            -price
            -quantity

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp/transaction-history?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list
    
    def zero_balance(self, startDate, endDate):

        '''
        This function returns 2 lists including;
            -Gas day date information as first item.
            -Zero balance amount as second item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "stp/zero-balance?"+"startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        zero_b_list = []
        g_day_list = []

        for item in response_list:
            zero_b_list.append(item['zeroBalance'])
            g_day_list.append(item['gasDay'])

        return g_day_list, zero_b_list

gas = gasClient()