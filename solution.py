import sys, getopt
import argparse
from xmlrpc.client import boolean
from modules import flights


def main(argparse):
    
    '''
    It is dedicated to trigger flight search and that before receive mandatory and optional paramaters from terminal.
    Also handling wrong input parameters by try-except statements with custome error message.
    
    # Parameters:
    -------Mandatories------
    $1: filename / filepath of input file (e.g. example3.csv)
    $2: geoagraphical code of origin airport
    $3: geographical code of destination airport
    
    -------Optionals--------
    -b (--bags): number of bags what user would like to take
    -r (--return): boolean value to flag search return flights as well
    
    '''
    parser = argparse.ArgumentParser(description='Process input file path, code of airports and.'
                                     ,epilog="If you want to take bag(s) or search for return flights please add parameters accordingly.")
    
    parser.add_argument('filepath',metavar='datasource',type=str,nargs=1,
                        help='File containing data set of flights.')
    parser.add_argument('airport', metavar='airports', type=str, nargs=2,
                    help='Please add airport codes (Origin and Destination airports as well)')
    parser.add_argument('--bags', metavar='b', type=int, default=0,
                    help='Indicates number of bags you want to take')
    parser.add_argument('--return',type=bool,default=False,const="default",nargs='?',
                        help="Indicate you want to search for return flights. Deafult is NO")
    args = parser.parse_args()
    print(args)
    print(args.airport[0])
    flights.search(args.filepath[0],args.airport[0],args.airport[1],bags=args.bags,returns=False)
        
if __name__=="__main__":
    '''
    Call of main function to launch flight search.
    '''

    try:
        main(argparse)       
    except Exception as error:
        print(error)
        print('Flight research has been stoped for one of the reasons mentioned above.')   


