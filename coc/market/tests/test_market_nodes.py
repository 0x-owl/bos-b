from market.tests.queries import (all_content, all_content_invs,
                                  all_content_items, all_content_manias,
                                  all_content_phobias, all_content_spells,
                                  all_content_tags, all_content_weapons,
                                  create_content, create_content_inv,
                                  create_content_item, create_content_mania,
                                  create_content_phobia, create_content_spell,
                                  create_content_tag, create_content_weapon,
                                  delete_content, delete_content_inv,
                                  delete_content_item, delete_content_mania,
                                  delete_content_phobia, delete_content_spell,
                                  delete_content_tag, delete_content_weapon,
                                  edit_content, edit_content_inv,
                                  edit_content_item, edit_content_mania,
                                  edit_content_phobia, edit_content_spell,
                                  edit_content_tag, edit_content_weapon,
                                  one_content, one_content_inv,
                                  one_content_item, one_content_mania,
                                  one_content_phobia, one_content_spell,
                                  one_content_tag, one_content_weapon)

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
        content_uuid = self.create_and_obtain_uuid(create_content, 'content')
        assert self.full_research_test(
            all_content, one_content, 'allContents'
        )
        # clean up
        self.delete_instance(delete_content, {'uuid': content_uuid})

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
        res = self.batch_instance_builder({
            'content': {'query': create_content},
            'tag': {'query': create_tag},
        })
        content_uuid = res['content']
        tag_uuid = res['tag']
        content_tag_uuid = self.create_and_obtain_uuid(
            query=create_content_tag,
            model_name='contentTag',
            uuids={'content_uuid': content_uuid, 'tag_uuid': tag_uuid}
        )
        assert self.full_research_test(
            all_content_tags, one_content_tag, 'allContentTags'
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_content_tag, {
                'uuid': content_tag_uuid,
                'content_uuid': content_uuid,
                'tag_uuid': tag_uuid
                }),
            (delete_content, {'uuid': content_uuid}),
            (delete_tag, {'uuid': tag_uuid})
        ])

    def test_content_tags_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        res = self.batch_instance_builder({
            'content': {'query': create_content},
            'tag': {'query': create_tag},
            'tag2': {'query': create_tag, 'alt_name': 'tag'}
        })
        content_uuid = res['content']
        tag_uuid = res['tag']
        tag_uuid2 = res['tag2']

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
        self.batch_instance_cleaner([
            (delete_tag, {'uuid': tag_uuid}),
            (delete_tag, {'uuid': tag_uuid2}),
            (delete_content, {'uuid': content_uuid})
        ])
        assert test_result


class TestContentInvQuery(GraphTest):
    """Test class that encapsulates all content investigator graphql query
    tests."""
    def test_content_inv_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'content': {'query': create_content},
            'investigator': {'query': create_investigator},
        })
        content_uuid = res['content']
        investigator_uuid = res['investigator']
        content_inv_uuid = self.create_and_obtain_uuid(
            query=create_content_inv,
            model_name='contentInv',
            uuids={'content_uuid': content_uuid, 'inv_uuid': investigator_uuid}
        )

        assert self.full_research_test(
            all_content_invs, one_content_inv, 'allContentInvestigators'
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_content_inv, {
                'uuid': content_inv_uuid,
                'content_uuid': content_uuid,
                'inv_uuid': investigator_uuid
                }),
            (delete_content, {'uuid': content_uuid}),
            (delete_investigator, {'uuid': investigator_uuid})
        ])

    def test_content_inv_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        res = self.batch_instance_builder({
            'content': {'query': create_content},
            'investigator': {'query': create_investigator},
            'investigator2': {
                'query': create_investigator,
                'alt_name': 'investigator'}
        })
        content_uuid = res['content']
        inv_uuid = res['investigator']
        inv_uuid2 = res['investigator2']

        test_result = self.full_mutation_test(
            create_query=create_content_inv,
            edit_query=edit_content_inv,
            delete_query=delete_content_inv,
            one_query=one_content_inv,
            query_edge_name='allContentInvestigators',
            mutation_edge_name='contentInvMutate',
            node_name='contentInv',
            edition_key='inv',
            value_key={'uuid': inv_uuid2},
            extras={
                'content_uuid': content_uuid,
                'inv_uuid': inv_uuid,
                'inv_uuid_2': inv_uuid2
            }
        )

        # clean up of auxiliar entities
        self.batch_instance_cleaner([
            (delete_investigator, {'uuid': inv_uuid}),
            (delete_investigator, {'uuid': inv_uuid2}),
            (delete_content, {'uuid': content_uuid})
        ])
        assert test_result


