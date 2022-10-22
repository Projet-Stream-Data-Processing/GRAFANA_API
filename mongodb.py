from pymongo import MongoClient

mongoUser="user"
mongoPass="password"
mongoClient = MongoClient(f"mongodb://{mongoUser}:{mongoPass}@localhost:27017")
db=mongoClient.Velov
c_StationName=db.StationName
c_Station=db.Station

def mongodb_stations_infos():
    return [e for e in c_StationName.find({},{"_id":0})]



def mongodb_stations_bikes():
    return [e for e in c_Station.find({},{"_id":0})]



