"""This file contains operations for accessing datastore"""
from google.cloud import datastore
from post import Post
from user import User

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
    key = client.key('user', user.user_id)
    entity = datastore.Entity(key)
    entity['user_id'] = user.user_id
    entity['username'] = user.username
    entity['password'] = user.password
    entity['email'] = user.email
    entity['phone_number'] = user.phone_number
    entity['bananas_given'] = user.bananas_given
    return entity


def post_to_entity(post):
    """Converts a post object into an entity"""
    client = get_client()
    key = client.key('post', post.post_id)
    entity = datastore.Entity(key)
    entity['post_id'] = post.post_id
    entity['user_id'] = post.user_id
    entity['geolocation'] = post.geolocation
    entity['quantity'] = post.quantity
    entity['timestamp'] = post.timestamp
    entity['description'] = post.description
    entity['status'] = post.status
    entity['image'] = post.image
    return entity

def request_to_entity(request):
    """Converts a request object into an entity"""
    client = get_client()
    key = client.key('request', request.request_id)
    entity = datastore.Entity(key)
    entity['user_id'] = request.user_id
    entity['timestamp'] = request.timestamp
    entity['quantity'] = request.quantity
    entity['radius'] = request.radius
    return entity


def entity_to_user(entity):
    """Converts an entity into a User object"""
    user_id = entity['user_id']
    username = entity['username']
    password = entity['password']
    email = entity['email']
    phone_number = entity['phone_number']
    bananas_given = entity['bananas_given']
    user = User(user_id, username, password, email, phone_number, bananas_given)
    return user

def entity_to_post(entity):
    """Converts a entity into a post object"""
    post_id = entity['post_id']
    user_id = entity['user_id']
    geolocation = entity['geolocation']
    quantity = entity['quantity']
    timestamp = entity['timestamp']
    description = entity['description']
    status = entity['status']
    picture = entity['picture']
    post = Post(post_id, user_id, description, geolocation,
                 quantity, timestamp, picture, status)
    return post

def entity_to_request(entity):
    """Converts a entity into a request object"""
    user_id = entity['user_id']
    timestamp = entity['timestamp']
    quantity = entity['quantity']
    radius = entity['radius']
    request = Request(request_id, user_id, timestamp,
                 quantity, radius)
    return post

def get_client():
    # Note that if we want to specify a project here, we could do it like this:
    # return datastore.Client('your-project-id')
    # Calling Client() with no argument will access the environment variables
    # for your project - which will be fine for your deployed application.
    return datastore.Client()
