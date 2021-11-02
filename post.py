import time
class Post():
    def __init__(self, username, description, geolocation,
                 quantity, picture="None", status="Available", timestamp=None):
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
