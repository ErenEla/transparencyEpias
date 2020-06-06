import pandas as pd 
import requests
import json
from datetime import timedelta 
from datetime import datetime
from transparency_epias.markets import dayaheadClient as dc
from transparency_epias.markets import validate as val
from transparency_epias.markets import balancingPowerClient as bpc
from transparency_epias.markets import intradayClient as ic
from transparency_epias.consumption import consumptionClient
import xlsxwriter 
from transparency_epias.markets import validate as val

class reportsClient:

    def daily_excel_export(self):
        
        current_date = datetime.today()

        current_date_formatted = datetime.strftime(current_date,'%Y-%m-%d')

        int_announce_hour = 13
        announce_hour = 14

        if current_date.hour >= int_announce_hour and current_date.hour < announce_hour:
            current_date = current_date + timedelta(days=1)
            current_date_formatted = datetime.strftime(current_date,'%Y-%m-%d')
            mcp_list = dc.dayahead.mcp_interim(current_date_formatted)
            print('Official MCP values are not published yet, for approved values try again after 2:00 P.M')
            mcp_df = pd.DataFrame({'Date':mcp_list[0],
                                'MCP':mcp_list[2]
                                })
        elif current_date.hour >= 14:
            current_date = current_date + timedelta(days=1)
            current_date_formatted = datetime.strftime(current_date,'%Y-%m-%d')
            mcp_list = dc.dayahead.mcp(current_date_formatted,current_date_formatted)
            mcp_df = pd.DataFrame({'Date':mcp_list[0],
                                'MCP':mcp_list[1]
                                })
        else:
            mcp_list = dc.dayahead.mcp(current_date_formatted,current_date_formatted)
            mcp_df = pd.DataFrame({'Date':mcp_list[0],
                                    'MCP':mcp_list[1]
                                    })

        mcp_df.to_excel(f'daily_mcp_{current_date_formatted}.xlsx')
        print(f'Report Created Successfully! Referance Date {current_date_formatted}')

    def mcp_excel_export(self, startDate, endDate):

        mcp_list = dc.dayahead.mcp(startDate, endDate)

        mcp_df = pd.DataFrame({'Date':mcp_list[0],
                                'MCP':mcp_list[1]
                                })
        mcp_df.to_excel(f'MCP_{startDate}_{endDate}.xlsx')

        print('Report Created Successfully!')

    def compare_price(self):

        current_date = datetime.today()

        yest_date = current_date - timedelta(days=1)

        yest_date_formatted = datetime.strftime(yest_date,'%Y-%m-%d')

        mcp = dc.dayahead.mcp(yest_date_formatted, yest_date_formatted)[1]
        smp = bpc.balancingPower.smp(yest_date_formatted, yest_date_formatted)[2]
        wap = ic.intraday.weighted_average_price(yest_date_formatted, yest_date_formatted)[1]
        date = dc.dayahead.mcp(yest_date_formatted, yest_date_formatted)[0]

        df = pd.DataFrame({'Date':date,
                                'MCP':mcp,
                                'SMP':smp,
                                'WAP':wap,
                                })
        
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        excel_file = 'PriceComparison.xlsx'
        sheet_name = 'Sheet1'

        writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=sheet_name)

        # Access the XlsxWriter workbook and worksheet objects from the dataframe.
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]

        # Create a chart object.
        chart = workbook.add_chart({'type': 'line'})

        # Configure the series of the chart from the dataframe data.

        name_list = ['mcp', 'smp','wap']
        line_list = ['solid','dash_dot','round_dot']

        for i in range(len(name_list)):
            
            col = i+2

            chart.add_series({
                'name': ['Sheet1',0,col],
                'categories': ['Sheet1', 1, 0, 24, 0],
                'values':     ['Sheet1', 1, col, 24, col],
                'line':   {'dash_type': f'{line_list[i]}'}
            })

        # Configure the chart axes.
        chart.set_x_axis({'name': 'Index', 'position_axis': 'on_tick'})
        chart.set_y_axis({'name': 'Value', 'major_gridlines': {'visible': False}})

        # Turn off chart legend. It is on by default in Excel.
        chart.set_legend({'position': 'bottom'})

        # Insert the chart into the worksheet.
        worksheet.insert_chart('G2', chart, {'x_scale': 3, 'y_scale': 1.5})

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

        print('Price Comparison excel is created!')


