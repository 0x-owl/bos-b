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
        content_inv_uuid = coninv['contentInvMutate']['contentInv']['uuid']

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

    def test_content_inv_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        content_data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = content_data['contentMutate']['content']['uuid']

        first_inv_data, status = self.run_query(create_investigator.format())
        assert status == 200
        inv_uuid = first_inv_data['investigatorMutate']['investigator']['uuid']

        second_inv_data, status = self.run_query(create_investigator.format())
        assert status == 200
        inv_uuid2 = second_inv_data['investigatorMutate'][
            'investigator']['uuid']

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
        self.run_query(delete_investigator.format(uuid=inv_uuid))
        self.run_query(delete_investigator.format(uuid=inv_uuid2))
        self.run_query(delete_content.format(uuid=content_uuid))

        assert test_result


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

    def test_content_item_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        content_data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = content_data['contentMutate']['content']['uuid']

        first_item_data, status = self.run_query(create_item.format())
        assert status == 200
        item_uuid = first_item_data['itemMutate']['item']['uuid']

        second_item_data, status = self.run_query(create_item.format())
        assert status == 200
        item_uuid2 = second_item_data['itemMutate']['item']['uuid']

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
        self.run_query(delete_item.format(uuid=item_uuid))
        self.run_query(delete_item.format(uuid=item_uuid2))
        self.run_query(delete_content.format(uuid=content_uuid))

        assert test_result