class TestContentItemQuery(GraphTest):
    """Test class that encapsulates all content items graphql query tests."""
    def test_content_item_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'content': {'query': create_content},
            'item': {'query': create_item},
        })
        content_uuid = res['content']
        item_uuid = res['item']
        content_item_uuid = self.create_and_obtain_uuid(
            query=create_content_item,
            model_name='contentItem',
            uuids={'content_uuid': content_uuid, 'item_uuid': item_uuid}
        )
        assert self.full_research_test(
            all_content_items, one_content_item, 'allContentItems'
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_content_item, {
                'uuid': content_item_uuid,
                'content_uuid': content_uuid,
                'item_uuid': item_uuid
            }),
            (delete_content, {'uuid': content_uuid}),
            (delete_item, {'uuid': item_uuid})
        ])

    def test_content_item_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        res = self.batch_instance_builder({
            'content': {'query': create_content},
            'item': {'query': create_item},
            'item2': {
                'query': create_item,
                'alt_name': 'item'}
        })
        content_uuid = res['content']
        item_uuid = res['item']
        item_uuid2 = res['item2']

        test_result = self.full_mutation_test(
            create_query=create_content_item,
            edit_query=edit_content_item,
            delete_query=delete_content_item,
            one_query=one_content_item,
            query_edge_name='allContentItems',
            mutation_edge_name='contentItemMutate',
            node_name='contentItem',
            edition_key='item',
            value_key={'uuid': item_uuid2},
            extras={
                'content_uuid': content_uuid,
                'item_uuid': item_uuid,
                'item_uuid_2': item_uuid2
            }
        )

        # clean up of auxiliar entities
        self.batch_instance_cleaner([
            (delete_item, {'uuid': item_uuid}),
            (delete_item, {'uuid': item_uuid2}),
            (delete_content, {'uuid': content_uuid})
        ])

        assert test_result


class TestContentSpellQuery(GraphTest):
    """Test class that encapsulates all content spell graphql query tests."""
    def test_content_spell_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'content': {'query': create_content},
            'spell': {'query': create_spell},
        })
        content_uuid = res['content']
        spell_uuid = res['spell']
        content_spell_uuid = self.create_and_obtain_uuid(
            query=create_content_spell,
            model_name='contentSpell',
            uuids={'content_uuid': content_uuid, 'spell_uuid': spell_uuid}
        )

        assert self.full_research_test(
            all_content_spells, one_content_spell, 'allContentSpells'
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_content_spell, {
                'uuid': content_spell_uuid,
                'content_uuid': content_uuid,
                'spell_uuid': spell_uuid
            }),
            (delete_content, {'uuid': content_uuid}),
            (delete_spell, {'uuid': spell_uuid})
        ])

    def test_content_spell_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        res = self.batch_instance_builder({
            'content': {'query': create_content},
            'spell': {'query': create_spell},
            'spell2': {
                'query': create_spell,
                'alt_name': 'spell'}
        })
        content_uuid = res['content']
        spell_uuid = res['spell']
        spell_uuid2 = res['spell2']

        test_result = self.full_mutation_test(
            create_query=create_content_spell,
            edit_query=edit_content_spell,
            delete_query=delete_content_spell,
            one_query=one_content_spell,
            query_edge_name='allContentSpells',
            mutation_edge_name='contentSpellMutate',
            node_name='contentSpell',
            edition_key='spell',
            value_key={'uuid': spell_uuid2},
            extras={
                'content_uuid': content_uuid,
                'spell_uuid': spell_uuid,
                'spell_uuid_2': spell_uuid2
            }
        )

        # clean up of auxiliar entities
        self.batch_instance_cleaner([
            (delete_spell, {'uuid': spell_uuid}),
            (delete_spell, {'uuid': spell_uuid2}),
            (delete_content, {'uuid': content_uuid})
        ])

        assert test_result


class TestContentWeaponQuery(GraphTest):
    """Test class that encapsulates all content weapon graphql query tests."""
    def test_content_weapon_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'content': {'query': create_content},
            'weapon': {'query': create_weapon},
        })
        content_uuid = res['content']
        weapon_uuid = res['weapon']
        content_weapon_uuid = self.create_and_obtain_uuid(
            query=create_content_weapon,
            model_name='contentWeapon',
            uuids={'content_uuid': content_uuid, 'weapon_uuid': weapon_uuid}
        )

        assert self.full_research_test(
            all_content_weapons, one_content_weapon, 'allContentWeapons'
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_content_weapon, {
                'uuid': content_weapon_uuid,
                'content_uuid': content_uuid,
                'weapon_uuid': weapon_uuid
            }),
            (delete_content, {'uuid': content_uuid}),
            (delete_weapon, {'uuid': weapon_uuid})
        ])

    def test_content_weapon_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        res = self.batch_instance_builder({
            'content': {'query': create_content},
            'weapon': {'query': create_weapon},
            'weapon2': {
                'query': create_weapon,
                'alt_name': 'weapon'}
        })
        content_uuid = res['content']
        weapon_uuid = res['weapon']
        weapon_uuid2 = res['weapon2']

        test_result = self.full_mutation_test(
            create_query=create_content_weapon,
            edit_query=edit_content_weapon,
            delete_query=delete_content_weapon,
            one_query=one_content_weapon,
            query_edge_name='allContentWeapons',
            mutation_edge_name='contentWeaponMutate',
            node_name='contentWeapon',
            edition_key='weapon',
            value_key={'uuid': weapon_uuid2},
            extras={
                'content_uuid': content_uuid,
                'weapon_uuid': weapon_uuid,
                'weapon_uuid_2': weapon_uuid2
            }
        )

        # clean up of auxiliar entities
        self.batch_instance_cleaner([
            (delete_weapon, {'uuid': weapon_uuid}),
            (delete_weapon, {'uuid': weapon_uuid2}),
            (delete_content, {'uuid': content_uuid})
        ])
        assert test_result


