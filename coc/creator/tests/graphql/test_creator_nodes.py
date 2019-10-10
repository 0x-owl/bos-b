"""
This tests must be run having an instance of the django server running
and a seeded database, either locally or remotely for them to work.
"""
from random import choice

from creator.tests.graphql.queries import (all_attrs_inv, all_diarys_inv,
                                           all_games, all_investigators,
                                           all_items, all_manias,
                                           all_manias_inv, all_occ,
                                           all_phobias, all_phobias_inv,
                                           all_skills, all_skills_inv,
                                           all_spells, all_tags, all_tags_inv,
                                           all_weapons, create_attr_inv,
                                           create_diary_inv, create_game,
                                           create_investigator, create_item,
                                           create_mania, create_mania_inv,
                                           create_occ, create_phobia,
                                           create_phobia_inv, create_skill,
                                           create_skill_inv, create_spell,
                                           create_tag, create_tag_inv,
                                           create_weapon, delete_attr_inv,
                                           delete_diary_inv, delete_game,
                                           delete_investigator, delete_item,
                                           delete_mania, delete_mania_inv,
                                           delete_occ, delete_phobia,
                                           delete_phobia_inv, delete_skill,
                                           delete_skill_inv, delete_spell,
                                           delete_tag, delete_tag_inv,
                                           delete_weapon, edit_attr_inv,
                                           edit_diary_inv, edit_game,
                                           edit_investigator, edit_item,
                                           edit_mania, edit_mania_inv,
                                           edit_occ, edit_phobia,
                                           edit_phobia_inv, edit_skill,
                                           edit_skill_inv, edit_spell,
                                           edit_tag, edit_tag_inv, edit_weapon,
                                           one_attr_inv, one_diary_inv,
                                           one_game, one_investigator,
                                           one_item, one_mania, one_mania_inv,
                                           one_occ, one_phobia, one_phobia_inv,
                                           one_skill, one_skill_inv, one_spell,
                                           one_tag, one_tag_inv, one_weapon)

from creator.tests.graphql.constants import GraphTest


class TestInvestigatorQuery(GraphTest):
    """Test class that encapsulates all investigator graphql query tests."""
    def test_investigators_query_node(self):
        """Test acquisitions of a full list of investigators or by a single
        uuid.
        """
        data_investigator, status = self.run_query(
            create_investigator.format())
        assert status == 200
        investigator_uuid = (
            data_investigator['investigatorMutate']['investigator']['uuid'])

        assert self.full_research_test(
            all_investigators, one_investigator, 'allInvestigators')

        self.run_query(delete_investigator.format(uuid=investigator_uuid))

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


class TestWeaponQuery(GraphTest):
    """Test class that encapsulates all weapons graphql query tests."""
    def test_items_query_node(self):
        """Test acquisitions of a full list of weapons or by a single uuid.
        """
        data_weapon, status = self.run_query(create_weapon.format())
        assert status == 200
        weapon_uuid = data_weapon['weaponMutate']['weapon']['uuid']
        assert self.full_research_test(
            all_weapons, one_weapon, 'allWeapons'
        )
        self.run_query(delete_weapon.format(uuid=weapon_uuid))

    def test_weapon_full_mutation(self):
        """This tests creates, updates and finally deletes a weapon
        through the graphql queries.
        """
        assert self.full_mutation_test(
            create_query=create_weapon,
            edit_query=edit_weapon,
            delete_query=delete_weapon,
            one_query=one_weapon,
            query_edge_name="allWeapons",
            mutation_edge_name="weaponMutate",
            node_name="weapon",
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
    """Test class that encapsulates all phobias graphql query tests."""
    def test_phobiasInv_query_node(self):
        """Test acquisitions of a full list of phobias or by a single uuid.
        """
        data_investigator, status = self.run_query(
            create_investigator.format())
        assert status == 200
        investigator_uuid = (
            data_investigator['investigatorMutate']['investigator']['uuid'])

        data_phobia, status = self.run_query(create_phobia.format())
        assert status == 200
        phobia_uuid = (
            data_phobia['phobiaMutate']['phobia']['uuid'])

        data_phobia_inv, status = self.run_query(
            create_phobia_inv.format(
                investigator=investigator_uuid,
                phobia=phobia_uuid))
        assert status == 200
        phobia_inv_uuid = (
            data_phobia_inv['phobiaInvMutate']['phobiaInv']['uuid'])

        assert self.full_research_test(
            all_phobias_inv, one_phobia_inv, 'allPhobiasInv'
        )

        # clean up auxiliar entities
        self.run_query(delete_investigator.format(uuid=investigator_uuid))
        self.run_query(delete_phobia_inv.format(uuid=phobia_uuid))
        self.run_query(delete_phobia.format(uuid=phobia_inv_uuid))

    def test_phobiasInv_full_mutation(self):
        """This tests creates, updates and finally deletes a phobia
        through the graphql queries.
        """
        data_investigator, status = self.run_query(
            create_investigator.format())
        assert status == 200
        investigator_uuid = (
            data_investigator['investigatorMutate']['investigator']['uuid'])

        data_phobia, status = self.run_query(create_phobia.format())
        assert status == 200
        phobia_uuid = (
            data_phobia['phobiaMutate']['phobia']['uuid'])

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
            extras={"investigator": investigator_uuid, "phobia": phobia_uuid}
        )

        # clean up auxiliar entities
        self.run_query(delete_investigator.format(uuid=investigator_uuid))
        self.run_query(delete_phobia.format(uuid=phobia_uuid))


