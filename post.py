import time
from time import gmtime, strftime
import datetime

class Post():
    def __init__(self, username, description, geolocation,
                 quantity, status="Available", timestamp=None, picture="None"):
        # post_id is id of post in datastore
        # user_id is id of associated user in datastore
        # Implement pictures and geolocation later
        self.username = username
        self.description = description
        self.geolocation = geolocation
        self.quantity = quantity
        if timestamp:
            self.timestamp = timestamp
        else:
            self.timestamp = time.time()
        self.picture = picture
        self.status = status 
        
    def get_time(self):
        return time.localtime(self.timestamp) - time.timezone

    def get_time_as_time(self):
        return str(time.strftime("%H:%M %p", self.get_time()))

    def get_time_as_date(self):
        return str(time.strftime("%x", self.get_time()))

    def get_time_as_hrs_ago(self):
        hrs = int(time.strftime("%H", time.localtime())) - int(time.strftime("%H", self.get_time()))
        return str(hrs) + " hours ago"

    def get_formatted_time(self):
        # calc difference in time in hours
        diff = (time.time() - self.timestamp) / (60 ** 2)

        if (diff < 2):
            return self.get_time_as_time()
        if (diff < 24):
            return self.get_time_as_hrs_ago()
        else:
            return self.get_time_as_date()