class TestContentManiaQuery(GraphTest):
    """Test class that encapsulates all content mania graphql query tests."""
    def test_content_mania_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'content': {'query': create_content},
            'mania': {'query': create_mania},
        })
        content_uuid = res['content']
        mania_uuid = res['mania']
        content_mania_uuid = self.create_and_obtain_uuid(
            query=create_content_mania,
            model_name='contentMania',
            uuids={'content_uuid': content_uuid, 'mania_uuid': mania_uuid}
        )

        assert self.full_research_test(
            all_content_manias, one_content_mania, 'allContentManias'
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_content_mania, {
                'uuid': content_mania_uuid,
                'content_uuid': content_uuid,
                'mania_uuid': mania_uuid
            }),
            (delete_content, {'uuid': content_uuid}),
            (delete_mania, {'uuid': mania_uuid})
        ])

    def test_content_mania_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        res = self.batch_instance_builder({
            'content': {'query': create_content},
            'mania': {'query': create_mania},
            'mania2': {
                'query': create_mania,
                'alt_name': 'mania'}
        })
        content_uuid = res['content']
        mania_uuid = res['mania']
        mania_uuid2 = res['mania2']

        test_result = self.full_mutation_test(
            create_query=create_content_mania,
            edit_query=edit_content_mania,
            delete_query=delete_content_mania,
            one_query=one_content_mania,
            query_edge_name='allContentManias',
            mutation_edge_name='contentManiaMutate',
            node_name='contentMania',
            edition_key='mania',
            value_key={'uuid': mania_uuid2},
            extras={
                'content_uuid': content_uuid,
                'mania_uuid': mania_uuid,
                'mania_uuid_2': mania_uuid2
            }
        )

        # clean up of auxiliar entities
        self.batch_instance_cleaner([
            (delete_mania, {'uuid': mania_uuid}),
            (delete_mania, {'uuid': mania_uuid2}),
            (delete_content, {'uuid': content_uuid})
        ])

        assert test_result


class TestContentPhobiaQuery(GraphTest):
    """Test class that encapsulates all content phobia graphql query tests."""
    def test_content_phobia_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'content': {'query': create_content},
            'phobia': {'query': create_phobia},
        })
        content_uuid = res['content']
        phobia_uuid = res['phobia']
        content_phobia_uuid = self.create_and_obtain_uuid(
            query=create_content_phobia,
            model_name='contentPhobia',
            uuids={'content_uuid': content_uuid, 'phobia_uuid': phobia_uuid}
        )

        assert self.full_research_test(
            all_content_phobias, one_content_phobia, 'allContentPhobias'
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_content_phobia, {
                'uuid': content_phobia_uuid,
                'content_uuid': content_uuid,
                'phobia_uuid': phobia_uuid
            }),
            (delete_content, {'uuid': content_uuid}),
            (delete_phobia, {'uuid': phobia_uuid})
        ])

    def test_content_phobia_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        res = self.batch_instance_builder({
            'content': {'query': create_content},
            'phobia': {'query': create_phobia},
            'phobia2': {
                'query': create_phobia,
                'alt_name': 'phobia'}
        })
        content_uuid = res['content']
        phobia_uuid = res['phobia']
        phobia_uuid2 = res['phobia2']


        test_result = self.full_mutation_test(
            create_query=create_content_phobia,
            edit_query=edit_content_phobia,
            delete_query=delete_content_phobia,
            one_query=one_content_phobia,
            query_edge_name='allContentPhobias',
            mutation_edge_name='contentPhobiaMutate',
            node_name='contentPhobia',
            edition_key='phobia',
            value_key={'uuid': phobia_uuid2},
            extras={
                'content_uuid': content_uuid,
                'phobia_uuid': phobia_uuid,
                'phobia_uuid_2': phobia_uuid2
            }
        )

        # clean up of auxiliar entities
        self.batch_instance_cleaner([
            (delete_phobia, {'uuid': phobia_uuid}),
            (delete_phobia, {'uuid': phobia_uuid2}),
            (delete_content, {'uuid': content_uuid})
        ])

        assert test_result
