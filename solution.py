import sys, getopt
from modules import flights


def main(argv):
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
    try:
        main(sys.argv[4:])       
    except Exception as error:
        print(error)
        print('Flight research has been stoped for one of the reasons mentioned above.')   


#test cases: 
# 1. átszállással: BPZ WTN
# 2. közvetlen járat: BPZ VVH

# test cases:
# 1. WUE-JBN are indirect journey?
# 