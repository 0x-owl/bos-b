from market.tests.queries import (all_content, all_content_invs,
                                  all_content_items, all_content_spells,
                                  all_content_tags, create_content,
                                  create_content_inv, create_content_item,
                                  create_content_spell, create_content_tag,
                                  delete_content, delete_content_inv,
                                  delete_content_item, delete_content_spell,
                                  delete_content_tag, edit_content,
                                  edit_content_inv, edit_content_item,
                                  edit_content_spell, edit_content_tag,
                                  one_content, one_content_inv,
                                  one_content_item, one_content_spell,
                                  one_content_tag)

from creator.tests.graphql.queries import (create_investigator, create_item,
                                           create_mania, create_phobia,
                                           create_spell, create_tag,
                                           create_weapon, delete_investigator,
                                           delete_item, delete_mania,
                                           delete_phobia, delete_spell,
                                           delete_tag, delete_weapon)
from creator.tests.graphql.constants import GraphTest


class TestContentQuery(GraphTest):
    """Test class that encapsulates all content graphql query tests."""
    def test_content_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = data['contentMutate']['content']['uuid']
        assert self.full_research_test(
            all_content, one_content, 'allContents'
        )
        # clean up
        self.run_query(delete_content.format(uuid=content_uuid))

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
            value_key='test',
            extras={}
        )
        assert test_result


class TestContentTagQuery(GraphTest):
    """Test class that encapsulates all content tag graphql query tests."""
    def test_content_tag_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        # Build content and content tag to be looked for
        data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = data['contentMutate']['content']['uuid']
        tag_data, status = self.run_query(create_tag.format())
        tag_uuid = tag_data['tagMutate']['tag']['uuid']

        contag, status = self.run_query(query=create_content_tag.format(
            content_uuid=content_uuid,
            tag_uuid=tag_uuid
        ))
        assert status == 200
        content_tag_uuid = contag['contentTagMutate']['contentTag']['uuid']

        assert self.full_research_test(
            all_content_tags, one_content_tag, 'allContentTags'
        )

        # clean up auxiliar entities
        self.run_query(delete_content_tag.format(
            uuid=content_tag_uuid,
            content_uuid=content_uuid,
            tag_uuid=tag_uuid
        ))
        self.run_query(delete_content.format(uuid=content_uuid))
        self.run_query(delete_tag.format(uuid=tag_uuid))

    def test_content_tags_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        content_data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = content_data['contentMutate']['content']['uuid']

        first_tag_data, status = self.run_query(create_tag.format())
        assert status == 200
        tag_uuid = first_tag_data['tagMutate']['tag']['uuid']

        second_tag_data, status = self.run_query(create_tag.format())
        assert status == 200
        tag_uuid2 = second_tag_data['tagMutate']['tag']['uuid']

        test_result = self.full_mutation_test(
            create_query=create_content_tag,
            edit_query=edit_content_tag,
            delete_query=delete_content_tag,
            one_query=one_content_tag,
            query_edge_name='allContentTags',
            mutation_edge_name='contentTagMutate',
            node_name='contentTag',
            edition_key='tag',
            value_key={'uuid': tag_uuid2},
            extras={
                'content_uuid': content_uuid,
                'tag_uuid': tag_uuid,
                'tag_uuid_2': tag_uuid2
            }
        )

        # clean up of auxiliar entities
        self.run_query(delete_tag.format(uuid=tag_uuid))
        self.run_query(delete_tag.format(uuid=tag_uuid2))
        self.run_query(delete_content.format(uuid=content_uuid))

        assert test_result


class TestContentInvQuery(GraphTest):
    """Test class that encapsulates all content investigator graphql query
    tests."""
    def test_content_inv_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        # Build content and content tag to be looked for
        data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = data['contentMutate']['content']['uuid']
        inv_data, status = self.run_query(create_investigator.format())
        inv_uuid = inv_data['investigatorMutate']['investigator']['uuid']
        coninv, status = self.run_query(query=create_content_inv.format(
            content_uuid=content_uuid,
            inv_uuid=inv_uuid
        ))
        assert status == 200
        content_inv_uuid = coninv['contentInvestigatorMutate'][
            'contentInv']['uuid']

        assert self.full_research_test(
            all_content_invs, one_content_inv, 'allContentInvestigators'
        )

        # clean up auxiliar entities
        self.run_query(delete_content_inv.format(
            uuid=content_inv_uuid,
            content_uuid=content_uuid,
            inv_uuid=inv_uuid
        ))
        self.run_query(delete_content.format(uuid=content_uuid))
        self.run_query(delete_investigator.format(uuid=inv_uuid))


class TestContentItemQuery(GraphTest):
    """Test class that encapsulates all content items graphql query tests."""
    def test_content_item_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        # Build content and content tag to be looked for
        data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = data['contentMutate']['content']['uuid']
        item_data, status = self.run_query(create_item.format())
        item_uuid = item_data['itemMutate']['item']['uuid']
        con_item, status = self.run_query(query=create_content_item.format(
            content_uuid=content_uuid,
            item_uuid=item_uuid
        ))
        assert status == 200
        content_item_uuid = con_item['contentItemMutate'][
            'contentItem']['uuid']

        assert self.full_research_test(
            all_content_items, one_content_item, 'allContentItems'
        )

        # clean up auxiliar entities
        self.run_query(delete_content_item.format(
            uuid=content_item_uuid,
            content_uuid=content_uuid,
            item_uuid=item_uuid
        ))
        self.run_query(delete_content.format(uuid=content_uuid))
        self.run_query(delete_item.format(uuid=item_uuid))


class TestContentSpellQuery(GraphTest):
    """Test class that encapsulates all content spell graphql query tests."""
    def test_content_item_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        # Build content and content tag to be looked for
        data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = data['contentMutate']['content']['uuid']
        spell_data, status = self.run_query(create_spell.format())
        spell_uuid = spell_data['spellMutate']['spell']['uuid']
        con_item, status = self.run_query(query=create_content_spell.format(
            content_uuid=content_uuid,
            spell_uuid=spell_uuid
        ))
        assert status == 200
        content_spell_uuid = con_item['contentSpellMutate'][
            'contentSpell']['uuid']

        assert self.full_research_test(
            all_content_spells, one_content_spell, 'allContentSpells'
        )

        # clean up auxiliar entities
        self.run_query(delete_content_spell.format(
            uuid=content_spell_uuid,
            content_uuid=content_uuid,
            spell_uuid=spell_uuid
        ))
        self.run_query(delete_content.format(uuid=content_uuid))
        self.run_query(delete_spell.format(uuid=spell_uuid))
