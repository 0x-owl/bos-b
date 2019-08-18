"""
This tests must be run having an instance of the django server running,
either locally or remotely for them to work.
"""
from json import loads

from creator.tests.graphql.queries import all_investigators
from creator.tests.graphql.constants import GraphTest


class TestInvestigatorQuery(GraphTest):
    """Test class that encapsulates all investigator graphql query tests."""
    def test_investigators_full_node(self):
        response = self.SESS.post(
            self.GRAPHQL_URL,
            json={
                'query': all_investigators
            },
            headers=self.HEADERS
        )
        data = response.json()
        assert response.status_code == 200
        assert len(data['data']['allInvestigators']['edges'])