class TestManiaInvQuery(GraphTest):
    """Test class that encapsulates all phobias graphql query tests."""
    def test_maniasInv_query_node(self):
        """Test acquisitions of a full list of phobias or by a single uuid.
        """
        data_investigator, status = self.run_query(
            create_investigator.format())
        assert status == 200
        investigator_uuid = (
            data_investigator['investigatorMutate']['investigator']['uuid'])

        data_mania, status = self.run_query(create_mania.format())
        assert status == 200
        mania_uuid = (
            data_mania['maniaMutate']['mania']['uuid'])

        data_mania_inv, status = self.run_query(
            create_mania_inv.format(
                investigator=investigator_uuid,
                mania=mania_uuid))
        assert status == 200
        mania_inv_uuid = (
            data_mania_inv['maniaInvMutate']['maniaInv']['uuid'])

        assert self.full_research_test(
            all_manias_inv, one_mania_inv, 'allManiasInv'
        )

        # clean up auxiliar entities
        self.run_query(delete_investigator.format(uuid=investigator_uuid))
        self.run_query(delete_mania.format(uuid=mania_uuid))
        self.run_query(delete_mania_inv.format(uuid=mania_inv_uuid))

    def test_maniasInv_full_mutation(self):
        """This tests creates, updates and finally deletes a phobia
        through the graphql queries.
        """
        data_investigator, status = self.run_query(
            create_investigator.format())
        assert status == 200
        investigator_uuid = (
            data_investigator['investigatorMutate']['investigator']['uuid'])

        data_mania, status = self.run_query(create_mania.format())
        assert status == 200
        mania_uuid = (
            data_mania['maniaMutate']['mania']['uuid'])

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
            extras={"investigator": investigator_uuid, "mania": mania_uuid}
        )

        # clean up auxiliar entities
        self.run_query(delete_investigator.format(uuid=investigator_uuid))
        self.run_query(delete_mania_inv.format(uuid=mania_uuid))


class TestGameQuery(GraphTest):
    """Test class that encapsulates all games graphql query tests."""
    def test_game_query_node(self):
        """Test acquisitions of a full list of games or by a single uuid.
        """
        data_game, status = self.run_query(create_game.format())
        assert status == 200
        game_uuid = data_game['gameMutate']['game']['uuid']

        assert self.full_research_test(
            all_games, one_game, 'allGames'
        )

        self.run_query(delete_game.format(uuid=game_uuid))

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
    """Test class that encapsulates all tags graphql query tests."""
    def test_tags_inv_query_node(self):
        """Test acquisitions of a full list of tags or by a single uuid.
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
        """This tag_1tests creates, updates and finally deletes a tag
        through the graphql queries.
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


