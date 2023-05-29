"""
Follwing is the example of logging in python:
The filename file will be places in the cwd() if the relative path is given.
We can disable the log messages by using logging.disable()
LOG LEVEL:
debug(lowest)
info
warning
error
critical(highest)

"""
import logging
logging.basicConfig(filename ='Logfile.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# logging.disable(logging.CRITICAL) This will disable all the log messages where condition is critical or low.
logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s)' %(n))
    total =1
    for i in range(1,n+1):
        total *= i
        logging.debug('i is %s, total is %s' %(i, total))
    logging . debug('Return value is %s' %(total))
    return total

print(factorial(5))

logging.debug('End of program')
