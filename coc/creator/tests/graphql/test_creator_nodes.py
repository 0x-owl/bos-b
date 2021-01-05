"""
This tests must be run having an instance of the django server running
and a seeded database, either locally or remotely for them to work.
"""
from random import choice

from creator.tests.graphql.queries import *

from creator.tests.graphql.constants import GraphTest


class TestInvestigatorQuery(GraphTest):
    """Test class that encapsulates all investigator graphql query tests."""
    def test_investigators_query_node(self):
        """Test acquisitions of a full list of investigators or by a single
        uuid.
        """
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'investigator': {'query': create_investigator}
        })
        investigator_uuid = res['investigator']

        assert self.full_research_test(
            all_investigators, one_investigator, 'allInvestigators')

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_investigator, {'uuid': investigator_uuid})
        ])

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
    """Test class that encapsulates all skills graphql query tests."""
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
            edition_key="subSkills-Test Skill-title",
            value_key="test_skill2",
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
            edition_key="properties-description",
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


class TestManiaQuery(GraphTest):
    """Test class that encapsulates all manias graphql query tests."""
    def test_manias_query_node(self):
        """Test acquisitions of a full list of manias or by a single uuid.
        """
        assert self.full_research_test(
            all_manias, one_mania, 'allManias'
        )

    def test_manias_full_mutation(self):
        """This tests creates, updates and finally deletes a mania
        through the graphql queries.
        """
        assert self.full_mutation_test(
            create_query=create_mania,
            edit_query=edit_mania,
            delete_query=delete_mania,
            one_query=one_mania,
            query_edge_name="allManias",
            mutation_edge_name="maniaMutate",
            node_name="mania",
            edition_key="title",
            value_key="test-mania2",
            extras={}
        )


class TestPhobiaQuery(GraphTest):
    """Test class that encapsulates all phobias graphql query tests."""
    def test_phobias_query_node(self):
        """Test acquisitions of a full list of phobias or by a single uuid.
        """
        assert self.full_research_test(
            all_phobias, one_phobia, 'allPhobias'
        )

    def test_phobias_full_mutation(self):
        """This tests creates, updates and finally deletes a phobia
        through the graphql queries.
        """
        assert self.full_mutation_test(
            create_query=create_phobia,
            edit_query=edit_phobia,
            delete_query=delete_phobia,
            one_query=one_phobia,
            query_edge_name="allPhobias",
            mutation_edge_name="phobiaMutate",
            node_name="phobia",
            edition_key="title",
            value_key="test-phobia2",
            extras={}
        )


class TestPhobiaInvQuery(GraphTest):
    """Test class that encapsulates all phobia-investigator graphql query
    tests.
    """
    def test_phobiasInv_query_node(self):
        """Test acquisitions of a full list of phobia-investigator or by a
        single uuid.
        """
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'investigator': {'query': create_investigator},
            'phobia': {'query': create_phobia}
        })
        investigator_uuid = res['investigator']
        phobia_uuid = res['phobia']
        phobia_inv_uuid = self.create_and_obtain_uuid(
            query=create_phobia_inv,
            model_name='phobiaInv',
            uuids={
                'investigator_uuid': investigator_uuid,
                'phobia_uuid': phobia_uuid
            }
        )

        assert self.full_research_test(
            all_phobias_inv, one_phobia_inv, 'allPhobiasInv'
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_investigator, {'uuid': investigator_uuid}),
            (delete_phobia, {'uuid': phobia_uuid}),
            (delete_phobia_inv, {'uuid': phobia_inv_uuid})
        ])


    def test_phobiasInv_full_mutation(self):
        """This tests creates, updates and finally deletes a
        phobia-investigator through the graphql queries.
        """
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'investigator': {'query': create_investigator},
            'phobia': {'query': create_phobia}
        })
        investigator_uuid = res['investigator']
        phobia_uuid = res['phobia']

        assert self.full_mutation_test(
            create_query=create_phobia_inv,
            edit_query=edit_phobia_inv,
            delete_query=delete_phobia_inv,
            one_query=one_phobia_inv,
            query_edge_name="allPhobiasInv",
            mutation_edge_name="phobiaInvMutate",
            node_name="phobiaInv",
            edition_key="duration",
            value_key=40,
            extras={
                "investigator_uuid": investigator_uuid,
                "phobia_uuid": phobia_uuid
            }
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_investigator, {'uuid': investigator_uuid}),
            (delete_phobia, {'uuid': phobia_uuid})
        ])


