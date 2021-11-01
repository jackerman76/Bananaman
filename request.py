class Request():
    def __init__(self, request_id, user_id, timestamp,
                 quantity, radius):
        self.request_id = request_id
        self.user_id = user_id
        self.timestamp = timestamp
        self.quantity = quantity
        self.radius = radius
