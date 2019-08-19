from requests import session


class GraphTest:
    sess = session()
    graphql_url = 'http://localhost:8000/graphql'
    csrf_token = sess.get(graphql_url).cookies['csrftoken']

    headers = {
        'X-CSRFToken': csrf_token
    }

    def run_query(self, query: str):
        """Run a query against the graphql layer.
        Arguments:
            query -- (str) query to be run.
        """
        response = self.sess.post(
            self.graphql_url,
            json={'query': query},
            headers=self.headers
        )
        data = response.json()['data']
        status = response.status_code
        return data, status
