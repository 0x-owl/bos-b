"""
This tests must be run having an instance of the django server running and a seeded database,
either locally or remotely for them to work.
"""
from json import loads
from random import choice

from creator.tests.graphql.queries import (all_investigators, all_tags,
                                           create_investigator, create_tag,
                                           delete_investigator, delete_tag,
                                           edit_investigator, edit_tag,
                                           one_investigator, one_tag)
from creator.tests.graphql.constants import GraphTest


class TestInvestigatorQuery(GraphTest):
    """Test class that encapsulates all investigator graphql query tests."""
    def test_investigators_query_node(self):
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
        query = one_investigator.format(uuid=investigator)
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
        data, status = self.run_query(one_investigator.format(uuid=inv_uuid))
        assert status == 200
        assert not data['allInvestigators']['edges']


class TestTagQuery(GraphTest):
    """Test class that encapsulates all tag graphql query tests."""
    def test_tag_query_node(self):
        """Test acquisitions of a full list of tags or by a single
        uuid.
        """
        # Test acquisition of all the tags
        data, status = self.run_query(all_tags)
        assert status == 200
        tags = data['allTags']['edges']
        assert tags
        # Test acquisition of one tag
        tag = choice(tags)['node']['uuid']
        query = one_tag.format(uuid=tag)
        data, status = self.run_query(query)
        assert status == 200
        assert len(data['allTags']['edges']) == 1

    def test_tag_full_mutation(self):
        """This tests creates, updates and finally deletes tags through the
        graphql queries.
        """
        # Create tag
        data, status = self.run_query(create_tag)
        assert status == 200
        tag_uuid = data['tagMutate']['tag']['uuid']
        # Update tag
        data, status = self.run_query(edit_tag.format(uuid=tag_uuid))
        assert status == 200
        tag = data['tagMutate']['tag']
        assert tag['title'] == 'test-tag2'
        # Clean the db from the generated test investigators
        data, status = self.run_query(delete_tag.format(
            uuid=tag_uuid))
        assert status == 200
        # Make sure the investigator no longer exists
        data, status = self.run_query(one_tag.format(uuid=tag_uuid))
        assert status == 200
        assert not data['allTags']['edges']
