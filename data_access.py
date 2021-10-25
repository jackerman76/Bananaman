"""This file contains operations for accessing datastore"""


"""Basic CRUD operations"""
def create_entity(kind='user'):
    client = get_client()
    # Calling key without an ID will generate (an int) one for you.
    key = client.key(kind)
    return datastore.Entity(key)


def retrieve_entity(id, kind='user'):
    client = get_client()
    # Make sure this is an int; string will yield a different result.
    # It's OK to use strings instead, but make sure you're consistent.
    key = client.key(kind, int(id))
    return client.get(key)


def update_entity(entity):
    client = get_client()
    client.put(entity)


def delete_entity(id, kind='user'):
    client = get_client()
    key = client.key(kind, int(id))
    client.delete(key)

def get_entities(kind="message"):
    """Returns List of entities"""
    result = []
    client = get_client()
    query = client.query(kind=kind)
    for entity in query.fetch():
        result.append(entity)
    return result


def get_client():
    # Note that if we want to specify a project here, we could do it like this:
    # return datastore.Client('your-project-id')
    # Calling Client() with no argument will access the environment variables
    # for your project - which will be fine for your deployed application.
    return datastore.Client()
