"""
This tests must be run having an instance of the django server running
and a seeded database, either locally or remotely for them to work.
"""
from random import choice

from creator.tests.graphql.queries import (all_investigators, all_items,
                                           all_occ, all_skills, all_spells,
                                           all_tags, create_investigator,
                                           create_item, create_occ,
                                           create_skill, create_spell,
                                           create_tag, delete_investigator,
                                           delete_item, delete_occ,
                                           delete_skill, delete_spell,
                                           delete_tag, edit_investigator,
                                           edit_item, edit_occ, edit_skill,
                                           edit_spell, edit_tag,
                                           one_investigator, one_item, one_occ,
                                           one_skill, one_spell, one_tag)
from creator.tests.graphql.constants import GraphTest


class TestInvestigatorQuery(GraphTest):
    """Test class that encapsulates all investigator graphql query tests."""
    def test_investigators_query_node(self):
        """Test acquisitions of a full list of investigators or by a single
        uuid.
        """
        assert self.full_research_test(
            all_investigators, one_investigator, 'allInvestigators')

    def test_investigators_full_mutation(self):
        """This tests creates, updates and finally deletes an investigator
        through the graphql queries.
        """
        test_result = self.full_mutation_test(
            create_query=create_investigator,
            edit_query=edit_investigator,
            delete_query=delete_investigator,
            one_query=one_investigator,
            query_edge_name="allInvestigators",
            mutation_edge_name="investigatorMutate",
            node_name="investigator",
            edition_key="player",
            value_key="TestUpdate",
            extras={}
        )
        assert test_result


class TestSkillQuery(GraphTest):
    """Test class that encapsulates all skillsa graphql query tests."""
    def test_skills_query_node(self):
        """Test acquisitions of a full list of skills or by a single
        uuid.
        """
        assert self.full_research_test(
            all_skills, one_skill, "allSkills"
        )

    def test_skills_full_mutation(self):
        """This tests creates, updates and finally deletes an skill
        through the graphql queries.
        """
        assert self.full_mutation_test(
            create_query=create_skill,
            edit_query=edit_skill,
            delete_query=delete_skill,
            one_query=one_skill,
            query_edge_name="allSkills",
            mutation_edge_name="skillMutate",
            node_name="skill",
            edition_key="title",
            value_key="Test-2",
            extras={}
        )


class TestTagQuery(GraphTest):
    """Test class that encapsulates all tag graphql query tests."""
    def test_tag_query_node(self):
        """Test acquisitions of a full list of tags or by a single
        uuid.
        """
        assert self.full_research_test(
            all_tags, one_tag, 'allTags'
        )

    def test_tag_full_mutation(self):
        """This tests creates, updates and finally deletes tags through the
        graphql queries.
        """
        assert self.full_mutation_test(
            create_query=create_tag,
            edit_query=edit_tag,
            delete_query=delete_tag,
            one_query=one_tag,
            query_edge_name="allTags",
            mutation_edge_name="tagMutate",
            node_name="tag",
            edition_key="title",
            value_key="test-tag2",
            extras={}
        )


class TestItemQuery(GraphTest):
    """Test class that encapsulates all items graphql query tests."""
    def test_items_query_node(self):
        """Test acquisitions of a full list of items or by a single uuid.
        """
        assert self.full_research_test(
            all_items, one_item, 'allItems'
        )

    def test_items_full_mutation(self):
        """This tests creates, updates and finally deletes an item
        through the graphql queries.
        """
        assert self.full_mutation_test(
            create_query=create_item,
            edit_query=edit_item,
            delete_query=delete_item,
            one_query=one_item,
            query_edge_name="allItems",
            mutation_edge_name="itemMutate",
            node_name="item",
            edition_key="description",
            value_key="TestUpdate",
            extras={}
        )


class TestSpellQuery(GraphTest):
    """Test class that encapsulates all spells graphql query tests."""
    def test_spell_query_node(self):
        """Test acquisitions of a full list of spell or by a single uuid.
        """
        assert self.full_research_test(
            all_spells, one_spell, 'allSpells'
        )

    def test_spells_full_mutation(self):
        """This tests creates, updates and finally deletes a spell
        through the graphql queries.
        """
        assert self.full_mutation_test(
            create_query=create_spell,
            edit_query=edit_spell,
            delete_query=delete_spell,
            one_query=one_spell,
            query_edge_name="allSpells",
            mutation_edge_name="spellMutate",
            node_name="spell",
            edition_key="notes",
            value_key="test",
            extras={}
        )


class TestOccupationQuery(GraphTest):
    """Test class that encapsulates all occupation graphql query tests."""
    def test_occupations_query_node(self):
        """Test acquisitions of a full list of occupations or by a single uuid.
        """
        assert self.full_research_test(
            all_occ, one_occ, 'allOccupations'
        )

    def test_occupations_full_mutation(self):
        """This tests creates, updates and finally deletes a occupation
        through the graphql queries.
        """
        assert self.full_mutation_test(
            create_query=create_occ,
            edit_query=edit_occ,
            delete_query=delete_occ,
            one_query=one_occ,
            query_edge_name="allOccupations",
            mutation_edge_name="occupationMutate",
            node_name="occupation",
            edition_key="title",
            value_key="Test-2",
            extras={}
        )
