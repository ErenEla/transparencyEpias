import pandas as pd 
import requests
import json
from datetime import timedelta 
from datetime import datetime
import validate as val

class DayaheadClient:

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

    def mcp_interim(self, date):

        '''
        This function returns 3 lists including;
            -Date list for specified date as first item.
            -Hour list as second item.
            -Interim MCP values for specified date as third item.

        Parameters:

        Date: Specific date in YYYY-MM-DD format.

        '''
        val.date_format_check(date)

        query = "market/day-ahead-interim-mcp?date="+f'{date}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        price_list = []
        hour_list = []

        for index, item in enumerate(response_list):
            date_list.append(date)
            hour_list.append(index)
            price_list.append(item['marketTradePrice'])

        return date_list, hour_list, price_list

    def mcp(self, startDate, endDate):

        '''
        This function returns 2 lists including;
            -Datetime list that covers the range of startDate and endDate parameters as first item.
            -MCP values for specified range of dates as second item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "market/day-ahead-mcp?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        datetime_list = []
        price_list = []

        for item_count in response_list:
            price_list.append(item_count['price'])
            datetime_list.append(item_count['date'])

        return datetime_list, price_list

    def diff_fund(self, startDate, endDate, is_statistic):

        '''
        This function returns two different lists according to is_statistic parameter, which includes;
            -Statistical results for the range of specified dates.
            -Date, originatingFromBids, originatingFromOffers, originatingFromRounding and
            total values for the range of specified dates.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.
        is_statistic: An integer or string value shoul be 1 or TRUE.

        '''

        val.date_check(startDate, endDate)

        query = "market/day-ahead-diff-funds?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]
        second_key_name = key_list[1]

        if is_statistic == 1 or is_statistic == 'TRUE' :
            response_list = json_result['body'][f'{second_key_name}']

        else:
            response_list = json_result['body'][f'{key_name}']

        return response_list

    def block_amount(self, startDate, endDate, is_statistic):
        '''
        This function returns 4 different lists according to is_statistic parameter, which includes;
            -Statistical results for the range of specified dates.
            -Datetime values for the range of specified dates as firts item.
            -Block Sell values for the range of specified dates as second item.
            -Block Buy values for the range of specified dates as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.
        is_statistic: An integer or string value shoul be 1 or TRUE.

        Warning! For the "MATCHED" block amounts look for block_amount_matched

        '''

        val.date_check(startDate, endDate)

        query = "market/amount-of-block?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]
        second_key_name = key_list[1]

        if is_statistic == 1 or is_statistic == 'TRUE' :
            response_list = json_result['body'][f'{second_key_name}']

            return response_list

        else:
            response_list = json_result['body'][f'{key_name}']

            date_list = []
            purch_amount_list = []
            sale_amount_list = []

            for item in response_list:
                date_list.append(item['date'])
                purch_amount_list.append(item['amountOfPurchasingTowardsBlock'])
                sale_amount_list.append(item['amountOfSalesTowardsBlock'])

            return date_list, sale_amount_list, purch_amount_list


    def block_amount_matched(self, startDate, endDate, is_statistic):
        '''
        This function returns 4 different lists according to is_statistic parameter, which includes;
            -Statistical results for the range of specified dates.
            -Datetime values for the range of specified dates as firts item.
            -Matched Block Sell values for the range of specified dates as second item.
            -Matched Block Buy values for the range of specified dates as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.
        is_statistic: An integer or string value shoul be 1 or TRUE.

        Warning! For the "NOT MATCHED" block amounts look for block_amount.

        '''

        val.date_check(startDate, endDate)

        query = "market/amount-of-block?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]
        second_key_name = key_list[1]

        if is_statistic == 1 or is_statistic == 'TRUE' :
            response_list = json_result['body'][f'{second_key_name}']

            return response_list

        else:
            response_list = json_result['body'][f'{key_name}']

            date_list = []
            macthed_purch_amount_list = []
            matched_sale_amount_list = []

            for item in response_list:
                date_list.append(item['date'])
                macthed_purch_amount_list.append(item['amountOfPurchasingTowardsMatchBlock'])
                matched_sale_amount_list.append(item['amountOfSalesTowardsBlock'])

            return date_list, matched_sale_amount_list, macthed_purch_amount_list


    def supply_demand_curve(self, date):

        '''
        This function returns 4 different which includes;
            -Datetime values for the range of specified dates as firts item.
            -Price values for the range of specified dates as second item.
            -Supply amount values for the range of specified dates as third item.
            -Demand amount values for the range of specified dates as third item.

        Parameters:

        date: Specific date in YYYY-MM-DD format.

        '''

        val.date_format_check(date)

        query = "market/supply-demand-curve?period="+f'{date}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        price_list = []
        supply_list = []
        demand_list = []

        for item in response_list:
            date_list.append(item['date'])
            price_list.append(item['price'])
            supply_list.append(item['supply'])
            demand_list.append(item['demand'])

        return date_list, price_list, supply_list, demand_list


    def bilateralContract(self, startDate, endDate):

        '''
        This function returns 3 different which includes;
            -Datetime values for the range of specified dates as firts item.
            -Quantity values for the range of specified dates as second item.
            -Next hour values for the range of specified dates as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "market/bilateral-contract?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        quantity_list = []
        next_hour_datelist = []

        for item in response_list:
            date_list.append(item['date'])
            quantity_list.append(item['quantity'])
            next_hour_datelist.append(item['nextHour'])

        return date_list, quantity_list, next_hour_datelist

    def bilateralContract_all(self, startDate, endDate, eic=None):

        '''
        This function returns 3 different which includes;
            -Datetime values for the range of specified dates as firts item.
            -Bid Quantity values for the range of specified dates as second item.
            -Ask Quantity values for the range of specified dates as third item.

        Parameters:

        eic (Optional): A code for the specific company e.g: "40X000000009447G".
        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        if eic != None:
            query = "market/bilateral-contract?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'+"&eic="+f'{eic}'
        else:
            query = "market/bilateral-contract?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        quantity_bid = []
        quantity_ask = []

        for item in response_list:
            date_list.append(item['date'])
            quantity_bid.append(item['quantityBid'])
            quantity_ask.append(item['quantityBidAsk'])

        return date_list, quantity_bid, quantity_ask


    def market_income_summary(self, period, startDate, endDate):

        '''
        This function returns 3 different which includes;
            -Datetime values for the range of specified dates as firts item.
            -Income values for the range of specified dates as second item.
            -Period information for the range of specified dates as third item.
            -Period type information for the range of specified dates as fourth item.

        Parameters:

        period: Period type shoul be defined as DAILY, WEEKLY, MONTHLY, or PERIODIC.
        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "market/day-ahead-market-income-summary?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'+"&period="+f'{period}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        income_list = []
        period_list = []
        period_type_list = []

        for item in response_list:
            date_list.append(item['date'])
            income_list.append(item['income'])
            period_list.append(item['period'])
            period_type_list.append(item['periodTpye'])

        return date_list, income_list, period_list, period_type_list


    def dayahead_trade_volume(self, startDate, endDate):

        '''
        This function returns 3 different which includes;
            -Datetime values for the range of specified dates as firts item.
            -Bid trade volume values for the range of specified dates as second item.
            -Ask trade volume values for the range of specified dates as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        Warning! Bid and ask trade volumes are MATCHED dayahead trade volumes. For ask and bid OFFERS look for dayahead_market_volume.

        '''

        val.date_check(startDate, endDate)

        query = "market/day-ahead-market-trade-volume?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        bid_volume_list = []
        ask_volume_list = []

        for item in response_list:
            date_list.append(item['date'])
            bid_volume_list.append(item['volumeOfBid'])
            ask_volume_list.append(item['volumeOfAsk'])

        return date_list, bid_volume_list, ask_volume_list
    
    def dayahead_market_volume(self, startDate, endDate, eic=None):

        '''
        This function returns 3 different which includes;
            -Returns a dictionary which includes following values;
                -date
                -quantityOfAsk
                -volume
                -quantityOfBid
                -priceIndependentBid
                -priceIndependentOffer
                -blockBid
                -blockOffer
                -matchedBids
                -matchedOffers

        Parameters:

        eic (Optional): A code for the specific company e.g: "40X000000009447G".
        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        Warning! Bid and ask trade volumes are MATCHED dayahead trade volumes. For ask and bid OFFERS look for dayahead_market_volume.

        '''

        val.date_check(startDate, endDate)

        if eic != None:

            query = "market/day-ahead-market-volume?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'+"&eic="+f'{eic}'
        else:
            query = "market/day-ahead-market-volume?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        response_list = json_result['body']['dayAheadMarketVolumeList']
        
        return response_list

    def imbalance_hourly(self, startDate, endDate):

        '''
        This function returns 3 different which includes;
            -Datetime values for the range of specified dates as firts item.
            -Hourly total positive imbalance values for the range of specified dates as second item.
            -Hourly total negative imbalance values for the range of specified dates as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "market/energy-imbalance-hourly?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        postive_imb_list = []
        negative_imb_list = []

        for item in response_list:
            date_list.append(item['date'])
            postive_imb_list.append(item['positiveImbalance'])
            negative_imb_list.append(item['negativeImbalance'])

        return date_list, postive_imb_list, negative_imb_list

    def imbalance_monthly(self, startDate, endDate):

        '''
        This function returns 3 different which includes;
            -Datetime values for the range of specified dates as firts item.
            -Montly total positive imbalance values for the range of specified dates as second item.
            -Montly total negative imbalance values for the range of specified dates as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "market/energy-imbalance-hourly?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        postive_imb_list = []
        negative_imb_list = []

        for item in response_list:
            date_list.append(item['date'])
            postive_imb_list.append(item['positiveImbalance'])
            negative_imb_list.append(item['negativeImbalance'])

        return date_list, postive_imb_list, negative_imb_list
    
    def imbalance_amount(self, startDate, endDate):

        '''
        This function returns 3 different which includes;
            -Date values for the range of specified dates as firts item.
            -Time values for the range of specified dates as firts item.
            -Total positive imbalance amount values for the range of specified dates as second item.
            -Total negative imbalance amount values for the range of specified dates as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "market/imbalance-amount?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        time_list = []
        postive_imb_list = []
        negative_imb_list = []

        for item in response_list:
            date_list.append(item['date'])
            time_list.append(item['time'])
            postive_imb_list.append(item['positiveImbalance'])
            negative_imb_list.append(item['negativeImbalance'])

        return date_list, time_list, postive_imb_list, negative_imb_list

dayahead = DayaheadClient()
