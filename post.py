import time
from time import gmtime, strftime
from datetime import datetime

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


    def get_dt(self):
        return datetime.fromtimestamp(self.timestamp)

    def get_formatted_time(self):
        delta = datetime.now() - self.get_dt()
        if delta.days != 0:
            return str(int(days)) + " days ago"

        if delta.seconds > 3600:
            return str(int(delta.seconds/3600)) + " hours ago"

        else:
            return str(int(delta.seconds/60)) + " minutes ago"
