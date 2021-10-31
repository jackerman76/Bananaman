import time
class Post():
    def __init__(self, post_id, user_id, description, geolocation,
                 quantity, timestamp, picture, status):
        # post_id is id of post in datastore
        # user_id is id of associated user in datastore
        # Implement pictures and geolocation later
        self.post_id = post_id
        self.user_id = user_id
        self.description = description
        self.geolocation = geolocation
        self.quantity = None
        self.timestamp = time.time()
        self.picture = picture
        self.status = status 
