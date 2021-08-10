from ast import literal_eval as leval
from json import dumps, loads
from random import choice

from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from creator.constants import SILOUETTES as silouettes
from creator.constants import ITEM_CATEGORIES as item_categories, ITEM_SUBCATEGORIES as item_subcategories
from creator.helpers.investigator import generate_full_half_fifth_values
from creator.helpers.views_helper import ALL_MODELS as all_models
from creator.helpers.views_helper import (gear_sanitizer,
                                          generate_attributes_form,
                                          generate_basic_info_form,
                                          generate_derivative_attributes_form,
                                          skills_sanitizer, skills_sum)
from creator.models import (Inventory, Investigator, Item, ManiaInvestigator,
                            Occupation, PhobiaInvestigator, Portrait, Skills,
                            SpellInvestigator, Mania, Phobia, Spell)
from creator.random_inv import (RandomInvestigator, base_skills_generator,
                                free_point_assigner, occ_point_assigner)

# Create your views here.

class GeneralInvestigatorViews:
    '''Views associated to the investigator entity and not to its periferals.'''

    def get_investigators_data(request, inv, **kwargs):
        '''Retrieve all information associated to an
        Investigator.'''
        investigator = Investigator.objects.get(
            uuid=inv
        )
        res = {
            'investigator': investigator
        }

        return render(
            request, 'character_sheet.html',
            {'res': res}
        )


    def investigators_basic_info(request, inv):
        '''Generate investigator basic information form.'''
        investigator = generate_basic_info_form(
            request, inv)
        occupations = [
            [occ.uuid, occ.__str__()] for occ in 
            Occupation.objects.all()
        ]
        investigator = {
            'name': investigator.name,
            'uuid': investigator.uuid,
            'sex': investigator.sex,
            'occupation': investigator.occupation.uuid,
            'age': investigator.age,
            'player': investigator.player,
            'residence': investigator.residence,
            'birthplace': investigator.birthplace
        }
        return JsonResponse(
            {
                'investigator': investigator,
                'occupations': occupations
            },
            status=200
        )


    def get_investigators_portrait(request, inv):
        '''Retrieve investigators portrait.'''
        investigator = Investigator.objects.get(
            uuid=inv
        )
        portrait = Portrait.objects.filter(
            investigator=investigator
        ).first()
        default_portrait = silouettes[0] if investigator.sex == 'M' else silouettes[1]

        res = {'portrait': portrait.portrait.url if portrait is not None else default_portrait}
        return JsonResponse(res, status=200)


    def generate_random_investigator(request):
        rand = RandomInvestigator()
        rand.build()

        return redirect(
            GeneralInvestigatorViews.get_investigators_data,
            inv=rand.investigator.uuid
        )


class AttributesInvestigatorViews:
    '''Views associated to the attribute of an investigator.'''

    def investigators_attributes(request, inv):
        '''Retrieve investigators attributes.'''
        inv = generate_attributes_form(
            request, inv
        )
        attributes = inv.attributes_detail
        attributes['MOV'] = [inv.move]
        attributes["BUILD"] = list(inv.build)
        return JsonResponse(
            {'attributes': attributes}, status=200)


    def investigators_attribute_update(request, inv):
        '''Retrieve investigators attributes.'''
        inv = Investigator.objects.filter(uuid=inv)

        if request.POST:
            data_unclean = dict(request.POST)
            attr = list(data_unclean.keys())[0]
            attr_value = int(data_unclean[attr][0])
            inv.update(**{attr: attr_value})
            attributes = {attr: generate_full_half_fifth_values(attr_value)}
            inv = inv.first()
            attributes['MOV'] = [inv.move]
            attributes["BUILD"] = list(inv.build)
            return JsonResponse(attributes, status=200)
        return JsonResponse({'response': 'Unauthorized'}, status=401)

    def investigators_deriv_attrs(request, inv):
        '''Generate investigator derivative attributes form.'''
        inv = generate_derivative_attributes_form(
            request, inv)
        investigator_relevant_data = {
            "health": inv.health,
            "magic_points": inv.magic_points,
            "luck": inv.luck,
            "sanity": inv.sanity
        }
        return JsonResponse(
            {'investigator': investigator_relevant_data},
            status=200
    )