class TestContentSpellQuery(GraphTest):
    """Test class that encapsulates all content spell graphql query tests."""
    def test_content_spell_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        # Build content and content tag to be looked for
        data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = data['contentMutate']['content']['uuid']
        spell_data, status = self.run_query(create_spell.format())
        spell_uuid = spell_data['spellMutate']['spell']['uuid']
        con_spell, status = self.run_query(query=create_content_spell.format(
            content_uuid=content_uuid,
            spell_uuid=spell_uuid
        ))
        assert status == 200
        content_spell_uuid = con_spell['contentSpellMutate'][
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

    def test_content_spell_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        content_data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = content_data['contentMutate']['content']['uuid']

        first_spell_data, status = self.run_query(create_spell.format())
        assert status == 200
        spell_uuid = first_spell_data['spellMutate']['spell']['uuid']

        second_spell_data, status = self.run_query(create_spell.format())
        assert status == 200
        spell_uuid2 = second_spell_data['spellMutate']['spell']['uuid']

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
        self.run_query(delete_spell.format(uuid=spell_uuid))
        self.run_query(delete_spell.format(uuid=spell_uuid2))
        self.run_query(delete_content.format(uuid=content_uuid))

        assert test_result


class TestContentWeaponQuery(GraphTest):
    """Test class that encapsulates all content weapon graphql query tests."""
    def test_content_weapon_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        # Build content and content tag to be looked for
        data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = data['contentMutate']['content']['uuid']
        weapon_data, status = self.run_query(create_weapon.format())
        weapon_uuid = weapon_data['weaponMutate']['weapon']['uuid']
        con_weapon, status = self.run_query(query=create_content_weapon.format(
            content_uuid=content_uuid,
            weapon_uuid=weapon_uuid
        ))
        assert status == 200
        content_weapon_uuid = con_weapon['contentWeaponMutate'][
            'contentWeapon']['uuid']

        assert self.full_research_test(
            all_content_weapons, one_content_weapon, 'allContentWeapons'
        )

        # clean up auxiliar entities
        self.run_query(delete_content_weapon.format(
            uuid=content_weapon_uuid,
            content_uuid=content_uuid,
            weapon_uuid=weapon_uuid
        ))
        self.run_query(delete_content.format(uuid=content_uuid))
        self.run_query(delete_weapon.format(uuid=weapon_uuid))

    def test_content_weapon_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        content_data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = content_data['contentMutate']['content']['uuid']

        first_weapon_data, status = self.run_query(create_weapon.format())
        assert status == 200
        weapon_uuid = first_weapon_data['weaponMutate']['weapon']['uuid']

        second_weapon_data, status = self.run_query(create_weapon.format())
        assert status == 200
        weapon_uuid2 = second_weapon_data['weaponMutate']['weapon']['uuid']

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
        self.run_query(delete_weapon.format(uuid=weapon_uuid))
        self.run_query(delete_weapon.format(uuid=weapon_uuid2))
        self.run_query(delete_content.format(uuid=content_uuid))

        assert test_result


class TestContentManiaQuery(GraphTest):
    """Test class that encapsulates all content mania graphql query tests."""
    def test_content_mania_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        # Build content and content tag to be looked for
        data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = data['contentMutate']['content']['uuid']
        mania_data, status = self.run_query(create_mania.format())
        mania_uuid = mania_data['maniaMutate']['mania']['uuid']
        con_mania, status = self.run_query(query=create_content_mania.format(
            content_uuid=content_uuid,
            mania_uuid=mania_uuid
        ))
        assert status == 200
        content_mania_uuid = con_mania['contentManiaMutate'][
            'contentMania']['uuid']

        assert self.full_research_test(
            all_content_manias, one_content_mania, 'allContentManias'
        )

        # clean up auxiliar entities
        self.run_query(delete_content_mania.format(
            uuid=content_mania_uuid,
            content_uuid=content_uuid,
            mania_uuid=mania_uuid
        ))
        self.run_query(delete_content.format(uuid=content_uuid))
        self.run_query(delete_mania.format(uuid=mania_uuid))

    def test_content_mania_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        content_data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = content_data['contentMutate']['content']['uuid']

        first_mania_data, status = self.run_query(create_mania.format())
        assert status == 200
        mania_uuid = first_mania_data['maniaMutate']['mania']['uuid']

        second_mania_data, status = self.run_query(create_mania.format())
        assert status == 200
        mania_uuid2 = second_mania_data['maniaMutate']['mania']['uuid']

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
        self.run_query(delete_mania.format(uuid=mania_uuid))
        self.run_query(delete_mania.format(uuid=mania_uuid2))
        self.run_query(delete_content.format(uuid=content_uuid))

        assert test_result


class TestContentPhobiaQuery(GraphTest):
    """Test class that encapsulates all content phobia graphql query tests."""
    def test_content_phobia_query_node(self):
        """Test acquisitions of a full list of contents or by a single uuid."""
        # Build content and content tag to be looked for
        data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = data['contentMutate']['content']['uuid']
        phobia_data, status = self.run_query(create_phobia.format())
        phobia_uuid = phobia_data['phobiaMutate']['phobia']['uuid']
        con_phobia, status = self.run_query(query=create_content_phobia.format(
            content_uuid=content_uuid,
            phobia_uuid=phobia_uuid
        ))
        assert status == 200
        content_phobia_uuid = con_phobia['contentPhobiaMutate'][
            'contentPhobia']['uuid']

        assert self.full_research_test(
            all_content_phobias, one_content_phobia, 'allContentPhobias'
        )

        # clean up auxiliar entities
        self.run_query(delete_content_phobia.format(
            uuid=content_phobia_uuid,
            content_uuid=content_uuid,
            phobia_uuid=phobia_uuid
        ))
        self.run_query(delete_content.format(uuid=content_uuid))
        self.run_query(delete_phobia.format(uuid=phobia_uuid))

    def test_content_phobia_full_mutation(self):
        """This test creates, updates and finally deletes a content through the
        grapql queries.
        """
        content_data, status = self.run_query(query=create_content.format())
        assert status == 200
        content_uuid = content_data['contentMutate']['content']['uuid']

        first_phobia_data, status = self.run_query(create_phobia.format())
        assert status == 200
        phobia_uuid = first_phobia_data['phobiaMutate']['phobia']['uuid']

        second_phobia_data, status = self.run_query(create_phobia.format())
        assert status == 200
        phobia_uuid2 = second_phobia_data['phobiaMutate']['phobia']['uuid']

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
        self.run_query(delete_phobia.format(uuid=phobia_uuid))
        self.run_query(delete_phobia.format(uuid=phobia_uuid2))
        self.run_query(delete_content.format(uuid=content_uuid))

        assert test_result