reports = reportsClient()


class calendarClient:

    def get_holidays(self, startDate, endDate):

        print('Warning! Holidays date range is between 2016 and 2020. Date range will be updated in future')

        holidaysTR = {'Date':["2016-01-01","2016-04-23","2016-05-01","2016-05-19","2016-07-04","2016-07-05","2016-07-06","2016-07-07","2016-08-30","2016-09-11","2016-09-12","2016-09-13","2016-09-14","2016-09-15","2016-10-28","2016-10-29","2017-01-01","2017-04-23","2017-05-01","2017-05-19","2017-06-24","2017-06-25","2017-06-26","2017-06-27","2017-07-15","2017-08-30","2017-08-31","2017-09-01","2017-09-02","2017-09-03","2017-09-04","2017-10-28","2017-10-29","2018-01-01","2018-04-23","2018-05-01","2018-05-19","2018-06-14","2018-06-15","2018-06-16","2018-06-17","2018-07-15","2018-08-20","2018-08-21","2018-08-22","2018-08-23","2018-08-24","2018-08-30","2018-10-28","2018-10-29","2019-01-01","2019-04-23","2019-05-01","2019-05-19","2019-06-03","2019-06-04","2019-06-05","2019-06-06","2019-07-15","2019-08-10","2019-08-11","2019-08-12","2019-08-13","2019-08-14","2019-08-30","2019-10-28","2019-10-29","2020-01-01","2020-04-23","2020-05-01","2020-05-19","2020-05-23","2020-05-24","2020-05-25","2020-05-26","2020-07-15","2020-07-30","2020-07-31","2020-08-01","2020-08-02","2020-08-03","2020-08-30","2020-10-28","2020-10-29"],
              'Days':[1,23,1,19,4,5,6,7,30,11,12,13,14,15,28,29,1,23,1,19,24,25,26,27,15,30,31,1,2,3,4,28,29,1,23,1,19,14,15,16,17,15,20,21,22,23,24,30,28,29,1,23,1,19,3,4,5,6,15,10,11,12,13,14,30,28,29,1,23,1,19,23,24,25,26,15,30,31,1,2,3,30,28,29],
              'Holidays':["Bank Holiday","Bank Holiday","Bank Holiday","Bank Holiday","Eve","Religious Holiday","Religious Holiday","Religious Holiday","Bank Holiday","Eve","Religious Holiday","Religious Holiday","Religious Holiday","Religious Holiday","Eve","Bank Holiday","Bank Holiday","Bank Holiday","Bank Holiday","Bank Holiday","Eve","Religious Holiday","Religious Holiday","Religious Holiday","Bank Holiday","Bank Holiday","Eve","Religious Holiday","Religious Holiday","Religious Holiday","Religious Holiday","Eve","Bank Holiday","Bank Holiday","Bank Holiday","Bank Holiday","Bank Holiday","Eve","Religious Holiday","Religious Holiday","Religious Holiday","Bank Holiday","Eve","Religious Holiday","Religious Holiday","Religious Holiday","Religious Holiday","Bank Holiday","Eve","Eve","Bank Holiday","Bank Holiday","Bank Holiday","Bank Holiday","Eve","Religious Holiday","Religious Holiday","Religious Holiday","Bank Holiday","Eve","Religious Holiday","Religious Holiday","Religious Holiday","Religious Holiday","Bank Holiday","Eve","Bank Holiday","Bank Holiday","Bank Holiday","Bank Holiday","Bank Holiday","Eve","Religious Holiday","Religious Holiday","Religious Holiday","Bank Holiday","Eve","Religious Holiday","Religious Holiday","Religious Holiday","Religious Holiday","Bank Holiday","Eve","Bank Holiday"] }

        val.date_check(startDate,endDate)

        # date list range check for parameters should be added
        date_list = []
        holiday_list = []
        for d_index, dates in enumerate(holidaysTR['Date']):
            if startDate <= dates <= endDate:
                date_list.append(dates)
                holiday_list.append(holidaysTR['Holidays'][d_index])

        return date_list, holiday_list

calendar = calendarClient()


