class Request():
    def __init__(self, user_id, timestamp,
                 quantity, radius, description):
        self.user_id = user_id
        self.timestamp = timestamp
        self.quantity = quantity
        self.radius = radius
        self.description = description
