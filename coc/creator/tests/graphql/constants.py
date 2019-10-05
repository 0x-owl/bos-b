from os import environ
from random import choice

from requests import session


class GraphTest:
    """GraphQL abstraction test class."""
    sess = session()
    sess.trust_env = False
    host = 'coc' if environ.get('ENV', None) == 'Docker' else 'localhost'
    graphql_url = f"http://{host}:8000/graphql"
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

    def full_research_test(
            self, all_search: str, one_search: str, edge_name: str):
        """Full query search for graphql node.
        KeyArguments:
            all_search -- full query search,
            one_search -- one node query search,
            edge_name -- name of the edges eg. 'allInvestigators'
        """
        # Test acquisition of all the nodes
        data, status = self.run_query(all_search)
        assert status == 200
        full_results = data[edge_name]['edges']
        assert full_results
        # Test acquisition of one node
        one_result = choice(full_results)['node']['uuid']
        query = one_search.format(uuid=one_result)
        data, status = self.run_query(query)
        assert status == 200
        assert len(data[edge_name]['edges']) == 1

        return True

    def full_mutation_test(
            self, **kwargs):
        """Full mutation tests, generates a node, edits it, deletes it and
        checks its deletition.

        Arguments:
            create_query -- (str) query for the node creation.
            edit_query -- (str) query for the node edition.
            delete_query -- (str) query for the node deletition.
            one_query -- (str) query to retrieve one node.
            query_edge_name -- (str) name of edges eg allInvestigators.
            mutation_edge_name -- (str) name of edge mutation
            eg investigatorMutate.
            node_name -- (str) name of node eg investigator.
            edition_key -- (str) name of the edited key.
            value_key -- (str) value of the edition.
            extras -- (dict) extra values for query formatting
        """
        edge_name = kwargs['query_edge_name']
        node_name = kwargs['node_name']
        mutation_name = kwargs['mutation_edge_name']
        data, status = self.run_query(kwargs['create_query'].format(
            **kwargs['extras']))
        assert status == 200
        node_uuid = data[mutation_name][node_name]['uuid']
        # Update node
        data, status = self.run_query(kwargs['edit_query'].format(
            uuid=node_uuid, **kwargs['extras']))
        assert status == 200
        node = data[kwargs['mutation_edge_name']][node_name]
        assert node[kwargs['edition_key']] == kwargs['value_key']
        # Clean the db from the generated test node
        data, status = self.run_query(kwargs['delete_query'].format(
            uuid=node_uuid, **kwargs['extras']))
        assert status == 200
        # Make sure the node no longer exists
        data, status = self.run_query(kwargs['one_query'].format(
            uuid=node_uuid))
        assert status == 200
        assert not data[edge_name]['edges']

        return True
