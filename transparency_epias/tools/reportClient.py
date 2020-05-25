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



