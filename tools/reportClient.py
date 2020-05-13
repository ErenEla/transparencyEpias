import pandas as pd 
import requests
import json
from datetime import timedelta 
from datetime import datetime
from markets import dayaheadClient
from markets import validate as val
from consumption import consumptionClient

class mcpClient:

    def daily_excel_export(self):
        
        current_date = datetime.today()

        current_date_formatted = datetime.strftime(current_date,'%Y-%m-%d')

        int_announce_hour = 13
        announce_hour = 14

        if current_date.hour >= int_announce_hour and current_date.hour < announce_hour:
            current_date = current_date + timedelta(days=1)
            current_date_formatted = datetime.strftime(current_date,'%Y-%m-%d')
            mcp_list = dayaheadClient.dayahead.mcp_interim(current_date_formatted)
            print('Official MCP values are not published yet, for approved values try again after 2:00 P.M')
            mcp_df = pd.DataFrame({'Date':mcp_list[0],
                                'MCP':mcp_list[2]
                                })
        elif current_date.hour >= 14:
            current_date = current_date + timedelta(days=1)
            current_date_formatted = datetime.strftime(current_date,'%Y-%m-%d')
            mcp_list = dayaheadClient.dayahead.mcp(current_date_formatted,current_date_formatted)
            mcp_df = pd.DataFrame({'Date':mcp_list[0],
                                'MCP':mcp_list[1]
                                })
        else:
            mcp_list = dayaheadClient.dayahead.mcp(current_date_formatted,current_date_formatted)
            mcp_df = pd.DataFrame({'Date':mcp_list[0],
                                    'MCP':mcp_list[1]
                                    })

        mcp_df.to_excel(f'daily_mcp_{current_date_formatted}.xlsx')
        print(f'Report Created Successfully! Referance Date {current_date_formatted}')

    def excel_export(self, startDate, endDate):

        mcp_list = dayaheadClient.dayahead.mcp(startDate, endDate)

        mcp_df = pd.DataFrame({'Date':mcp_list[0],
                                'MCP':mcp_list[1]
                                })
        mcp_df.to_excel(f'MCP_{startDate}_{endDate}.xlsx')

        print('Report Created Successfully!')
        
mcp = mcpClient()



