from pymongo import MongoClient

mongoUser="user"
mongoPass="password"
mongoClient = MongoClient(f"mongodb://{mongoUser}:{mongoPass}@localhost:27017")
db=mongoClient.Velov
c_StationName=db.StationName
c_Station=db.Station

def get_stations_infos():
    return [e for e in c_StationName.find({})]



def get_stations_bikes():
    a = [e for e in c_Station.find({})]
    return a[:100]


if __name__ == "__main__":
    data = get_stations_bikes()
    print(data)
    

