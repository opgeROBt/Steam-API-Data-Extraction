#########################################################
## parsing nested json into dataframes and excel files ##
#########################################################



#This code takes the raw_data.json output and parses it based on the keys given in the code. 
keys = ['categories','package_groups','genres','screenshots','movies']
Allkeys = ['raw', 'categories','package_groups','genres','screenshots','movies']
dataframes = {}

#creates dataframes for the seperate parsing keys 
for k in Allkeys:
    file = f"..\\..\\data\\dataframe_{k}.xlsx"
    try:
        dataframes[k] = pd.read_excel(file)
    except:
        print(f"File doesn't exist {file}")
        dataframes[k] = pd.DataFrame()
        pass

##parses data into seperate keys 
raw_exists = exists("..\\..\\data\\raw_data.json")
if (raw_exists):
    app_data = []
    with open('..\\..\\data\\raw_data.json') as f: 
        for jsonObj in f: 
            result = json.loads(jsonObj)
            app_data.append(result)
            for key in keys:
                if( key not in dataframes):
                    dataframes[key] = pd.DataFrame()
                try:
                    data = pd.json_normalize(result,record_path = [key], meta = ["steam_appid"], errors="ignore")
                    dataframes[key] = pd.concat([dataframes[key],data])            
                    print(key)
                except:
                    pass
        result = pd.json_normalize(app_data)
        dataframes['raw'] = pd.concat([dataframes['raw'], result])

#writing the new data to the .xlsx files from the new dataframes
for key in Allkeys:
    print(f"Writing to dataframe {key}")
    file = f"..\\..\\data\\dataframe_{key}.xlsx"
    print(dataframes[key])
    with pd.ExcelWriter(file,mode = 'w') as writer: 
        dataframes[key].to_excel(writer)