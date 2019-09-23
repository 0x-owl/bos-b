from market.tests.queries import (all_content, create_content, delete_content,
                                  edit_content, one_content)
from creator.tests.graphql.constants import GraphTest


class TestContentQuery(GraphTest):
    """Test class that encapsulates all content graphql query tests."""
    def test_content_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        assert self.full_research_test(
            all_content, one_content, 'allContents'
        )

    def test_contents_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        test_result = self.full_mutation_test(
            create_query=create_content,
            edit_query=edit_content,
            delete_query=delete_content,
            one_query=one_content,
            query_edge_name='allContents',
            mutation_edge_name='contentMutate',
            node_name='content',
            edition_key='description',
            value_key='test'
        )
        assert test_result
