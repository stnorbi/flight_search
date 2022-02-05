from datetime import datetime

def flight_no_checker(flight_no):
    if len(flight_no)!=5 or (isinstance(flight_no[:2],str)==False or flight_no[2:].isdigit())==False:
        exit('Input file contains invalid flight number such as '+"'"+flight_no+"'"+' !')
             

def geo_checker(geo_cd,paramname):
    if isinstance(geo_cd,str)==False or (len(geo_cd)==3)==False or any(char.isdigit() for char in geo_cd):
        exit(geo_cd + ' is not a valid geo code to '+paramname+' airport. Please fix adequate field of input file!')


def timestamp_checker(timestamp,paramname):
    try:
        datetime.fromisoformat(timestamp)
    except ValueError as error:
        exit("Sorry but date format of "+ timestamp+ " is unacceptable in the field "+ paramname + " of input file:\n\t"+str(error))

def integer_checker(number,paramname):
    if number.isdigit()!=True:
        exit(number + ' is not a number in '+paramname +'field. Please fix adequate field of input file!')

def float_checker(number,paramname):
    try:
        float(number)
    except ValueError:
        exit(paramname + ' is not a number. Please fix adequate field of input file!')
