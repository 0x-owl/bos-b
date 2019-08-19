"""
This tests must be run having an instance of the django server running and a seeded database,
either locally or remotely for them to work.
"""
from json import loads
from random import choice

from creator.tests.graphql.queries import (all_investigators,
                                           create_investigator,
                                           delete_investigator,
                                           edit_investigator, one_investigator)
from creator.tests.graphql.constants import GraphTest


class TestInvestigatorQuery(GraphTest):
    """Test class that encapsulates all investigator graphql query tests."""
    def test_investigators_full_node(self):
        """Test acquisitions of a full list of investigators or by a single
        uuid.
        """
        # Test acquisition of all the investigators
        data, status = self.run_query(all_investigators)
        assert status == 200
        investigators = data['allInvestigators']['edges']
        assert investigators
        # Test acquisition of one investigator
        investigator = choice(investigators)['node']['uuid']
        query = one_investigator.format(investigator=investigator)
        data, status = self.run_query(query)
        assert status == 200
        assert len(data['allInvestigators']['edges']) == 1

    def test_investigators_full_mutation(self):
        """This tests creates, updates and finally deletes an investigator
        through the graphql queries.
        """
        # Create investigator
        data, status = self.run_query(create_investigator)
        assert status == 200
        inv_uuid = data['investigatorMutate']['investigator']['uuid']

        # Update investigator
        data, status = self.run_query(edit_investigator.format(uuid=inv_uuid))
        assert status == 200
        investigator = data['investigatorMutate']['investigator']
        assert investigator['player'] == 'TestUpdate'
        # Clean the db from the generated test investigators
        data, status = self.run_query(delete_investigator.format(
            uuid=inv_uuid))
        assert status == 200
        # Make sure the investigator no longer exists
        data, status = self.run_query(one_investigator.format(
            investigator=inv_uuid))
        assert status == 200
        assert not data['allInvestigators']['edges']
