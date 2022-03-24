
#############################
## libraries and functions ##
############################# 

#import libraries needed for this proces
import requests
from datetime import datetime
import numpy
import time
import json
from pathlib import Path
import pandas as pd
from os.path import exists

##this block creates functions that can be used to extract the data from the steam API
##maybe we can add this block in the source file as a functions file

def get_request(url, parameters=None):
    #function to create an API request based on URL and  parameters
    response = requests.get(url=url, params=parameters)
    if response:
        time.sleep(1)
        return response.json()
    else:
        print("Request unsuccessful, retrying in 5 seconds.")
        time.sleep(5)
        return get_request(url, parameters)
    time.sleep(1)

def getAppList():
    #using the function to get all data id's which include appid and app name 
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    parameters = {"request": all}
    return get_request(url, parameters=parameters)
    print("Your request has been processed successfully, call upon 'data_ids' to preview the full list of IDs and names of all currently available products on Steam as of ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"), ".")
    
def getAppDetails(id):
    #function to collect the raw data from the api per app_id
    url = "http://store.steampowered.com/api/appdetails/"
    parameters = {"appids": {id}}
    raw_data = get_request(url, parameters=parameters)
    response = raw_data[str(id)]
    if(response['success']):
        data_json = response["data"]
        data_json['collection_details'] = {'created_by': 'our_scraper',
                                            'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
        f = open('..\\..\\data\\raw_data.json','a',encoding='utf-8')
        f.write(json.dumps(data_json)+'\n')
        f.close()
        return data_json
    return 
 