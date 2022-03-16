## collecting the data with a for loop that checks if the response was a succes = True. and than takes the data attribute 
## with addition of try and excepts from michael 

details = {} 

counter = 1   
for i in app_ids: 
    url = "http://store.steampowered.com/api/appdetails/"
    parameters = {"appids": {i}}
    app_data = get_request(url, parameters=parameters)
    id = str(i)
    print("Processing data pertaining to Steam ID:"+id)
    response = app_data[id]
    succes = response["success"]
    if (succes): 
        data_json = response["data"]
        try:
            app_id = data_json["steam_appid"]
            name = data_json["name"]
            prod_type = data_json["type"]
            freemium = data_json["is_free"]
            price = data_json["price_overview"]["final_formatted"]
            discount = data_json["price_overview"]["discount_percent"]
            developer = data_json["developers"]
            publisher = data_json["publishers"]
            desc = data_json["detailed_description"]
            short_desc = data_json["short_description"]
            try:
                release_date = data_json["release_date"]["date"]
            except:
                release_date = "TBA"
            try:
                win = data_json["platforms"]["windows"]
            except:
                win = ""
            try:
                mac = data_json["platforms"]["mac"]
            except:
                mac = ""
            try:
                lin = data_json["platforms"]["linux"]
            except:
                lin = ""
            try:
                achievements = data_json["achievements"]["total"]
            except:
                achievements = "0"
            try:
                reviews = data_json["recommendations"]
            except:
                reviews = ""
            try:
                metacritic = data_json["metacritic"]
            except:
                metacritic = "not available"
            try:
                base_app = data_json["fullgame"]["appid"]
            except:
                base_app = "none"
            scrape_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            details[app_id]=[name],[release_date],[freemium],[prod_type],[price],[discount],[developer],[publisher],[desc],[short_desc],[achievements],[win],[mac],[lin],[reviews],[metacritic],[base_app],[scrape_datetime]
        except:
            pass
        counter = counter + 1 
    if (counter > 10000):
        break           
