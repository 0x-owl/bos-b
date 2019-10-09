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

    def create_and_obtain_uuid(
            self, query: str, model_name: str, mutation=None, uuids={}):
        """Returns the uuid of a created entity.
        Arguments:
            query -- (str) creation_query
            model_name -- (str) name of entity e.g tag
            mutation_name -- (str-optional) overrides the default name.
        """
        default_mutation = f'{model_name}Mutate'
        data, status = self.run_query(query=query.format(**uuids))
        assert status == 200, f"Couldn't create instance query:\n {query}"
        mutation_name = mutation if mutation is not None else default_mutation
        uuid = data[mutation_name][model_name]['uuid']
        return uuid

    def delete_instance(self, query: str, uuids: dict):
        """Given the deletetion query and a uuid, erase an entity.
        Arguments:
            query -- deletition query.
            uuids -- uuids required to delete the instance.
        """
        data, status = self.run_query(query.format(**uuids))
        return status == 200, data

    def batch_instance_builder(self, models):
        """Method that creates the entities required by a intermediate model.
        Returns its uuids
        Arguments:
            models -- dictionary with each key being the model name and holds
            the creation query and the variable name.
            e.g:
                {'modelx2': {
                    'query': query,
                    'mutation_name': mutation,
                    'alt_name': 'modelx',
                    'uuids': {'content_uuid': auuid}
                    }
                }
                mutation_name in case it differs from default value
                alt_name in case we need to generate two of the same kind.
                uuids in case we need uuids for intermediate entities.
        """
        results = {}
        for model in models:
            alt_name = models[model].get('alt_name', None)
            model_name = alt_name if alt_name is not None else model
            query = models[model]['query']
            mutation_name = models[model].get('mutation_name', None)
            uuid = self.create_and_obtain_uuid(
                query,
                model_name,
                mutation_name,
                models[model].get('uuids', {})
            )
            results[model] = uuid
        return results

    def batch_instance_cleaner(self, targets: list):
        """Method that deletes many objects at once.
        Arguments:
            targets -- list of tuples that hold the query on the first
            index and dict of parameters on the second.
            e.g [(delete_content, {uuid:content_uuid}),
                 (delete_tag, {uuid: tag_uuid})]
        """
        deleted_list = []
        for target in targets:
            success, deleted = self.delete_instance(target[0], target[1])
            assert success, f"Couldn't delete instance {target}"
            deleted_list.append(deleted)
        return deleted_list
