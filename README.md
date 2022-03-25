

# Steam-API
![Steam Logo](https://upload.wikimedia.org/wikipedia/commons/8/87/New_Steam_Logo_with_name.jpg)


# index
1. About-this-project
2. Repository overview
3. Running instructions
4. Documentation  
5. About 
6. Contributors 

 

# About-this-project  

Gaming has become one of the most valuable and fast growing industries worldwide. The Covid-19 pandemic was as unpredictable as it was beneficial for the video game industry, with public interest increasing even more. The video game industry is generally highly secretive with its information. Not only publishers and developers, but also distribution platforms such as Steam, Playstation Store, Epic Games, and more. The scarceness of information in this sector has a negative impact on the posibility to research in this domain. Research observing how video games as media affects us mentally or cognitively is far more prevalent and varied than statistical studies done within the industry. 
   
  
To aid against the lack of available data on the video game industry, this team proposes the creation of datasets through the use of Steam API. Steam API enables the collection of various data points pertaining to users and video games available in its online retail store. This project specifically will focus on the collection of software datapoints as provided by Steam in an attempt to create a dataset that includes a comprehensive list of software available for sale.

Our full research documentation can be found in the [**documentation**](https://github.com/opgeROBt/steam-API/tree/main/documentation) folder. 

# Repository overview
### **scr/collection** 
The src folder contains two folders for collection and reporting. The collection folder holds the seperate python files that are needed to collect the data and parse them in seperate files or dataframes. The folder reporting is at this moment empty and can be used for reporting purposes when working with the data. For now this was left empty since our project focused mainly on collecting the data. 

### **data** 
Data collected trough the files in src/collection are automatically written to the data folder. Collected data consists of raw .json files containing app ids, collected app ids, and the raw data. Furthermore, with the parsing script all nested json objects in the raw dataset and the raw dataset are writen to .xlsx files and saved in the data folder.  

### **documentation** 
Our full research documentation can be found in the [**documentation**](https://github.com/opgeROBt/steam-API/tree/main/documentation) folder. 


# Running instructions 

### **run in following order**  
"libraries and functions.py" ->  "collect all app id's.py" -> "collect appdetails.py" ->  "parsing nested json into dataframes and excel files.py"


### **step 1 | installing libraries and functions**
The following libraries are needed to run the code. These have been added in the 'libraries and functions script which should always be run as the first script. 
 

```
import requests
from datetime import datetime
import numpy
import time
import json
from pathlib import Path
import pandas as pd
from os.path import exists
```

```
get_request(url, parameters=None)  #creates the get request to collect data, used in getAppDetails
getAppList()                       #gets the full  list of current app_id's from the store.steampowered API
getAppDetails(id)                  #the function used to collect the appdetails per app_id 
```

### **step 2 | collect available app_ids**
By running the code from 'collect all app id's.py'  all app ids from the steam store are collected in the 'app_ids.json' and saved in the /data folder. 

### **step 3 | collect app_details per app_id**
This is where the magic happens and the details of every app is collected and put in a big raw_data.json. It is possible to specify of how many app_id's the details should be collected. Since running the code can be very time consuming. Benchmark: circa 60 minutes per 2500 app ids. This is due to the **limitations** that are set. Although there is no official documentation on this, there is a limit of around 10 calls per 10 seconds with a maximum of 100.000 calls per day. Furthermore, a timestamp is added to the collected data to keep track of when which records have been collected.  

### **step 4 | parse raw data to usable datasets**
This code parses all the data in the raw_data.json file and puts for every nested category the data in seperate dataframes. The steam_appid is included in the parsed dataframe which gives the option to join the data to the raw dataset when further exploration is needed.   

# About 
This is the repository for the course [Online Data Collection and Management ](https://odcm.hannesdatta.com/) at Tilburg University as part of the Master's program 'Marketing Analytics'.    




# Contributors  
 * [Cas van Dijk](https://github.com/Cas-24), c.c.j.m.vandijk@tilburguniversity.edu
 * [Chokie Tang](https://github.com/chokietang), c.k.tang@tilburguniversity.edu
 * [Rob Esenkbrink](https://github.com/opgeROBt), r.m.esenkbrink@tilburguniversity.edu
 * [Michael Serbanescu](https://github.com/MihaiVladS), v.serbanescu@tilburguniversity.edu
 * [Anoesjka Raateland](https://github.com/Anoesjka97), a.raateland@tilburguniversity.edu