class SkillsInvestigatorViews:
    '''Views associated to the skills of an investigator.'''

    def get_investigators_skills(request, inv):
        investigator = Investigator.objects.get(
            uuid=inv
        )
        # Retrieve skills
        skills_sanitized = skills_sanitizer(investigator)
        res = {'skills': skills_sanitized}
        return JsonResponse(res, status=200)


    def update_investigators_skills(request, inv):
        investigator = Investigator.objects.get(
            uuid=inv
        )
        skills = request.POST.keys()
        for skill in skills:
            inv_sk = investigator.skills.get(skill)
            if inv_sk is not None:
                investigator.skills[skill]['value'] = int(request.POST[skill])
        investigator.save()
        skills_sanitized = skills_sanitizer(investigator)
        res = {'skills': skills_sanitized}
        return JsonResponse(res, status=200)


    def update_investigators_skill(request, inv):
        '''Update a single skill for an investigator.'''
        if request.method == "POST":
            investigator = Investigator.objects.get(
                uuid=inv
            )
            data_unclean = loads(request.body)
            improved = data_unclean.get('improved', False)
            skill = list(data_unclean.keys())[0]
            new_value = data_unclean[skill]
            assert isinstance(new_value, int), 'Invalid Value, Expected int'
            assigned_points = skills_sum(investigator.skills, 'value') - skills_sum(investigator.skills, 'base_value')
            if investigator.skills.get(skill) is None:
                return JsonResponse({'response': 'Invalid Skill'}, status=400)
            old_value = investigator.skills[skill]['value']
            points_change = new_value - old_value
            skill_pool = investigator.occupation_skill_points + investigator.free_skill_points
            if new_value < investigator.skills[skill]['base_value'] or (improved and points_change < 0) or new_value >= 99:
                return JsonResponse({'response': 'Invalid Value'}, status=400)
            if not improved and assigned_points + points_change > skill_pool:
                return JsonResponse({'response': 'Overassigned Skill'}, status=400)
            if improved:
                investigator.skills[skill]['improved'] = points_change
            else:
                investigator.skills[skill]['value'] = new_value
            investigator.save()
            res = {skill: list(generate_full_half_fifth_values(new_value))}
            return JsonResponse(res, status=200)
        return JsonResponse({'response': 'Unauthorized'}, status=401)


    def investigators_skills_reset(request, inv):
        investigator = Investigator.objects.get(
            uuid=inv
        )
        skills = list(Skills.objects.all())
        base_skills_generator(skills, investigator)
        skills_sanitized = skills_sanitizer(investigator)
        res = {'skills': skills_sanitized}
        return JsonResponse(res, status=200)


    def investigators_skills_shuffle(request, inv):
        investigator = Investigator.objects.get(
            uuid=inv
        )
        skills = list(Skills.objects.all())
        base_skills_generator(skills, investigator)
        proff_points = investigator.occupation_skill_points
        occ_point_assigner(proff_points, investigator)
        # Assign free skill points
        free_point_assigner(investigator.free_skill_points, investigator)
        skills = sorted(investigator.skills)
        skills_sanitized = []
        for skill in skills:
            skills_sanitized.append(
                [
                    skill,
                    *generate_full_half_fifth_values(
                        investigator.skills[skill]['value']
                    )
                ]
            )
        res = {'skills': skills_sanitized}
        return JsonResponse(res, status=200)


