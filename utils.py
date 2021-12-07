import time
from datetime import datetime
def datetime_input_dt(input):
    """converts html datetime-local input to datetime"""
    dt = datetime.strptime(input, '%Y-%m-%dT%H:%M')
    return dt

def datetime_to_timestamp(dt):
    timestamp = time.mktime(dt)
    return timestamp