class TestManiaInvQuery(GraphTest):
    """Test class that encapsulates all mania-investigator graphql query tests.
    """
    def test_maniasInv_query_node(self):
        """Test acquisitions of a full list of mania-investigator or by a
        single uuid.
        """
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'investigator': {'query': create_investigator},
            'mania': {'query': create_mania}
        })
        investigator_uuid = res['investigator']
        mania_uuid = res['mania']
        mania_inv_uuid = self.create_and_obtain_uuid(
            query=create_mania_inv,
            model_name='maniaInv',
            uuids={
                'investigator_uuid': investigator_uuid,
                'mania_uuid': mania_uuid
            }
        )

        assert self.full_research_test(
            all_manias_inv, one_mania_inv, 'allManiasInv'
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_investigator, {'uuid': investigator_uuid}),
            (delete_mania, {'uuid': mania_uuid}),
            (delete_mania_inv, {'uuid': mania_inv_uuid})
        ])

    def test_maniasInv_full_mutation(self):
        """This tests creates, updates and finally deletes a mania-investigator
        through the graphql queries.
        """
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'investigator': {'query': create_investigator},
            'mania': {'query': create_mania}
        })
        investigator_uuid = res['investigator']
        mania_uuid = res['mania']

        assert self.full_mutation_test(
            create_query=create_mania_inv,
            edit_query=edit_mania_inv,
            delete_query=delete_mania_inv,
            one_query=one_mania_inv,
            query_edge_name="allManiasInv",
            mutation_edge_name="maniaInvMutate",
            node_name="maniaInv",
            edition_key="duration",
            value_key=40,
            extras={
                "investigator_uuid": investigator_uuid,
                "mania_uuid": mania_uuid
            }
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_investigator, {'uuid': investigator_uuid}),
            (delete_mania, {'uuid': mania_uuid})
        ])


class TestGameQuery(GraphTest):
    """Test class that encapsulates all games graphql query tests."""
    def test_game_query_node(self):
        """Test acquisitions of a full list of games or by a single uuid.
        """
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'game': {'query': create_game}
        })
        game_uuid = res['game']

        assert self.full_research_test(
            all_games, one_game, 'allGames'
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_game, {'uuid': game_uuid})
        ])

    def test_game_full_mutation(self):
        """This tests creates, updates and finally deletes a game
        through the graphql queries.
        """
        assert self.full_mutation_test(
            create_query=create_game,
            edit_query=edit_game,
            delete_query=delete_game,
            one_query=one_game,
            query_edge_name="allGames",
            mutation_edge_name="gameMutate",
            node_name="game",
            edition_key="title",
            value_key="test_update",
            extras={}
        )


class TestCampaignInvQuery(GraphTest):
    """Test class that encapsulates all campaign-inv graphql query tests."""
    def test_campaign_inv_query_node(self):
        """Test acquisitions of a full list of campaign-inv or by a single
        uuid.
        """
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'investigator': {'query': create_investigator},
            'game': {'query': create_game}
        })
        investigator_uuid = res['investigator']
        campaign_uuid = res['game']
        campaign_inv_uuid = self.create_and_obtain_uuid(
            query=create_campaign_inv,
            model_name='campaignInv',
            uuids={
                'investigator_uuid': investigator_uuid,
                'campaign_uuid': campaign_uuid
            }
        )

        assert self.full_research_test(
            all_campaigns_inv, one_campaign_inv, 'allCampaignsInv'
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_investigator, {'uuid': investigator_uuid}),
            (delete_game, {'uuid': campaign_uuid}),
            (delete_campaign_inv, {'uuid': campaign_inv_uuid})
        ])

    def test_campaign_inv_full_mutation(self):
        """This tests creates, updates and finally deletes a campaign-inv
        through the graphql queries.
        """
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'investigator': {'query': create_investigator},
            'game': {'query': create_game},
            'game2': {
                'query': create_game,
                'alt_name': 'game'}
        })
        investigator_uuid = res['investigator']
        campaign_uuid = res['game']
        campaign_uuid2 = res['game2']

        assert self.full_mutation_test(
            create_query=create_campaign_inv,
            edit_query=edit_campaign_inv,
            delete_query=delete_campaign_inv,
            one_query=one_campaign_inv,
            query_edge_name="allCampaignsInv",
            mutation_edge_name="campaignInvMutate",
            node_name="campaignInv",
            edition_key="campaign",
            value_key={'uuid': campaign_uuid2},
            extras={
                'investigator_uuid': investigator_uuid,
                'campaign_uuid': campaign_uuid,
                'campaign_uuid2': campaign_uuid2
            }
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_investigator, {'uuid': investigator_uuid}),
            (delete_game, {'uuid': campaign_uuid}),
            (delete_game, {'uuid': campaign_uuid2})
        ])


