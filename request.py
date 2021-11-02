import time
class Request():
    def __init__(self, request_id, user_id, timestamp,
                 quantity, radius):
        self.request_id = request_id
        self.user_id = user_id
        if not timestamp:
            self.timestamp = time.time()
        else:
            self.timestamp = timestamp
        self.quantity = quantity
        self.radius = radius
