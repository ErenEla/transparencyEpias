import pandas as pd 
import requests
import json
from datetime import timedelta 
from datetime import datetime
from markets import validate as val

class consumptionClient:

    def get_request_result(self, query):

        #main_url = "https://seffaflik.epias.com.tr/transparency/service/market/"

        url = "https://seffaflik.epias.com.tr/transparency/service/"+query

        response = requests.request("GET", url)

        json_data = json.loads(response.text.encode('utf8'))

        return json_data
    
    def consumption_all(self, date):

        '''
        This function returns 4 lists including;
            -Date list for specified date as first item.
            -Total consumption amount as second item.
            -Eligible Customer consumption amount for specified date as third item.
            -Under Supply Liability consumption amount for specified date as third item.

        Parameters:

        Date: Specific date in YYYY-MM-DD format.

        '''
        val.date_format_check(date)

        query = "consumption/consumption?period="+f'{date}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        consumption_list = []
        consumption_elig_list = []
        consumption_underSupply_list = []

        for item in response_list:
            date_list.append(item['period'])
            consumption_list.append(item['consumption'])
            consumption_elig_list.append(item['eligibleCustomerConsumption'])
            consumption_underSupply_list.append(item['underSupplyLiabilityConsumption'])

        return date_list, consumption_list, consumption_elig_list, consumption_underSupply_list
    
    def distribution_network(self):

        '''
        This function returns a list including;
            -Distribution 

        Parameters:

        Date: Specific date in YYYY-MM-DD format.

        '''

        query = "consumption/distribution"

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        network_list = []

        for item in response_list:
            network_list.append(item['distributionList'])

        return network_list

    # response error -1 
    def distribution_profile(self, date, id=None, meterType=None, profile_group=None):

        '''
        This function returns a dictionary including;
            -Date.
            -Multiplier.

        Parameters:

        Date: Specific date in YYYY-MM-DD format.

        '''
        val.date_format_check(date)

        query = "consumption/distribution-profile?period="+f'{date}'+"&distributionId"+f'{id}'+"&subscriberProfileGroup"+f'{profile_group}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list
    
    def distribution_company(self):

        '''
        This function returns a list including;
            -Distribution companies' information. 

        Parameters:

        Date: Specific date in YYYY-MM-DD format.

        '''

        query = "consumption/get-distribution-company"

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        company_list = []

        for item in response_list:
            company_list.append(item['distributionCompanyList'])

        return company_list
    
    def outage_planned(self, date, companyId=None, provinceId=None):

        '''
        This function returns a list including;
            -Planned outage amount information. 

        Parameters:

        date: Specific date in YYYY-MM-DD format.
        companyId (Optional) = Specific company id.
        provinceId (Optional) = Specific province id.

        '''

        val.date_format_check(date)

        query = "consumption/get-planned-outage?"+"period="+f'{date}'+"distributionCompanyId="+f'{companyId}'+"provinceId="+f'{provinceId}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        outage_list = []

        for item in response_list:
            outage_list.append(item['powerOutageList'])

        return outage_list
    
    def outage_unplanned(self, date, companyId=None, provinceId=None):

        '''
        This function returns a list including;
            -Unplanned outage amount information. 

        Parameters:

        date: Specific date in YYYY-MM-DD format.
        companyId (Optional) = Specific company id.
        provinceId (Optional) = Specific province id.

        '''

        val.date_format_check(date)

        query = "consumption/get-unplanned-outage?"+"period="+f'{date}'+"distributionCompanyId="+f'{companyId}'+"provinceId="+f'{provinceId}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        outage_list = []

        for item in response_list:
            outage_list.append(item['powerOutageList'])

        return outage_list
    
    #response error 
    def consumption_forecast(self, startDate, endDate):

        '''
        This function returns a dictionary including;
            -date
            -lepAvg
            -lepMax
            -lepMin
            -lepSum

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        Warning: Estimation plan is not published by EPIAS.

        '''

        val.date_check(startDate, endDate)

        query = "consumption/load-estimation-plan?"+"startDate="+f'{startDate}'+"endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list

    def consumption_realtime(self, startDate, endDate):

        '''
        This function returns a dictionary including;
            -Datetime list that covers the range of startDate and endDate parameters as first item. 
            -Actual consumption amount as second item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "consumption/real-time-consumption?"+"startDate="+f'{startDate}'+"endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        consumption_list = []

        for item in response_list:
            date_list.append(item['date'])
            consumption_list.append(item['consumption'])

        return date_list, consumption_list
    
    def consumption_official(self, startDate, endDate):

        '''
        This function returns a dictionary including;
            -Datetime list that covers the range of startDate and endDate parameters as first item. 
            -Officially aproved consumption amount as second item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "consumption/swv?"+"startDate="+f'{startDate}'+"endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        consumption_list = []

        for item in response_list:
            date_list.append(item['date'])
            consumption_list.append(item['swv'])

        return date_list, consumption_list
    
    def consumption_supplyLia(self, startDate, endDate):

        '''
        This function returns a dictionary including;
            -Datetime list that covers the range of startDate and endDate parameters as first item. 
            -Under supply liablitiy consumption amount as second item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''

        val.date_check(startDate, endDate)

        query = "consumption/under-supply-liability-consumption?"+"startDate="+f'{startDate}'+"endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        swv_list = []

        for item in response_list:
            date_list.append(item['date'])
            swv_list.append(item['swv'])

        return date_list, consumption_list
    
    def consumption_eligible(self, date):

        '''
        This function returns a list including;
            -Date information as first item.
            -Eligible consumer consumption amount as second item.

        Parameters:

        date: Specific date in YYYY-MM-DD format.
        companyId (Optional) = Specific company id.
        provinceId (Optional) = Specific province id.

        '''

        val.date_format_check(date)

        query = "consumption/swv-v2?"+"period="+f'{date}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        svw2_list = []

        for item in response_list:
            date_list.append(item['vc_gec_trh'])
            svw2_list.append(item['st'])

        return date_list, svw2_list
    


consumption = consumptionClient()