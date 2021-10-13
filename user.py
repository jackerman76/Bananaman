import time
import json
class User():

    def __init__(self, username=None, password=None):
        # create user id

        self.username = str(username)
        self.password = str(password)
        self.email = None
        self.phone_number = None
        self.posts = []
        self.requests = []

    def set_phone(self, phone_number): self.phone_number = phone_number

    def set_email(self, email): self.email = email

    def get_phone(self): return self.phone_number

    def get_email(self): return self.email

    def add_post(self, post):
        self.posts.append(post)

    def add_request(self, request):
        self.posts.append(request)

    def get_posts(self):
        return self.posts

    def get_requests(self):
        return self.requests

    def __str__(self):
        return str(self.toJSON())

    def toJSON(self):
         return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

def test():
    me = User("jackerman76", "111111")
    me.set_email("joshackerman417@gmail.com")
    me.set_phone(4128523638)
    me.add_post("1234")
    me.add_post("5677")
    me.add_post("1357")
    print(me.toJSON())
    print(me)
    print(me.posts)

def main():
    test()

if __name__ == '__main__':
    main()
