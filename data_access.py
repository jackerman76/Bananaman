"""This file contains operations for accessing datastore"""
from google.cloud import datastore
from post import Post
from user import User
from request import Request

"""Basic CRUD operations"""
def retrieve_entity(id, kind='user'):
    client = get_client()
    # Make sure this is an int; string will yield a different result.
    # It's OK to use strings instead, but make sure you're consistent.
    key = client.key(kind, int(id))
    return client.get(key)

"""Adds an entity to the datastore"""
def update_entity(entity):
    client = get_client()
    client.put(entity)


def delete_entity(id, kind='user'):
    client = get_client()
    key = client.key(kind, int(id))
    client.delete(key)

def get_entities(kind):
    """Returns List of entities"""
    result = []
    client = get_client()
    query = client.query(kind)
    for entity in query.fetch():
        result.append(entity)
    return result


def user_to_entity(user):
    """Converts a User object into an entity"""
    client = get_client()
    key = client.key('user')
    entity = datastore.Entity(key)
    entity['username'] = user.username
    entity['password'] = user.password
    if user.email:
        entity['email'] = user.email
#    if user.phone_number:
#        entity['phone_number'] = user.phone_number
    entity['bananas_given'] = user.bananas_given
    return entity


def post_to_entity(post):
    """Converts a post object into an entity"""
    client = get_client()
    key = client.key('post')
    entity = datastore.Entity(key)
    entity['username'] = post.username
    entity['geolocation'] = post.geolocation
    entity['quantity'] = post.quantity
    entity['timestamp'] = post.timestamp
    entity['description'] = post.description
    entity['status'] = post.status
    entity['picture'] = post.picture
    entity['availability_start'] = post.availability_start
    entity['availability_end'] = post.availability_end
    return entity

def request_to_entity(request):
    """Converts a request object into an entity"""
    client = get_client()
    key = client.key('request')
    entity = datastore.Entity(key)
    entity['username'] = request.username
    entity['timestamp'] = request.timestamp
    entity['quantity'] = request.quantity
    entity['radius'] = request.radius
    return entity


def entity_to_user(entity):
    """Converts an entity into a User object"""
    username = entity['username']
    password = entity['password']
    email = entity['email']
#    phone_number = entity['phone_number']
    bananas_given = entity['bananas_given']
    user = User(username, password, email, bananas_given)
    return user

def entity_to_post(entity):
    """Converts a entity into a post object"""
    username = entity['username']
    geolocation = entity['geolocation']
    quantity = entity['quantity']
    timestamp = entity['timestamp']
    description = entity['description']
    status = entity['status']
    picture = entity['picture'] or None
    availability_start = entity['availability_start'] or None
    availability_end = entity['availability_end']or None
    post = Post(username, description, geolocation,
                 quantity, status, timestamp, picture, availability_start=availability_start, availability_end=availability_end)
    return post

def entity_to_request(entity):
    """Converts a entity into a request object"""
    username = entity['username']
    timestamp = entity['timestamp']
    quantity = entity['quantity']
    radius = entity['radius']
    request = Request(username, timestamp,
                 quantity, radius)
    return request

def get_user_entity(user):
    """Takes user object and returns user entity"""
    client = get_client()
    query = client.query(kind="user")
    query = query.add_filter("username", "=", user.username)
    # query fetch returns an iterator
    for i in query.fetch():
        # return first (and only) one
        return i

def query_posts():
    client = get_client()
    query = client.query(kind="post")
    list = []
    for i in query.fetch():
        list.append(entity_to_post(i))
    return list

def query_posts_by_location(latitude, longitude, radius=1000000, posts=None):
    """Returns list of posts sorted by location"""
    posts = query_posts()
    list = []
    for post in posts:
        # calc distance also sets the distance attribute in posts
        sublist = [post.calc_distance(latitude, longitude), post]
        list.append(sublist)

    list.sort(key = lambda x: x[0]) # sorts based on first element of sublist, which is location
    sorted = []
    for sublist in list:
        print(sublist[0])
        if sublist[0] <= radius: sorted.append(sublist[1])
    return sorted


def query_user_requests(user):
    client = get_client()
    query = client.query(kind="request")
    query = query.add_filter("username", "=", user.username)
    return query.fetch()


def get_client():
    return datastore.Client()
