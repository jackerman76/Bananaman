"""This file contains operations for accessing datastore"""
from google.cloud import datastore
from listing import Listing
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


def userToEntity(user):
    """Converts a User object into an entity"""
    client = get_client()
    key = client.key('user', user.user_id)
    entity = datastore.Entity(key)
    entity['userId'] = user.user_id
    entity['username'] = user.username
    entity['password'] = user.password
    entity['email'] = user.email
    entity['phoneNumber'] = user.phone_number
    entity['bananasGiven'] = user.bananasGiven
    return entity


def listingToEntity(listing):
    """Converts a Listing object into an entity"""
    client = get_client()
    key = client.key('listing', listing.listing_id)
    entity = datastore.Entity(key)
    entity['listingId'] = listing.listing_id
    entity['sellerId'] = listing.seller_id
    entity['location'] = listing.location
    entity['sellerUsername'] = listing.seller_username
    entity['email'] = listing.userEmail
    entity['phoneNumber'] = listing.userPhoneNumber
    entity['listingId'] = listing.listing_id
    entity['amtBananas'] = listing.amtBananas
    return entity

def entityToUser(entity):
    """Converts an entity into a User object"""
    userId = entity['userId']
    username = entity['username']
    password = entity['password']
    email = entity['email']
    phoneNumber = entity['phoneNumber']
    bananasGiven = entity['bananasGiven']
    user = User(userId, username, password, email, phoneNumber, bananasGiven)
    return user

def entityToListing(entity):
    """Converts a entity into a Listing object"""
    listingId = entity['listingId']
    sellerId = entity['sellerId']
    sellerUsername = entity['sellerUsername']
    location = entity['location']
    email = entity['email']
    phoneNumber = entity['phoneNumber']
    listingId = entity['listingId']
    amtBananas = entity['amtBananas']
    listing = Listing(sellerId, sellerUsername, location, email, phoneNumber, listingId, amtBananas)
    return listing

def get_client():
    # Note that if we want to specify a project here, we could do it like this:
    # return datastore.Client('your-project-id')
    # Calling Client() with no argument will access the environment variables
    # for your project - which will be fine for your deployed application.
    return datastore.Client()