class TestSkillInvQuery(GraphTest):
    """Test class that encapsulates all skills_inv graphql query tests."""
    def test_skills_inv_query_node(self):
        """Test acquisitions of a full list of skills_inv or by a single uuid.
        """
        data_investigator, status = self.run_query(
            create_investigator.format())
        assert status == 200
        investigator_uuid = (
            data_investigator['investigatorMutate']['investigator']['uuid'])
        data_skill, status = self.run_query(
            create_skill.format())
        assert status == 200
        skill_uuid = (
            data_skill['skillMutate']['skill']['uuid'])

        data_skill_inv, status = self.run_query(
            create_skill_inv.format(
                investigator=investigator_uuid,
                skill=skill_uuid
            ))
        assert status == 200
        skill_inv_uuid = (
            data_skill_inv['skillInvMutate']['skillInv']['uuid'])

        assert self.full_research_test(
            all_skills_inv, one_skill_inv, 'allSkillsInv'
        )

        # clean up auxiliar entities
        self.run_query(delete_investigator.format(uuid=investigator_uuid))
        self.run_query(delete_skill.format(uuid=skill_uuid))
        self.run_query(delete_skill_inv.format(uuid=skill_inv_uuid))

    def test_skills_inv_full_mutation(self):
        """This tests creates, updates and finally deletes a skills_inv
        through the graphql queries.
        """
        data_investigator, status = self.run_query(
            create_investigator.format())
        assert status == 200
        investigator_uuid = (
            data_investigator['investigatorMutate']['investigator']['uuid'])
        data_skill, status = self.run_query(
            create_skill.format())
        assert status == 200
        skill_uuid = (
            data_skill['skillMutate']['skill']['uuid'])

        assert self.full_mutation_test(
            create_query=create_skill_inv,
            edit_query=edit_skill_inv,
            delete_query=delete_skill_inv,
            one_query=one_skill_inv,
            query_edge_name="allSkillsInv",
            mutation_edge_name="skillInvMutate",
            node_name="skillInv",
            edition_key="value",
            value_key=33,
            extras={
                "investigator": investigator_uuid,
                "skill": skill_uuid
            }
        )

        # clean up auxiliar entities
        self.run_query(delete_investigator.format(uuid=investigator_uuid))
        self.run_query(delete_skill.format(uuid=skill_uuid))


class TestAttrInvQuery(GraphTest):
    """Test class that encapsulates all attr_inv graphql query tests."""
    def test_attrs_inv_query_node(self):
        """Test acquisitions of a full list of attr_inv or by a single uuid.
        """
        data_investigator, status = self.run_query(
            create_investigator.format())
        assert status == 200
        investigator_uuid = (
            data_investigator['investigatorMutate']['investigator']['uuid'])

        data_attr_inv, status = self.run_query(
            create_attr_inv.format(investigator=investigator_uuid))
        assert status == 200
        attr_inv_uuid = (
            data_attr_inv['attrInvMutate']['attrInv']['uuid'])

        assert self.full_research_test(
            all_attrs_inv, one_attr_inv, 'allAttrsInv'
        )

        self.run_query(delete_investigator.format(uuid=investigator_uuid))
        self.run_query(delete_attr_inv.format(uuid=attr_inv_uuid))

    def test_attrs_inv_full_mutation(self):
        """This tests creates, updates and finally deletes a phobia
        through the graphql queries.
        """
        data_investigator, status = self.run_query(
            create_investigator.format())
        assert status == 200
        investigator_uuid = (
            data_investigator['investigatorMutate']['investigator']['uuid'])

        assert self.full_mutation_test(
            create_query=create_attr_inv,
            edit_query=edit_attr_inv,
            delete_query=delete_attr_inv,
            one_query=one_attr_inv,
            query_edge_name="allAttrsInv",
            mutation_edge_name="attrInvMutate",
            node_name="attrInv",
            edition_key="value",
            value_key=40,
            extras={"investigator": investigator_uuid}
        )

        # clean up of auxiliar entities
        self.run_query(delete_investigator.format(uuid=investigator_uuid))
