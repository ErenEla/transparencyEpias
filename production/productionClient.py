import pandas as pd 
import requests
import json
from datetime import timedelta 
from datetime import datetime
from markets import validate as val

class productionClient:

    def get_request_result(self, query):

        #main_url = "https://seffaflik.epias.com.tr/transparency/service/market/"

        url = "https://seffaflik.epias.com.tr/transparency/service/"+query

        response = requests.request("GET", url)

        json_data = json.loads(response.text.encode('utf8'))

        return json_data
    
    def availability(self, startDate, endDate, orgEic=None, uevcbEic=None):

        '''
        This function returns a dictionary including following information;
            -Date (tarih)
            -Total (toplam)
            -Natural Gas (dogalgaz)
            -Wind (ruzgar)
            -Brown Coal (linyit)
            -Bituminous Coal (tasKomur)
            -Import Coal (ithalKomur)
            -Fuel (fuelOil)
            -Geothermal (jeotermal)
            -Dam (barajli)
            -Naphtha-based (nafta)
            -Biomass (biokutle)
            -River (akarsu)
            -Other (diger)

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.
        orgEic (Optional): Organization EIC Code information e.g: 40X000000003585Y.
        uevcbEic (Optional): Organization EIC Code information e.g: 40W000000026808R.

        Note: For certain power plant availability information, both orgEic and uevcbEic parameters should pass as an argument.

        '''
        val.date_check(startDate, endDate)

        if orgEic == None and uevcbEic != None:
            raise Exception('Please provide organization eic cide with uevbEic code to get plant availability informaton' )
        else:
            pass

        val.uevcb_eic_check(uevcbEic)
        val.org_eic_check(orgEic)

        query = "production/aic?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'+"&organizationEIC="+f'{orgEic}'+"&uevcbEIC="+f'{uevcbEic}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list

    def daily_production_plan(self, startDate, endDate, orgEic=None, uevcbEic=None):

        '''
        This function returns a dictionary including following information;
            -Date (tarih)
            -Hour (saat)
            -Total (toplam)
            -Natural Gas (dogalgaz)
            -Wind (ruzgar)
            -Brown Coal (linyit)
            -Bituminous Coal (tasKomur)
            -Import Coal (ithalKomur)
            -Fuel (fuelOil)
            -Geothermal (jeotermal)
            -Dam (barajli)
            -Naphtha-based (nafta)
            -Biomass (biokutle)
            -River (akarsu)
            -Other (diger)

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.
        orgEic (Optional): Organization EIC Code information e.g: 40X000000003585Y.
        uevcbEic (Optional): Organization EIC Code information e.g: 40W000000026808R.

        Note: For certain power plant availability information, both orgEic and uevcbEic parameters should pass as an argument.

        '''
        val.date_check(startDate, endDate)

        if orgEic == None and uevcbEic != None:
            raise Exception('Please provide organization eic cide with uevbEic code to get plant availability informaton' )
        else:
            pass

        val.uevcb_eic_check(uevcbEic)
        val.org_eic_check(orgEic)

        query = "production/dpp?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'+"&organizationEIC="+f'{orgEic}'+"&uevcbEIC="+f'{uevcbEic}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list
    
    def daily_production_plan_total(self, startDate, endDate):

        '''
        This function returns a dictionary including following information;
            -Date infromation.
            -Total Daily production plan for specified datetime.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "production/final-dpp?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list
    
    def back_charge(self, startDate, endDate):

        '''
        This function returns a dictionary including following information;
            -Back charge credit amount (gddk Credit Amount)
            -Back charge debt amount (gddkDebtAmount)
            -Net back charge amount (gddkNetAmount)

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "production/gddk-amount?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list
    
    def installed_cap(self, date):

        '''
        This function returns a dictionary including following information;
            -Period information.
            -Capacity type information.
            -Capacity amount.

        Parameters:

        date: Date in YYYY-MM-DD format.

        Note: For plants in feed-in tarriffs look for install_cap_fit
        '''
        val.date_format_check(date)

        query = "production/installed-capacity?period="+f'{date}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}'][1]

        return response_list
    
    def installed_cap_fit(self, date):

        '''
        This function returns a dictionary including following information;
            -Period information.
            -Capacity type information.
            -Capacity amount.

        Parameters:

        date: Date in YYYY-MM-DD format.

        Note: For all plants look for install_cap.
        '''
        val.date_format_check(date)

        query = "production/installed-capacity?period="+f'{date}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}'][0]

        return response_list

    def installed_cap_renewables(self, date):

        '''
        This function returns a dictionary including following information;
            -Capacity type id information.
            -Period information.
            -Capacity type information.
            -Capacity amount.

        Parameters:

        date: Date in YYYY-MM-DD format.

        '''
        val.date_format_check(date)

        query = "production/installed-capacity-of-renewable?period="+f'{date}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list
    
    def real_time_gen(self, startDate, endDate):

        '''
        This function returns a dictionary including following information;
            -Biomass
            -BlackCoal
            -DammedHydro
            -Date
            -Fueloil
            -GasOil
            -Geothermal
            -ImportCoal
            -ImportExport
            -Lignite
            -Lng
            -Naphta
            -NaturalGas
            -Nuclear (Nucklear **There is a typo on the response)
            -River
            -Sun
            -Total
            -Wind

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "production/real-time-generation?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list
    
    def real_time_gen_renewabales(self, startDate, endDate):

        '''
        This function returns a dictionary including following information;
            -Biogas
            -Biomass
            -CanalType
            -Date
            -Geothermal
            -Lfg
            -Others
            -Reservoir
            -RiverType
            -Sun
            -Total
            -Wind

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "production/renewable-sm-licensed-real-time-generation?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list
    
    def unit_cost_fit(self, startDate, endDate):

        '''
        This function returns 3 lists including;
            -Unit Cost values as first item.
            -Version date information as second item.
            -Period date information as third item.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "production/renewable-sm-unit-cost?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        unit_cost_list = []
        version_list = []
        period_list = []

        for x in range(len(response_list)):
            unit_cost_list.append(response_list[x]['unitCost'])
            version_list.append(response_list[x]['id']['donem'])
            period_list.append(response_list[x]['id']['versiyon'])
        
        return unit_cost_list, version_list, period_list
    
    def generation_official_unlicenced_fit(self, startDate, endDate):

        '''
        This function returns a dictionary including following information;
            -Date
            -Total
            -Wind
            -Biogas
            -CanalType
            -Biomass
            -Sun
            -Others

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "production/renewable-unlicenced-generation-amount?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list
    
    def fit_cost_total(self, startDate, endDate):

        '''
        This function returns a dictionary including following information;
            -LicenseExemptCost
            -Period
            -PortfolioIncome
            -ReneablesCost (RenewableCost **There is a typo in the response)
            -RenewablesTotalCost
            -UnitCost

            
        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "production/renewables-support?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list

    # response error code -1
    def daily_production_plan_updated(self, startDate, endDate, orgEic=None, uevcbEic=None):

        '''
        This function returns a dictionary including following information;
            -Date (tarih)
            -Hour (saat)
            -Total (toplam)
            -Natural Gas (dogalgaz)
            -Wind (ruzgar)
            -Brown Coal (linyit)
            -Bituminous Coal (tasKomur)
            -Import Coal (ithalKomur)
            -Fuel (fuelOil)
            -Geothermal (jeotermal)
            -Dam (barajli)
            -Naphtha-based (nafta)
            -Biomass (biokutle)
            -River (akarsu)
            -Other (diger)

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.
        orgEic (Optional): Organization EIC Code information e.g: 40X000000003585Y.
        uevcbEic (Optional): Organization EIC Code information e.g: 40W000000026808R.

        Note: For certain power plant availability information, both orgEic and uevcbEic parameters should pass as an argument.

        '''
        val.date_check(startDate, endDate)

        if orgEic == None and uevcbEic != None:
            raise Exception('Please provide organization eic cide with uevbEic code to get plant availability informaton' )
        else:
            pass

        val.uevcb_eic_check(uevcbEic)
        val.org_eic_check(orgEic)

        query = "production/sbfgp?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'+"&organizationEIC="+f'{orgEic}'+"&uevcbEIC="+f'{uevcbEic}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list
    
    #null response
    def plant_notifications(self, startDate, endDate):

        '''
        This function returns a dictionary including following information;
            -CapacityAtCaseTime
            -CaseAddDate
            -CaseEndDate
            -CaseStartDate
            -CaseVaguenessTime
            -City
            -CityId
            -FaultDetails
            -FuelType
            -FuelTypeId
            -Id
            -MessageType
            -OperatorPower
            -PowerPlantName
            -Reason
            -Region
            -UevcbName
            -validityStatus

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        '''
        val.date_check(startDate, endDate)

        query = "production/urgent-market-message?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        return response_list
    
    def production_total_official(self, startDate, endDate):

        '''
        This function returns two lists including;
            -Datetime information.
            -Officially aproved total production amount.

        Parameters:

        startDate: Start date in YYYY-MM-DD format.
        endDate: End date in YYYY-MM-DD format.

        Note:
        '''
        val.date_check(startDate, endDate)

        query = "production/ssv?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

        json_result = self.get_request_result(query)

        key_list = list(json_result['body'].keys())

        key_name = key_list[0]

        response_list = json_result['body'][f'{key_name}']

        date_list = []
        prod_list = []

        for item in response_list:
            date_list.append(item['date'])
            prod_list.append(item['ssv'])

        return date_list, prod_list

production = productionClient()