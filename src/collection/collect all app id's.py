##########################
## Collect all app id's ##
########################## 


#collect all app id's from steam 
data_ids = getAppList()

#Code to collect all app id's in one list and write them to a json file called app_ids 
all_app_ids = []
print("Creating a list of all IDs currently available on Steam")

for item in data_ids['applist']['apps']:
    all_app_ids.append(item['appid'])

f = open('..\\..\\data\\app_ids.json','w',encoding='utf-8')
f.write(json.dumps(all_app_ids)+'\n')
f.close()

print("List created sucessfully, the total number of IDs available on Steam is:", len(all_app_ids),".")