class ItemsInvestigatorViews:
    '''Views associated to the items manipulation of the investigator.'''

    def get_investigators_weapons(request, inv):
        '''Retrieve investigators weapons.'''
        investigator = Investigator.objects.get(
            uuid=inv
        )
        weapons = Inventory.objects.filter(
            investigator=investigator,
            item__category=3)
        weapons_results = []
        for weapon in weapons:
            w_dict = weapon.properties
            w_dict['skill_value'] = generate_full_half_fifth_values(
                investigator.skills[weapon.item.properties['skill']]['value']
            )
            w_dict['uuid'] = weapon.uuid
            weapons_results.append(w_dict)
        return JsonResponse({'weapons': weapons_results}, status=200)


    def get_investigators_gear(request, inv):
        '''Retrieve investigators gear.'''
        investigator = Investigator.objects.get(
            uuid=inv
        )
        gear = gear_sanitizer(investigator)
        return JsonResponse({'gear': gear}, status=200)


    def remove_investigators_gear(request, inventory):
        '''Remove inventory from investigator.'''
        inventory = Inventory.objects.get(uuid=inventory)
        inventory.delete()
        return JsonResponse({'response': 'Ok'}, status=200)


    def edit_investigators_gear(request, inventory):
        '''Remove inventory from investigator.'''
        inventory = Inventory.objects.get(uuid=inventory)
        if request.POST:
            data = dict(request.POST)
            sanitize_data = {
                k: data[k][0] for k in data.keys()
                if k != 'stock'
            }
            inventory.stock = int(data.get('stock', [1])[0])
            inventory.properties.update(**sanitize_data)
            inventory.save()
            inventory.properties['stock'] = inventory.stock
            return JsonResponse(inventory.properties, status=200)
        return JsonResponse({'response': 'Unauthorized'}, status=401)

    def add_item(request):
        if request.POST:
            data = dict(request.POST)
            sanitize_data = {
                k: data[k][0] for k in data.keys()
            }
            inv = Investigator.objects.get(uuid=sanitize_data['inv'])
            item = all_models['items'].objects.get(uuid=sanitize_data['item'])
            props = item.properties.copy()
            props['title'] = item.title
            props['era'] = item.era
            props['price'] = item.base_price
            props['rare'] = item.rare
            props['description'] = item.description
            if item.category == item_categories[2][0]:
                props['ammo'] = item.properties["bullets_in_gun_mag"]
            inventory = Inventory.objects.filter(investigator=inv, item=item, properties=props).first()
            #checks if the investigator already has the item, if not it adds it
            if inventory is None:
                inventory = Inventory(
                    investigator=inv,
                    item=item,
                    properties=props
                    )
                inventory.save()
                if item.category == item_categories[2][0]:
                    props['skill_value'] = generate_full_half_fifth_values(
                    inv.skills[item.properties['skill']]['value'])
                return JsonResponse(
                    {'item': {'uuid': inventory.uuid, 'properties': props, 'stock': inventory.stock },
                     'category': item.category}, status=201)
            else:
                stock = inventory.stock
                inventory.stock = stock + 1
                inventory.save()
                return JsonResponse({'response': 'Stock Increased'}, status=200)
        return JsonResponse({'response': 'Unauthorized'}, status=401)

