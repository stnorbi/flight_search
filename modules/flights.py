#from itertools import filterfalse
import csv
import json
from datetime import datetime,timezone
from modules import data_validation as dv
import pprint

def search(filepath,origin,destination,bags=0,returns=False):
    '''
    # Input argument(s):
        filepath: input file location in the filesystem
        origin: geoagraphical code of origin airport
        destination: geoagraphical code of destination airport
        bags: number of bags what user would like to take. By default not taking any lagguage   
              (default value=0)
        returns: boolean value to flag search return flights as well, by default not search for flight 
                (default value=False)
        
    # Purpose:
        Main method to read input file and trigger flight(s) search based on returns flag.
        If the user would like to get return flights as well, result set will include flight 
        into both direction (there and back again)
    
    # Return:
         json-compatible structured list and result set sorted by total_price of journey saved into "json_data.json" 

    '''

    if returns==False:
        jsonOrig, jsonDest=read_csv(filepath,origin,destination)
        flights=get_flights(jsonOrig, jsonDest, origin,destination,bags)
    
    elif returns==True:
        
        #"To" flights
        jsonOrig, jsonDest=read_csv(filepath,origin,destination)
        l=get_flights(jsonOrig, jsonDest, origin,destination,bags)
        
        #"Return" flights: in this case origin and destination airports got swapped
        jsonOrig, jsonDest=read_csv(filepath,destination,origin)
        r=get_flights(jsonOrig,jsonDest,destination,origin,bags)
        
        flights=l+r

    flights=sorted(flights, key = lambda i: i['total_price'])
    
    set_result('json_data.json',flights,returns)
    
    return flights

def get_flights(jsonOrig,jsonDest,origin,dest,bags):
    '''
    # Input argument(s):
        jsonOrig: list of flight which departure from origin airport
        jsonDest: list of flight which arrive to destination airport
        origin: geoagraphical code of origin airport
        dest: geoagraphical code of destination airport
        bags: number of bags what user would like to take
        
    # Purpose:
        Gather direct and indirect flights.
            - Direct flight: passenger does not have to change flights
            - Indirect flight: passenger has to change flights
        Taking into account number of bags as constrain in both of the cases (direct and indirect flights).
        Overlay as condition comes to the picture regarding indirect flights. 
        (Only journeys will be part of search result set which  overlay time between flights is greater than 1 hour and less than 6 hours)
    
    # Return:
        It returns a list of the single and paired flights.
    '''
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
                    overlay=get_overlay(j['departure'],i['arrival'])
                    if (overlay>1) and (overlay<6):                                 # Overlay conditioning
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
    '''
    # Input argument(s):
        filepath: list of flight which departure from origin airport
        origin: geoagraphical code of origin airport
        destination: geoagraphical code of destination airport
        
    # Purpose:
        Read input file and validate input values row by row.

    # Return:
        jsonOrig: list of rows from input file where origin airport geo-code is equal to corresponding search parameter
        jsonDest: list of rows from input file where destination airport geo-code is equal to corresponding search parameter
    
    '''
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

def get_overlay(endtime,starttime):
    '''
    # Input argument(s):
        endtime: string representation of timestamp regarding end of period (e.g. departure time in case of flight change)
        starttime: string representation of timestamp regarding start of period (e.g. arrival time in case of change for prior fligth)
        
    # Purpose:
        Calculate overlay time.

    # Return:
        overlay: waiting time amount between flights.
    
    '''
    overlay=(datetime.fromisoformat(endtime).astimezone(timezone.utc)-datetime.fromisoformat(starttime).astimezone(timezone.utc)).total_seconds() / 3600
    return overlay


def get_traveltime(arrival,departure):
    '''
    # Input argument(s):
        arrival: string representation of timestamp regarding beginning of journey
        departure: string representation of timestamp regarding end of journey
        
    # Purpose:
        Calculate time consumption of entire journey.

    # Return:
        traveltime: Time needs to the journey from original airport to final destionation one.
    
    '''
    traveltime=datetime.fromisoformat(arrival)-datetime.fromisoformat(departure)
    return traveltime

        
def set_result(filename,data,returns):
    '''
    # Input argument(s):
        filename: name of file in which data be stored
        data: json-compatible structured list
        returns: boolean flag to decide search result includes return flights or not.
        
    # Purpose:
        Search result set be printed to the terminal and saved into a file

    # Return:
        Json file in the filesystem and search result printed to the terminal.
    
    '''
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
    '''
    # Input argument(s):
        json.JSONEncoder: class to serialize object while performing encoding
        
    # Purpose:
        Handle result set to get formatted in a proper way during printing to terminal and storing into file.

    # Return:
        String representation of python object
    
    '''
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)
