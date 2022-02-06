from datetime import datetime

def flight_no_checker(flight_no):
    '''
    # Input argument(s):
        flight_no: identification number of a flight / airplane.
    
    # Purpose:
    Takes string representation of flight number and check its length and string-number elements
    based on standard(s) assumed.
     - Flight number length has to be 5 characters.
     - First 2 character of flight number have to be string and the rest of it should be number.
    '''
    if len(flight_no)!=5 or (isinstance(flight_no[:2],str)==False or flight_no[2:].isdigit())==False:
        exit('Input file contains invalid flight number such as '+"'"+flight_no+"'"+' !')
             

def geo_checker(geo_cd,paramname):
    '''
    # Input argument(s):
        geo_cd: identification characters of airport
        paramname: it can be origin / destination, it depends on function utilization
        
    # Purpose:
        Checks the length of geographical codes and their composition.
        - geo_cd has to be 3 character long string.
    '''
    if isinstance(geo_cd,str)==False or (len(geo_cd)==3)==False or any(char.isdigit() for char in geo_cd):
        exit(geo_cd + ' is not a valid geo code to '+paramname+' airport. Please fix adequate field of input file!')


def timestamp_checker(timestamp,paramname):
    '''
    # Input argument(s):
        timestamp: string representation of departure / arrival time
        paramname: it can be departure / arrival, it depends on function utilization
        
    # Purpose:
        Checks the timestamp ISO format and its correctness.
        - timestamp has to be ISO format timestamp.
    '''
    try:
        datetime.fromisoformat(timestamp)
    except ValueError as error:
        exit("Sorry but date format of "+ timestamp+ " is unacceptable in the field "+ paramname + " of input file:\n\t"+str(error))

def integer_checker(number,paramname):
    '''
    # Input argument(s):
        number: string format of a number
        paramname: it can be bag_price / bags_allowed it depends on function utilization
        
    # Purpose:
        Checks string represent is digit or not.
        - number has to be digit.
    '''    
    if number.isdigit()!=True:
        exit(number + ' is not a number in '+paramname +'field. Please fix adequate field of input file!')

def float_checker(number,paramname):
    '''
    # Input argument(s):
        number: string format of a number
        paramname: it can be base_price, it also depends on function utilization
        
    # Purpose:
        Checks string represent is float or not.
        - number has to be float.
    '''
    try:
        float(number)
    except ValueError:
        exit(paramname + ' is not a number. Please fix adequate field of input file!')