class BackstoryInvestigatorViews:
    '''Views associated to all backstory related views of an investigator.'''

    def get_investigators_manias_and_phobias(request, inv):
        '''Retrieve investigators manias and phobias.'''
        investigator = Investigator.objects.get(
            uuid=inv
        )
        manias = ManiaInvestigator.objects.filter(
            investigator=investigator
        )
        phobias = PhobiaInvestigator.objects.filter(
            investigator=investigator
        )
        phobias = [[phobia.phobia.uuid, phobia.phobia.title] for phobia in phobias]
        manias = [[mania.mania.uuid, mania.mania.title] for mania in manias]
        res = {
            'manias': manias,
            'phobias': phobias
        }
        return JsonResponse(res, status=200)


    def get_investigators_arcane(request, inv):
        '''Retrieve arcane artifacts and spells from investigator.'''
        investigator = Investigator.objects.get(
            uuid=inv
        )
        # Retrieve arcane
        artifacts = Inventory.objects.filter(
            investigator=investigator,
            item__category=item_categories[0][0],
            properties__subcategory=item_subcategories['artifacts']

        )
        tomes = Inventory.objects.filter(
            investigator=investigator, 
            item__category=item_categories[0][0],
            properties__subcategory=item_subcategories['tomes']
            )
        occult_books= Inventory.objects.filter(
            investigator=investigator, 
            item__category=item_categories[0][0],
            properties__subcategory=item_subcategories['occult_books']
            )
        spells = SpellInvestigator.objects.filter(
            investigator=investigator
        )
        spells = [
            {
                'name': spell.spell.name,
                'uuid': spell.spell.uuid,
                'cost': spell.spell.cost,
                'casting_time': spell.spell.casting_time,
                'description': spell.spell.description,
                'deeper_magic': spell.spell.deeper_magic,
                'alternative_names': spell.spell.alternative_names
            }
            for spell in spells
        ]
        artifacts = [
            {
                'uuid': artifact.uuid,
                'properties':{
                    'title': artifact.properties['title'],
                    'description': artifact.properties['description'],
                    'used_by': artifact.properties['used_by'],
                    'subcategory': artifact.properties['subcategory']
                }
            }
            for artifact in artifacts
        ]
        tomes = [
            {
                'uuid': tome.uuid,
                'properties': {
                    'title': tome.properties['title'],
                    'author': tome.properties['author'],
                    'mythos_rating': tome.properties['mythos_rating'],
                    'cthulhu_mythos_initial': tome.properties['cthulhu_mythos_initial'],
                    'cthulhu_mythos_full': tome.properties['cthulhu_mythos_full'],
                    'language': tome.properties['language'],
                    'sanity': tome.properties['sanity'],
                    'subheading': tome.properties['subheading'],
                    'subcategory': tome.properties['subcategory']
                }
            }
            for tome in tomes
        ]
        occult_books = [
            {
                'uuid': occult_book.uuid,
                'properties': {
                    'title': occult_book.properties['title'],
                    'subheading': occult_book.properties['subheading'],
                    'description': occult_book.properties['description'],
                    'sanity': occult_book.properties['sanity'],
                    'occult': occult_book.properties['occult'],
                    'subheading': occult_book.properties['subheading'],
                    'subcategory': occult_book.properties['subcategory']
                }
            }
            for occult_book in occult_books
        ]
        res = {
            'artifacts': artifacts,
            'tomes': tomes,
            'occult_books': occult_books,
            'spells': spells,
            'encounters': investigator.encounters_with_strange_entities
        }
        return JsonResponse(res, status=200)


    def get_investigators_backstory(request, inv):
        '''Retrieve arcane artifacts and spells from investigator.'''
        investigator = Investigator.objects.get(
            uuid=inv
        )
        res = {
            'description': investigator.description,
            'ideologies': investigator.ideologies,
            'significant_people': investigator.significant_people,
            'meaningful_locations': investigator.meaningful_locations,
            'treasured_possessions': investigator.treasured_possessions,
            'traits': investigator.traits,
            'injuries_scars': investigator.injure_scars,
            'encounters_with_strange_entities': investigator.encounters_with_strange_entities
        }
        return JsonResponse(res, status=200)


    def update_investigators_backstory(request, inv):
        '''Update investigators backstory information.'''
        investigator = Investigator.objects.filter(
            uuid=inv
        )
        if request.POST:
            data = dict(request.POST)
            sanitize_data = {
                k: data[k][0] for k in data.keys()
            }
            investigator.update(**sanitize_data)
            investigator = investigator.first().__dict__
            res = {
                k: investigator[k] for k in sanitize_data
            }
            return JsonResponse(res, status=200)
        return JsonResponse({'response': 'Unauthorized'}, status=401)


    def add_mania(request):
        if request.POST:
            data = dict(request.POST)
            sanitize_data = {
                k: data[k][0] for k in data.keys()
            }
            inv_mania = ManiaInvestigator()
            inv = Investigator.objects.get(uuid=sanitize_data['inv'])
            mania = all_models['manias'].objects.get(uuid=sanitize_data['mania'])
            mania_query = ManiaInvestigator.objects.filter(investigator=inv,mania=mania)
            #checks if the investigator already has the mania, if not it adds it
            if not mania_query.exists():
                inv_mania.mania = mania
                inv_mania.investigator = inv
                inv_mania.save()
                return JsonResponse({'title': mania.__str__()}, status=200)
            else:
                return JsonResponse({'response': 'Already in use'}, status=304)
        return JsonResponse({'response': 'Unauthorized'}, status=401)


    def remove_mania(request, inv, mania):
        '''Remove mania from investigator.'''
        mania = ManiaInvestigator.objects.get(investigator=inv,mania=mania)
        mania.delete()
        return JsonResponse({'response': 'Ok'}, status=200)


    def add_phobia(request):
        if request.POST:
            data = dict(request.POST)
            sanitize_data = {
                k: data[k][0] for k in data.keys()
            }
            inv_phobia = PhobiaInvestigator()
            inv = Investigator.objects.get(uuid=sanitize_data['inv'])
            phobia = all_models['phobias'].objects.get(uuid=sanitize_data['phobia'])
            phobia_query = PhobiaInvestigator.objects.filter(investigator=inv,phobia=phobia)
            #checks if the investigator already has the phobia, if not it adds it
            if not phobia_query.exists():
                inv_phobia.phobia = phobia
                inv_phobia.investigator = inv
                inv_phobia.save()
                return JsonResponse({'title': phobia.__str__()}, status=200)
            else:
                return JsonResponse({'response': 'Already in use'}, status=304)
        return JsonResponse({'response': 'Unauthorized'}, status=401)


    def remove_phobia(request, inv, phobia):
        '''Remove mania from investigator.'''
        phobia = PhobiaInvestigator.objects.get(investigator=inv,phobia=phobia)
        phobia.delete()
        return JsonResponse({'response': 'Ok'}, status=200)


    def add_spell(request):
        if request.POST:
            data = dict(request.POST)
            sanitize_data = {
                k: data[k][0] for k in data.keys()
            }
            inv_spell = SpellInvestigator()
            inv = Investigator.objects.get(uuid=sanitize_data['inv'])
            spell = all_models['spells'].objects.get(uuid=sanitize_data['spell'])
            spell_query = SpellInvestigator.objects.filter(investigator=inv,spell=spell)
            #checks if the investigator already has the spell, if not it adds it
            if not spell_query.exists():
                inv_spell.spell = spell
                inv_spell.investigator = inv
                inv_spell.save()
                return JsonResponse({'spell': spell.safe_dict()}, status=200)
            else:
                return JsonResponse({'response': 'Already in use'}, status=304)
        return JsonResponse({'response': 'Unauthorized'}, status=401)


    def remove_spell(request, inv, spell):
        '''Remove spell from investigator.'''
        spell = SpellInvestigator.objects.get(investigator=inv,spell=spell)
        spell.delete()
        return JsonResponse({'response': 'Ok'}, status=200)


