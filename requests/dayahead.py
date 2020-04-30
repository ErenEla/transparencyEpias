import pandas as pd 
import requests
import json
from datetime import timedelta 
from datetime import datetime
import validate as val


def get_request_result(query):

    #main_url = "https://seffaflik.epias.com.tr/transparency/service/market/"

    url = "https://seffaflik.epias.com.tr/transparency/service/market/"+query

    payload = {}
    headers = {
    'Cookie': 'TS01f69930=01cbc7c0b229af3f9e170f80092f828abac28c9cacff2f44fbd6391713e0e3f0af97eecc2694f5fc77aefc033595cc62fe9c469b52'
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    json_data = json.loads(response.text.encode('utf8'))

    return json_data


def mcp_interim(date):

    '''
    This function returns 3 lists including;
        -Date list for specified date as first item.
        -Hour list as second item.
        -Interim MCP values for specified date as third item.

    Parameters:

    Date: Specific date in YYYY-MM-DD format.

    '''
    val.date_format_check(date)

    query = "day-ahead-interim-mcp?date="+f'{date}'

    json_result = get_request_result(query)

    key_list = list(json_result['body'].keys())

    key_name = key_list[0]

    response_list = json_result['body'][f'{key_name}']

    date_list = []
    price_list = []
    hour_list = []

    for index, item_count in enumerate(response_list):
        date_list.append(date)
        hour_list.append(index)
        price_list.append(item_count['marketTradePrice'])

    return date_list, hour_list, price_list


def mcp(startDate, endDate):

    '''
    This function returns 2 lists including;
        -Datetime list that covers the range of startDate and endDate parameters as first item.
        -MCP values for specified range of dates as second item.

    Parameters:

    startDate: Start date in YYYY-MM-DD format.
    endDate: End date in YYYY-MM-DD format.

    '''

    val.date_check(startDate, endDate)

    query = "day-ahead-mcp?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

    json_result = get_request_result(query)

    key_list = list(json_result['body'].keys())

    key_name = key_list[0]

    response_list = json_result['body'][f'{key_name}']

    datetime_list = []
    price_list = []

    for item_count in response_list:
        price_list.append(item_count['price'])
        datetime_list.append(item_count['date'])

    return datetime_list, price_list


def diff_fund(startDate, endDate, is_statistic):

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

    query = "day-ahead-diff-funds?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

    json_result = get_request_result(query)

    key_list = list(json_result['body'].keys())

    key_name = key_list[0]
    second_key_name = key_list[1]

    if is_statistic == 1 or is_statistic == 'TRUE' :
        response_list = json_result['body'][f'{second_key_name}']

    else:
        response_list = json_result['body'][f'{key_name}']

    return response_list


def block_amount(startDate, endDate, is_statistic):
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

    query = "amount-of-block?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

    json_result = get_request_result(query)

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


def block_amount_matched(startDate, endDate, is_statistic):
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

    query = "amount-of-block?startDate="+f'{startDate}'+"&endDate="+f'{endDate}'

    json_result = get_request_result(query)

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


def supply_demand_curve(date):

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

    query = "supply-demand-curve?period="+f'{date}'

    json_result = get_request_result(query)

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

print(mcp_interim('2020-04-01'))