import pandas as pd 
import requests
import json
from datetime import timedelta 
from datetime import datetime
import validate as val

class balancingPowerClient:

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

balancingPower = balancingPowerClient()