from markets import dayaheadClient
from markets import validate
from gas import gasTraClients


print(gasTraClients.gasClient.balancing_gas_price(startDate='2020-04-05',endDate='2020-04-06'))

print(dayaheadClient.dayahead.mcp(startDate='2020-05-14',endDate='2020-05-14'))