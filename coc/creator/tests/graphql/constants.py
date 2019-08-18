from requests import session


class GraphTest:
    SESS = session()
    GRAPHQL_URL = 'http://localhost:8000/graphql'
    CSRF_TOKEN = SESS.get(GRAPHQL_URL).cookies['csrftoken']

    HEADERS = {
        'X-CSRFToken': CSRF_TOKEN
    }
