from dayaheadClient import dayahead
import pandas as pd 
from pandas import ExcelWriter
import openpyxl
import xlsxwriter

'''
date_list = dayahead.mcp_interim('2020-04-01')[0]
interim_mcp = dayahead.mcp_interim('2020-04-01')[2]

interim_df = pd.DataFrame({'date':date_list, 'interim_MCP':interim_mcp})

writer = pd.ExcelWriter('Out.xlsx')
interim_df.to_excel(writer,'Interim MCP')
writer.save()
'''

print(dayahead.dayahead_market_volume(startDate='2020-04-01', endDate='2020-04-01'))