class TestInventoryInvQuery(GraphTest):
    """Test class that encapsulates all inventory-inv graphql query tests."""
    def test_inventorysInv_query_node(self):
        """Test acquisitions of a full list of inventory-inv or by a single
        uuid.
        """
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'investigator': {'query': create_investigator},
            'item': {'query': create_item}
        })
        investigator_uuid = res['investigator']
        item_uuid = res['item']
        inventory_inv_uuid = self.create_and_obtain_uuid(
            query=create_inventory_inv,
            model_name='inventoryInv',
            uuids={
                'investigator_uuid': investigator_uuid,
                'item_uuid': item_uuid
            }
        )

        assert self.full_research_test(
            all_inventorys_inv, one_inventory_inv, 'allInventorysInv'
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_investigator, {'uuid': investigator_uuid}),
            (delete_item, {'uuid': item_uuid}),
            (delete_inventory_inv, {'uuid': inventory_inv_uuid})
        ])

    def test_inventorysInv_full_mutation(self):
        """This tests creates, updates and finally deletes a inventory-inv
        through the graphql queries.
        """
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'investigator': {'query': create_investigator},
            'item': {'query': create_item},
            'item2': {
                'query': create_item,
                'alt_name': 'item'}
        })
        investigator_uuid = res['investigator']
        item_uuid = res['item']
        item_uuid2 = res['item2']

        assert self.full_mutation_test(
            create_query=create_inventory_inv,
            edit_query=edit_inventory_inv,
            delete_query=delete_inventory_inv,
            one_query=one_inventory_inv,
            query_edge_name="allInventorysInv",
            mutation_edge_name="inventoryInvMutate",
            node_name="inventoryInv",
            edition_key="item",
            value_key={'uuid': item_uuid2},
            extras={
                "investigator_uuid": investigator_uuid,
                "item_uuid": item_uuid,
                "item_uuid2": item_uuid2
            }
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_investigator, {'uuid': investigator_uuid}),
            (delete_item, {'uuid': item_uuid}),
            (delete_item, {'uuid': item_uuid2})
        ])


class TestDiaryInvQuery(GraphTest):
    """Test class that encapsulates all diary-inv graphql query tests."""
    def test_diarysInv_query_node(self):
        """Test acquisitions of a full list of diary-inv or by a single uuid.
        """
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'investigator': {'query': create_investigator}
        })
        investigator_uuid = res['investigator']
        diary_inv_uuid = self.create_and_obtain_uuid(
            query=create_diary_inv,
            model_name='diaryInv',
            uuids={'investigator_uuid': investigator_uuid}
        )

        assert self.full_research_test(
            all_diarys_inv, one_diary_inv, 'allDiarysInv'
        )

        # clean up auxiliar entities
        self.batch_instance_cleaner([
            (delete_investigator, {'uuid': investigator_uuid}),
            (delete_diary_inv, {'uuid': diary_inv_uuid})
        ])

    def test_diarysInv_full_mutation(self):
        """This tests creates, updates and finally deletes a diary-inv
        through the graphql queries.
        """
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'investigator': {'query': create_investigator}
        })
        investigator_uuid = res['investigator']

        assert self.full_mutation_test(
            create_query=create_diary_inv,
            edit_query=edit_diary_inv,
            delete_query=delete_diary_inv,
            one_query=one_diary_inv,
            query_edge_name="allDiarysInv",
            mutation_edge_name="diaryInvMutate",
            node_name="diaryInv",
            edition_key="title",
            value_key="test",
            extras={
                "investigator_uuid": investigator_uuid
            }
        )

        # clean up of auxiliar entities
        self.batch_instance_cleaner([
            (delete_investigator, {'uuid': investigator_uuid})
        ])


class TestTagInvQuery(GraphTest):
    """Test class that encapsulates all tags-investigator graphql query tests.
    """
    def test_tags_inv_query_node(self):
        """Test acquisitions of a full list of tags-investigator or by a single
        uuid.
        """
        res = self.batch_instance_builder({
            'investigator': {'query': create_investigator},
            'tag': {'query': create_tag}
        })
        investigator_uuid = res['investigator']
        tag_uuid = res['tag']
        tag_inv_uuid = self.create_and_obtain_uuid(
            query=create_tag_inv,
            model_name='tagInv',
            uuids={
                'investigator_uuid': investigator_uuid,
                'tag_uuid': tag_uuid
            }
        )

        assert self.full_research_test(
            all_tags_inv, one_tag_inv, 'allTagsInv'
        )

        # clean up of auxiliar entities
        self.batch_instance_cleaner([
            (delete_tag_inv, {'uuid': tag_inv_uuid}),
            (delete_investigator, {'uuid': investigator_uuid}),
            (delete_tag, {'uuid': tag_uuid}),
        ])

    def test_tags_inv_full_mutation(self):
        """This tag_1tests creates, updates and finally deletes a
        tag-investigator through the graphql queries.
        """
        # Build content and content tag to be looked for
        res = self.batch_instance_builder({
            'investigator': {'query': create_investigator},
            'tag': {'query': create_tag},
            'tag2': {
                'query': create_tag,
                'alt_name': 'tag'}
        })
        investigator_uuid = res['investigator']
        tag_uuid = res['tag']
        tag_uuid2 = res['tag2']

        test_result = self.full_mutation_test(
            create_query=create_tag_inv,
            edit_query=edit_tag_inv,
            delete_query=delete_tag_inv,
            one_query=one_tag_inv,
            query_edge_name="allTagsInv",
            mutation_edge_name="tagInvMutate",
            node_name="tagInv",
            edition_key="tag",
            value_key={'uuid': tag_uuid2},
            extras={
                "investigator_uuid": investigator_uuid,
                "tag_uuid": tag_uuid,
                "tag_uuid_2": tag_uuid2
            }
        )

        # clean up of auxiliar entities
        self.batch_instance_cleaner([
            (delete_investigator, {'uuid': investigator_uuid}),
            (delete_tag, {'uuid': tag_uuid}),
            (delete_tag, {'uuid': tag_uuid2})
        ])

        assert test_result