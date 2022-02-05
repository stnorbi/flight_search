#from itertools import filterfalse
import csv
import json
from datetime import datetime,timezone
from modules import data_validation as dv
import pprint

def search(filepath,origin,destination,bags=0,returns=False):

    if returns==False:
        jsonOrig, jsonDest=read_csv(filepath,origin,destination)
        flights=get_flights(jsonOrig, jsonDest, origin,destination,bags)
    
    elif returns==True:
        
        #"To" flights
        jsonOrig, jsonDest=read_csv(filepath,origin,destination)
        l=get_flights(jsonOrig, jsonDest, origin,destination,bags)
        
        #"Return" flights
        jsonOrig, jsonDest=read_csv(filepath,destination,origin)
        r=get_flights(jsonOrig,jsonDest,destination,origin,bags)
        
        flights=l+r

    flights=sorted(flights, key = lambda i: i['total_price'])
    
    set_result('json_data.json',flights,returns)

def get_flights(jsonOrig,jsonDest,origin,dest,bags):
    bags=int(bags)
    l=[]
    for i in jsonOrig:
        if i['destination']==dest and bags<=int(i['bags_allowed']) and i['origin']==origin:
            l.append({'flights':[i],
                    'bags_allowed': i['bags_allowed'],
                    'bags_count': bags,
                    'destination': i['destination'],
                    'origin': i['origin'],
                    'total_price': float(i['base_price'])+(float(i['bag_price'])*float(bags)),
                    'travel_time': get_traveltime(i['arrival'],i['departure'])
                    })
        elif i['origin']==origin and i['destination']!=dest:
            for j in jsonDest:
                flights=dict()
                if i['destination']==j['origin'] and j['destination']==dest:
                    layover=get_layover(j['departure'],i['arrival'])
                    if (layover>1) and (layover<6):
                        if int(i['bags_allowed'])>int(j['bags_allowed']):
                            bags_allowed=j['bags_allowed']
                        else:
                            bags_allowed=int(i['bags_allowed'])
                        if  bags<=int(j['bags_allowed']):
                            l.append({'flights':[i,j],
                                'bags_allowed': bags_allowed,
                                    'bags_count': bags,
                                    'destination': j['destination'],
                                    'origin': i['origin'],
                                    'total_price': float(i['base_price'])+float(i['bag_price'])*float(bags)+float(j['base_price'])+float(j['bag_price'])*float(bags),
                                    'travel_time': get_traveltime(j['arrival'],i['departure'])
                                    })                     
    return l

def read_csv(filepath,origin,destination):
    jsonOrig=[]
    jsonDest=[]
    try:
        with open(filepath) as csvFile:
            csvReader=csv.DictReader(csvFile)
            for row in csvReader:
                dv.flight_no_checker(row['flight_no'])
                dv.geo_checker(row['origin'],'Origin')
                dv.geo_checker(row['destination'],'Destination')
                dv.timestamp_checker(row['departure'],'Departure')
                dv.timestamp_checker(row['arrival'],'Arrival')
                dv.float_checker(row['base_price'],'base_price')
                dv.integer_checker(row['bag_price'],'bag_price')
                dv.integer_checker(row['bags_allowed'],'bags_allowed')
                if row['origin']==origin:
                    jsonOrig.append(row)
                elif row['destination']==destination:# and row['origin']!=origin:
                    jsonDest.append(row)
        return jsonOrig, jsonDest
    except Exception as error:
        print('Please open an input file with appropriate structure and format!')

def get_layover(endtime,starttime):
    layover=(datetime.fromisoformat(endtime).astimezone(timezone.utc)-datetime.fromisoformat(starttime).astimezone(timezone.utc)).total_seconds() / 3600
    return layover


def get_traveltime(arrival,departure):
    traveltime=datetime.fromisoformat(arrival)-datetime.fromisoformat(departure)
    return traveltime

        
def set_result(filename,data,returns):
    print(json.dumps(data,sort_keys=False,indent=3,cls=DatetimeEncoder))
    if len(data)>0 and returns==False:
        with open(filename, 'w') as outfile:
            json.dump(data, outfile,cls=DatetimeEncoder)
        print('Number of flights found: '+str(len(data))+'\nSearch result has been saved into '+filename+'.')
    if len(data)>0 and returns:
        with open(filename, 'w') as outfile:
            json.dump(data, outfile,cls=DatetimeEncoder)
        print('Number of flights found, returns included: '+str(len(data))+'\nSearch result has been saved into '+filename+'.')
    if len(data)==0:
        print('There is no flight based on search parameters! Please choose another route or reduce the number of your lagguage!')    
    
    
class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)
        


def print_result(dict):
    pass