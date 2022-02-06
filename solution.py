import sys, getopt
from modules import flights


def main(argv):
    
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
    
    bag=None
    returns=None

    try:
      opts, args = getopt.getopt(argv,"b::r",["bags=","return"])
    except getopt.GetoptError:
      print('One of the arguments is invalid!')
      sys.exit(2)
    for opt, arg in opts:
        if opt in ('--bags'):
            bag=arg
        if opt in ('--return'):
            returns=eval('True')    
    
    if bag!=None and returns==None:
        flights.search(sys.argv[1],sys.argv[2],sys.argv[3],bags=bag)
    elif bag==None and returns!=None:
        flights.search(sys.argv[1],sys.argv[2],sys.argv[3],returns=returns)
    elif bag!=None and returns!=None:
        flights.search(sys.argv[1],sys.argv[2],sys.argv[3],bags=bag,returns=returns)
    else:
        flights.search(sys.argv[1],sys.argv[2],sys.argv[3])
        
        
if __name__=="__main__":
    '''
    Call of main function to launch flight search.
    '''
    try:
        main(sys.argv[4:])       
    except Exception as error:
        print(error)
        print('Flight research has been stoped for one of the reasons mentioned above.')   


