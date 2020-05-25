# transparencyEpias

[![PyPI Latest Release](https://img.shields.io/pypi/v/transparencyEpias.svg)](https://pypi.org/project/transparencyEpias/)

transparencyEpias is a package which consumes Epias Transparency Rest Web Services, mainly scopes to provide easy access to users public Turkish Electricity Market data.

# Covers

  - Consumption Data Services
  - Natural Gas Data Services
  - Market Data Services<br/>
    -Dayahead Market Data <br/>
    -Intraday Market Data <br/>
    -Balancing Power Market Data<br/>
    -Ancillary Services Data<br/>
 - Production Data Services<br/>
 - Tools (Which includes useful functions like exporting excel, creating basic report etc. )

### Installation

transparencyEpias requires python3 or latest versions to run.
Also following packages need to be installed. 
- pandas
- requests
- datetime
- json
- xlsxwriter

Install the dependencies and install transparencyEpias.

```sh
$ python -m pip install transparencyEpias
```

### Sample Usage

To be able to reach file user shoul follow instructions below.
- MCP Values Example:
 
```sh
from transparency_epias.markets import dayaheadClient 
```
```sh
mcp_list = dayaheadClient.dayahead.mcp(startDate='2020-05-10',endDate='2020-05-10')[1]
```
```sh
>>[249.99, 322.22, 321.82, 321.81, 310.01, 214, 79.96, 14.04, 1, 0, 0, 0, 0.87, 1, 4, 13.99, 97.45, 227.57, 299.99, 323.23, 321.85, 308.56, 289.8, 284.99]
```
- MCP Excel Export Example:
```sh
from transparency_epias.tools import reportClient
```
```sh
reportClient.reports.mcp_excel_export(startDate='2020-05-10',endDate='2020-05-10')
```
```sh
>> User should get an xlsx document includes daily MCP price values to the path that python runs.
```
- Simple Price Comparison Report Example:
```sh
from transparency_epias.tools import reportClient
```
```sh
reportClient.reports.compare_price()
```
```sh
>> User should get a xlsx document includes MCP, SMP, and Weighted Avarage Price 

values to the path that python runs.
```

License
----

MIT

Soruce
----

https://seffaflik.epias.com.tr/transparency/

https://seffaflik.epias.com.tr/transparency/technical/en/