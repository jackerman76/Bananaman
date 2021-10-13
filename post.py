import time
class Post():
    def __init__(self, user_id):

        self.user_id = user_id
        self.description = None
        #self.geolocation
        self.quantity = None
        self.timestamp = time.time()
        #self.picture = "/path/to/picture.PNG"
        self.status = "Available"
