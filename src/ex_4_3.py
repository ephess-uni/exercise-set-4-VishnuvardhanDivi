""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    shdwns = get_shutdown_events(logfile)
    
    sh11 = shdwns[0]
    
    sh22 = shdwns[-1]
       
    sh11_date = logstamp_to_datetime(sh11.split()[1])
    
    sh22_date = logstamp_to_datetime(sh22.split()[1])
    
    diff = sh22_date-sh11_date
    
    return diff


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
