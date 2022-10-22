from pymongo import MongoClient
from calendar import timegm
from datetime import datetime
mongoUser="user"
mongoPass="password"
mongoClient = MongoClient(f"mongodb://{mongoUser}:{mongoPass}@localhost:27017")
db=mongoClient.Velov
c_StationName=db.StationName
c_Station=db.Station


def convert_to_time_ms(timestamp):
    return 1000 * timegm(datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S').timetuple())


def mongodb_stations_infos():
    return [e for e in c_StationName.find({},{"_id":0})]



def mongodb_stations_bikes():
    return [e for e in c_Station.find({},{"_id":0})]



def stations(recherche:str):
    r = []
    if recherche == "all_bike_stands" or recherche == "all_available_bikes":
        if recherche == "all_bike_stands":
            recherche_ = "available_bike_stands"
        elif recherche == "all_available_bikes":
            recherche_ = "available_bikes"

        d = {}
        for e in c_Station.find({},{"_id":0}):
            if not convert_to_time_ms(e['timestamp']) in d:
                d[convert_to_time_ms(e['timestamp'])] = int(e[recherche_])
            else:
                d[convert_to_time_ms(e['timestamp'])] += int(e[recherche_])
        for k,v in d.items():
            r.append([v,k])
        return r
        
        
    
    for e in c_Station.find({},{"_id":0}):
        r.append([e[recherche],convert_to_time_ms(e['timestamp'])])
    
    return r