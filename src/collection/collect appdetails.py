########################
## Collect appdetails ##
######################## 

#This code can be run to collect the appdetails, in case there was data collected earlier in the raw_data.json file than it will add to existing files. 
#put the amount of appids you want to collect in the 'limit'parameter
counter = 0
limit = 100

## collect app_ids from the  app_ids file created before 
r = open('..\\..\\data\\app_ids.json','r',encoding='utf-8')
app_ids = json.load(r)

## creates an empty raw_data.json that can be appended on
f = open('..\\..\\data\\raw_data.json','a',encoding='utf-8') 

# check if the json from earlier was created and set limit 
raw_exists = exists("..\\..\\data\\raw_data.json")

#create list of already collected id's 
if (raw_exists):
    #create list of collected id's 
    col_ids = []
    with open('..\\..\\data\\raw_data.json') as f: 
        for jsonObj in f: 
            rawDict = json.loads(jsonObj)
            col_ids.append(rawDict["steam_appid"])

## getting the new data
#  keep in mind that while running the code it can reach a limit, letting it run it automaticly continues after 2 minutes or so 
for i in app_ids: 
    if i not in col_ids:
        if(counter > limit):
            break
        id = str(i)
        counter = counter + 1
        try:
            app_data = getAppDetails(i)
            print("Processing data pertaining to Steam ID:"+id)
        except:
            pass
    else:
        print(f"Skipping id {str(i)}")

##create json file with collected id's 
if (raw_exists):
    col_ids = []
    with open('..\\..\\data\\raw_data.json') as f: 
        for jsonObj in f: 
            data = json.loads(jsonObj)
            col_ids.append(data["steam_appid"])
        f = open("..\\..\\data\\collected_ids.json", "w",encoding='utf-8')
        f.write(json.dumps(col_ids)+"\n")
        f.close()
