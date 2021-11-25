import time
from time import gmtime, strftime
from datetime import datetime
from geopy import distance
import json

class Post():
    def __init__(self, username, description, geolocation,
                 quantity, status="Available", timestamp=None, picture="None",
                 availability_start=None, availability_end=None):
        # post_id is id of post in datastore
        # user_id is id of associated user in datastore
        # Implement pictures and geolocation later
        self.username = username
        self.description = description
        self.geolocation = geolocation # "[latitude,longitude]"
        self.quantity = quantity
        if timestamp:
            self.timestamp = timestamp
        else:
            self.timestamp = time.time()
        self.picture = picture
        self.status = status
        self.availability_start = availability_start
        self.availability_end = availability_end
        self.formatted_time = None
        self.distance = None

    def has_geolocation(self):
        return self.geolocation != None

    def get_latitude(self):
        self.latitude = float(json.loads(self.geolocation)[0]) or None
        return self.latitude

    def get_longitude(self):
        self.longitude = float(json.loads(self.geolocation)[1]) or None
        return self.longitude

    def calc_distance(self, latitude, longitude):
        u = (latitude, longitude)
        p = (self.get_latitude(), self.get_longitude())
        self.distance = distance.distance(u, p).miles
        return self.distance

    def get_availability_start_dt(self):
        return datetime.strptime(self.availability_start, '%Y-%m-%dT%H:%M')

    def get_availability_end_dt(self):
        return datetime.strptime(self.availability_end, '%Y-%m-%dT%H:%M')

    def available_now(self):
        start = self.get_availability_start_dt()
        end = self.get_availability_end_dt()
        now = datetime.now()
        return now >= start and now <= end 

    def get_dt(self):
        return datetime.fromtimestamp(self.timestamp)

    def get_formatted_time(self):
        delta = datetime.now() - self.get_dt()
        if delta.days != 0:
            return str(int(delta.days)) + " days ago"

        if delta.seconds > 3600:
            return str(int(delta.seconds/3600)) + " hours ago"

        else:
            return str(int(delta.seconds/60)) + " minutes ago"
    def as_json(self):
        self.formatted_time = self.get_formatted_time()
        return json.dumps(self.__dict__)


#post = Post(username = "test_username", description = "test_desc", geolocation = "[35.035729, -85.31293699999999]", quantity = 3, status="Available", timestamp=1637848591.016366, picture="https://storage.googleapis.com/banana-post-pictures/image.jpgjackerman761637792419.9615953", availability_start="2018-06-07T00:00", availability_end="2018-06-14T00:00")