class GenericViews:
    '''Agnostic model views.'''

    common_models = {
        # if tuples second element is unset will look on key 'title'
        Item: [],
        Skills: [],
        Occupation: [],
        Mania: [],
        Phobia: [],
        Spell: ['name', 'alternative_names']
    }

    def generic_model_list(request, model_type):

        res = {
            'model_name': model_type,
            'records_title': [[model.uuid, model.__str__()] for model in all_models[model_type].objects.all()],
        }

        return JsonResponse(res, status=200)

    def record_detail(request, id, model_name):
        record = all_models[model_name].objects.get(uuid=id)
        rec = {
            'record': record.safe_dict()
        }

        return JsonResponse(rec, status=200)


    def generic_search(request):
        '''
            General searcher, this view should be capable of searching by name/title on
            a defined set of models and capable of accepting filters.

        '''
        if request.POST:
            # apply filters
            data_unclean = dict(request.POST)
            res = {
            "results": []
            }
            return JsonResponse(res, status=200)
        else:
            # simple search
            query = str(request.GET.get('q'))
            unclean_results = []
            for model in GenericViews.common_models:
                especial_keys = GenericViews.common_models[model]
                if especial_keys:
                    for key in especial_keys:
                        unclean_results.extend(
                            model.objects.filter(
                                **{f'{key}__icontains': query},
                            )
                        )
                else:
                    unclean_results.extend(
                        list(model.objects.filter(
                            title__icontains=query 
                        ))
                    )
            sanitized_results = {
                str(res.uuid): res.safe_dict() for res in unclean_results
            }
            return JsonResponse(sanitized_results, status=200)