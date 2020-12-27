# Investigator

all_investigators = """
{
    allInvestigators{
        edges{
            node{
                uuid
            }
        }
    }
}
"""

one_investigator = """
{{
    allInvestigators(uuid: "{uuid}"){{
        edges{{
            node{{
                uuid
            }}
        }}
    }}
}}
"""

all_relevant_data_from_investigator = """
query {{
	allInvestigators(uuid: "{uuid}"){{
	  	edges {{
			node {{
			  	uuid,
			  	name,
			  	age,
				player,
				birthplace,
				residence,
				sex,
				occupation{{
				  uuid,
				  title,
				  creditRatingMin,
				  creditRatingMax
				}}
			  	investigatorattributeSet {{
					edges {{
					  	node {{
							uuid,
							attr,
							value
					  	}}
					}}
			  	}},
				luck,
				sanity,
				significantPeople,
				ideologies,
				traits,
			  	investigatorskillsSet {{
					edges {{
					  	node {{
							uuid,
						  	skill{{
						    	title
						  	}},
				    		value
				  		}}
					}}
			  	}}
			}}
		}}
	}}
}}
"""


create_investigator = """
mutation{{
  investigatorMutate(
    input: {{
      user:1, name: "Test", player: "Test",
      sex: "M", residence: "Capital", birthplace: "Capital", age: 23,
      occupation: 7, ideologies: "prueba", description: "prueba",
      traits: "prueba", injureScars: "prueba", significantPeople:
      "prueba", treasuredPossessions: "prueba",
      encountersWithStrangeEntities: "prueba",
      meaningfulLocations: "prueba", method: "CREATE"
    }}){{
    investigator{{
        uuid,
        name,
        player,
        sex,
        residence,
        birthplace,
        age,
        occupation{{
          title
        }}
        ideologies,
        description,
        traits,
        meaningfulLocations,
        injureScars,
        significantPeople,
        treasuredPossessions,
        encountersWithStrangeEntities
      }}
  }}
}}

"""

delete_investigator = """
mutation{{
  investigatorMutate(
    input: {{
      uuid: "{uuid}", method: "DELETE"
    }}){{
    investigator{{
        uuid,
        name,
        player,
        sex,
        residence,
        birthplace,
        age,
        occupation{{
          title
        }}
        ideologies,
        description,
        traits,
        meaningfulLocations,
        injureScars,
        significantPeople,
        treasuredPossessions,
        encountersWithStrangeEntities
      }}
  }}
}}
"""

edit_investigator = """
mutation{{
  investigatorMutate(
    input: {{
      uuid: "{uuid}", user:1, name: "Test", player: "TestUpdate", sex: "M",
      residence: "Capital", birthplace: "Capital", age: 23,
      occupation: 7, ideologies: "prueba", description: "prueba",
      traits: "prueba", injureScars: "prueba", significantPeople:
      "prueba", treasuredPossessions: "prueba",
      encountersWithStrangeEntities: "prueba156",
      meaningfulLocations: "prueba", method: "UPDATE"
    }}){{
    investigator{{
        uuid,
        name,
        player,
        sex,
        residence,
        birthplace,
        age,
        occupation{{
          title
        }}
        ideologies,
        description,
        traits,
        meaningfulLocations,
        injureScars,
        significantPeople,
        treasuredPossessions,
        encountersWithStrangeEntities
      }}
  }}
}}
"""

# Skills

all_skills = """
{
    allSkills{
        edges{
            node{
                uuid
            }
        }
    }
}
"""

one_skill = """
{{
    allSkills(uuid: "{uuid}"){{
        edges{{
            node{{
                uuid,
                skills,
                year
            }}
        }}
    }}
}}
"""

create_skill = """
mutation{
  skillMutate(
    input:{
      method: "CREATE",
      year: "Future",
      skills: "{\\"test_skill\\":{\\"title\\": \\"test_skill\\"}}"
    }){
    skill{
      uuid,
      year,
      skills
    }
  }
}
"""

edit_skill = """
mutation{{
  skillMutate(
    input:{{
      method: "UPDATE",
      uuid: "{uuid}",
      year: "FutureX2",
      skills: "{{\\"Test Skill\\":{{\\"title\\": \\"test_skill2\\"}}}}"
  }}){{
    skill{{
      uuid,
      year,
      skills
    }}
  }}
}}
"""

delete_skill = """
mutation{{
  skillMutate(
    input:{{
      uuid: "{uuid}",
      method: "DELETE"
    }}){{
    skill{{
      uuid,
      year,
      skills
    }}
  }}
}}
"""

# Tag

all_tags = """
query{
  allTags{
    edges{
      node{
        uuid
      }
    }
  }
}
"""

one_tag = """
query{{
    allTags(uuid:"{uuid}"){{
        edges{{
            node{{
                title,
                id,
            }}
        }}
    }}
}}
"""

create_tag = """
mutation{{
  tagMutate(
    input:{{
      method: "CREATE",
      title: "test-tag",
      user: 1
    }}){{
      tag{{
        uuid
        title
      }}
    }}
}}
"""

edit_tag = """
mutation{{
    tagMutate(
        input:{{
            method: "UPDATE",
            user: 1,
            title: "test-tag2",
            uuid: "{uuid}"
        }}
    ){{
        tag{{
            id,
            uuid,
            title
        }}
   }}
}}
"""

delete_tag = """
mutation{{
    tagMutate(
        input: {{
            user: 1,
            uuid: "{uuid}",
            method: "DELETE"
          }}){{
        tag{{
            id,
            uuid,
            title
        }}
    }}
}}
"""

# Item

all_items = """
{
  allItems{
    edges{
      node{
        uuid
      }
    }
  }
}
"""

one_item = """
{{
  allItems(uuid: "{uuid}"){{
    edges{{
      node{{
        uuid,
        category,
        properties
      }}
    }}
  }}
}}
"""

search_item = """
{{
  item(id: "{uuid}"){{
    uuid,
    category,
    properties {{
      title,
      price,
      description
    }}
  }}
}}
"""

create_item = """
mutation{
  itemMutate(
    input:{
      method: "CREATE",
      category: 2,
      properties: "{\\"title\\": \\"test-item-create\\",\\"description\\": \\"Created item\\",\\"price\\": 25.6}"
    }){
    item{
      uuid,
      category,
      properties
    }
  }
}
"""

edit_item = """
mutation{{
  itemMutate(
      input:{{
        method: "UPDATE",
        uuid: "{uuid}",
        category: 4,
        properties: "{{\\"title\\": \\"Test-2\\", \\"description\\": \\"TestUpdate\\"}}"
      }}){{
    item{{
      uuid,
      category,
      properties
    }}
  }}
}}
"""

delete_item = """
mutation{{
  itemMutate(
      input:{{
        method: "DELETE",
        uuid: "{uuid}"
      }}){{
    item{{
      uuid,
      category,
      properties
    }}
  }}
}}
"""

# Spells

all_spells = """
query{
  allSpells{
    edges{
      node{
        uuid
      }
    }
  }
}
"""

one_spell = """
query{{
  allSpells(uuid: "{uuid}"){{
    edges{{
      node{{
         name
      }}
    }}
  }}
}}
"""

create_spell = """
mutation{{
  spellMutate(
    input:{{
        method: "CREATE",
        notes: "test",
        name: "tester spell",
        description:"We may ommit this",
        cost: "1D6 Sanity",
        castingTime: "Immediate",
        user: 1
    }}){{
    spell{{
      uuid,
      notes,
      name
    }}
  }}
}}
"""

delete_spell = """
mutation{{
  spellMutate(
    input:{{
      uuid: "{uuid}",
      method: "DELETE",
      user: 1
    }}){{
    spell{{
        uuid
    }}
  }}
}}
"""

edit_spell = """
mutation{{
  spellMutate(
    input:{{
        uuid: "{uuid}",
        method: "UPDATE",
        notes: "test",
      user: 1
    }}){{
    spell{{
      notes
    }}
  }}
}}
"""

# Occupations

all_occ = """
query{
  allOccupations{
    edges{
      node{
        uuid
      }
    }
  }
}
"""

one_occ = """
query{{
  allOccupations(uuid:"{uuid}"){{
    edges{{
      node{{
        title,
        description,
        suggestedContacts,
        creditRatingMin,
        creditRatingMax,
        id,
        user{{
          id,
          username
        }}
      }}
    }}
  }}
}}
"""

create_occ = """
mutation{{
  occupationMutate(
    input:{{
      method: "CREATE",
      title:"test-occuation-create",
      user:1,
      description:"Created occupation",
      suggestedContacts:"test",
      creditRatingMin:20,
      creditRatingMax:40
    }}){{
    occupation{{
      uuid,
      title,
      description,
      suggestedContacts,
      creditRatingMin,
      creditRatingMax
    }}
  }}
}}
"""

edit_occ = """
mutation{{
  occupationMutate(
    input:{{
      method: "UPDATE",
      uuid: "{uuid}",
      user: 1,
      title: "Test-2",
      description: "Update test",
      suggestedContacts: "test, test2",
      creditRatingMin: 10,
      creditRatingMax: 15
  }}){{
    occupation{{
      uuid,
      title,
      description,
      suggestedContacts,
      creditRatingMin,
      creditRatingMax,
      user{{
        id,
        username
      }}
    }}
  }}
}}
"""

delete_occ = """
mutation{{
  occupationMutate(
    input:{{
      method: "DELETE",
      uuid: "{uuid}",
      user: 1
    }}){{
    occupation{{
      uuid,
      title,
      description,
      suggestedContacts,
      creditRatingMin,
      creditRatingMax
    }}
  }}
}}
"""

# Mania

all_manias = """
query{
  allManias{
    edges{
      node{
        title,
        uuid
      }
    }
  }
}
"""

one_mania = """
query{{
  allManias(uuid: "{uuid}"){{
    edges{{
      node{{
        title,
        uuid
      }}
    }}
  }}
}}
"""

create_mania = """
mutation{{
  maniaMutate(
    input:{{
      method: "CREATE",
      title: "test-mania",
      description: "sample description"
    }}){{
      mania{{
        uuid
        title
      }}
    }}
}}
"""

edit_mania = """
mutation{{
    maniaMutate(
        input:{{
            method: "UPDATE",
            title: "test-mania2",
            uuid: "{uuid}"
        }}
    ){{
        mania{{
            id,
            uuid,
            title
        }}
   }}
}}
"""

delete_mania = """
mutation{{
    maniaMutate(
        input: {{
            uuid: "{uuid}",
            method: "DELETE"
          }}){{
        mania{{
            id,
            uuid,
            title
        }}
    }}
}}
"""

# Phobias

all_phobias = """
query{
  allPhobias{
    edges{
      node{
        title,
        uuid
      }
    }
  }
}
"""

one_phobia = """
query{{
  allPhobias(uuid: "{uuid}"){{
    edges{{
      node{{
        title,
        uuid
      }}
    }}
  }}
}}
"""

create_phobia = """
mutation{{
  phobiaMutate(
    input:{{
      method: "CREATE",
      title: "test-phobia",
      description: "sample description"
    }}){{
      phobia{{
        uuid
        title
      }}
    }}
}}
"""

edit_phobia = """
mutation{{
    phobiaMutate(
        input:{{
            method: "UPDATE",
            title: "test-phobia2",
            uuid: "{uuid}"
        }}
    ){{
        phobia{{
            id,
            uuid,
            title
        }}
   }}
}}
"""

delete_phobia = """
mutation{{
    phobiaMutate(
        input: {{
            uuid: "{uuid}",
            method: "DELETE"
          }}){{
        phobia{{
            id,
            uuid,
            title
        }}
    }}
}}
"""

# Phobias-Investigator

all_phobias_inv = """
query{
  allPhobiasInv{
    edges{
      node{
        uuid
      }
    }
  }
}
"""

one_phobia_inv = """
{{
  allPhobiasInv(uuid: "{uuid}"){{
    edges{{
      node{{
        uuid
      }}
    }}
  }}
}}
"""

create_phobia_inv = """
mutation{{
  phobiaInvMutate(
    input: {{
      method: "CREATE",
      investigator: "{investigator_uuid}",
      duration: 10,
      phobia: "{phobia_uuid}"
      }})
  {{
    phobiaInv{{
      uuid,
      investigator{{
        name
      }},
      phobia{{
        title
      }},
      duration
    }}
  }}
}}
"""

delete_phobia_inv = """
mutation{{
  phobiaInvMutate(
    input: {{
      method: "DELETE",
      uuid: "{uuid}"
      }})
  {{
    phobiaInv{{
      uuid,
      investigator{{
        name
      }},
      phobia{{
        title
      }},
      duration
    }}
  }}
}}
"""

edit_phobia_inv = """
mutation{{
  phobiaInvMutate(
    input: {{
      method: "UPDATE",
      uuid: "{uuid}",
      investigator: "{investigator_uuid}",
      phobia: "{phobia_uuid}",
      duration: 40
      }})
  {{
    phobiaInv{{
      uuid,
      investigator{{
        name
      }},
      phobia{{
        title
      }},
      duration
    }}
  }}
}}
"""

# Manias-Investigator

all_manias_inv = """
query{
  allManiasInv{
    edges{
      node{
        uuid
      }
    }
  }
}
"""

one_mania_inv = """
{{
  allManiasInv(uuid: "{uuid}"){{
    edges{{
      node{{
        uuid
      }}
    }}
  }}
}}
"""

create_mania_inv = """
mutation{{
  maniaInvMutate(
    input:{{
      method: "CREATE",
      mania: "{mania_uuid}",
      investigator: "{investigator_uuid}",
      duration:10
      }})
  {{
    maniaInv{{
      uuid,
      investigator{{
        name
      }},
      mania{{
        title
      }},
      duration
    }}
  }}
}}
"""

delete_mania_inv = """
mutation{{
  maniaInvMutate(
    input:{{
      method: "DELETE",
      uuid: "{uuid}"
      }})
  {{
    maniaInv{{
      uuid,
      investigator{{
        name
      }},
      mania{{
        title
      }},
      duration
    }}
  }}
}}
"""

edit_mania_inv = """
mutation{{
  maniaInvMutate(
    input:{{
      method: "UPDATE",
      uuid: "{uuid}",
      mania: "{mania_uuid}",
      investigator: "{investigator_uuid}",
      duration:40
      }})
  {{
    maniaInv{{
      uuid,
      investigator{{
        name
      }},
      mania{{
        title
      }},
      duration
    }}
  }}
}}
"""

# Campaigns-Investigator

all_campaigns_inv = """
query{
  allCampaignsInv{
    edges{
      node{
        uuid
      }
    }
  }
}
"""

one_campaign_inv = """
{{
  allCampaignsInv(uuid: "{uuid}"){{
    edges{{
      node{{
        uuid
      }}
    }}
  }}
}}
"""

create_campaign_inv = """
mutation{{
  campaignInvMutate(
    input:{{
      method:"CREATE",
      investigator: "{investigator_uuid}",
      campaign: "{campaign_uuid}"
  }})
  {{
    campaignInv{{
      uuid,
      investigator{{
        uuid
      }},
      timestamp,
      campaign{{
        uuid
      }}
    }}
  }}
}}
"""

delete_campaign_inv = """
mutation{{
  campaignInvMutate(
    input:{{
      method:"DELETE",
      uuid: "{uuid}"
  }})
  {{
    campaignInv{{
      uuid,
      investigator{{
        uuid
      }},
      timestamp,
      campaign{{
        uuid
      }}
    }}
  }}
}}
"""

edit_campaign_inv = """
mutation{{
  campaignInvMutate(
    input:{{
      method:"UPDATE",
      uuid: "{uuid}",
      investigator: "{investigator_uuid}",
      campaign: "{campaign_uuid2}"
  }})
  {{
    campaignInv{{
      uuid,
      investigator{{
        uuid
      }},
      timestamp,
      campaign{{
        uuid
      }}
    }}
  }}
}}
"""

# Inventorys-Investigator

all_inventorys_inv = """
query{
  allInventorysInv{
    edges{
      node{
        uuid
      }
    }
  }
}
"""

one_inventory_inv = """
{{
  allInventorysInv(uuid: "{uuid}"){{
    edges{{
      node{{
        uuid
      }}
    }}
  }}
}}
"""

create_inventory_inv = """
mutation{{
  inventoryInvMutate(input:{{
    method: "CREATE",
    stock: 3,
    investigator: "{investigator_uuid}",
    item: "{item_uuid}"
  }})
  {{
    inventoryInv{{
      investigator{{
        uuid
      }},
      item{{
        uuid
      }},
      stock,
      uuid
    }}
  }}
}}
"""

delete_inventory_inv = """
mutation{{
  inventoryInvMutate(input:{{
    method: "DELETE",
    uuid: "{uuid}"
  }})
  {{
    inventoryInv{{
      investigator{{
        uuid
      }},
      item{{
        uuid
      }},
      stock,
      uuid
    }}
  }}
}}
"""

edit_inventory_inv = """
mutation{{
  inventoryInvMutate(input:{{
    method: "UPDATE",
    stock: 10,
    uuid: "{uuid}",
    investigator: "{investigator_uuid}",
    item: "{item_uuid2}"
  }})
  {{
    inventoryInv{{
      investigator{{
        uuid
      }},
      item{{
        uuid
      }},
      stock,
      uuid
    }}
  }}
}}
"""

# Diarys-Investigator

all_diarys_inv = """
query{
  allDiarysInv{
    edges{
      node{
        uuid
      }
    }
  }
}
"""

one_diary_inv = """
{{
  allDiarysInv(uuid: "{uuid}"){{
    edges{{
      node{{
        uuid
      }}
    }}
  }}
}}
"""

create_diary_inv = """
mutation{{
  diaryInvMutate(input:{{
    method: "CREATE",
    investigator: "{investigator_uuid}",
    title: "test_1",
    notes: "test_1"
  }})
  {{
    diaryInv{{
      investigator{{
        name
      }},
      title,
      notes,
      uuid
    }}
  }}
}}
"""

delete_diary_inv = """
mutation{{
  diaryInvMutate(input:{{
    method: "DELETE",
    uuid: "{uuid}"
  }})
  {{
    diaryInv{{
      investigator{{
        name
      }},
      title,
      notes,
      uuid
    }}
  }}
}}
"""

edit_diary_inv = """
mutation{{
  diaryInvMutate(input:{{
    method: "UPDATE",
    uuid: "{uuid}"
    investigator: "{investigator_uuid}",
    title: "test",
    notes: "test"
  }})
  {{
    diaryInv{{
      investigator{{
        name
      }},
      title,
      notes,
      uuid
    }}
  }}
}}
"""

# Tags-Investigator

all_tags_inv = """
query{
  allTagsInv{
    edges{
      node{
        uuid,
        investigator{
          name
        },
        tag{
          title
        }
      }
    }
  }
}
"""

one_tag_inv = """
{{
  allTagsInv(uuid: "{uuid}"){{
    edges{{
      node{{
        uuid
      }}
    }}
  }}
}}
"""

create_tag_inv = """
mutation{{
  tagInvMutate(
    input:{{
      method: "CREATE",
      investigator: "{investigator_uuid}",
      tag: "{tag_uuid}"
    }})
  {{
    tagInv{{
      uuid
    }}
  }}
}}
"""

delete_tag_inv = """
mutation{{
  tagInvMutate(
    input:{{
      method: "DELETE",
      uuid: "{uuid}",
    }})
  {{
    tagInv{{
      uuid
    }}
  }}
}}
"""

edit_tag_inv = """
mutation{{
  tagInvMutate(
    input:{{
      method: "UPDATE",
      investigator: "{investigator_uuid}",
      tag: "{tag_uuid_2}",
      uuid: "{uuid}"
    }})
  {{
    tagInv{{
      uuid,
      tag{{
        uuid
      }},
      investigator{{
        uuid
      }}
    }}
  }}
}}
"""

# Games

all_games = """
query{
  allGames{
    edges{
      node{
        uuid
      }
    }
  }
}
"""

one_game = """
{{
  allGames(uuid: "{uuid}"){{
    edges{{
      node{{
        uuid
      }}
    }}
  }}
}}
"""

create_game = """
mutation{{
  gameMutate(input:{{
    method: "CREATE",
    title: "test",
    gameType: "1",
    description: "test",
    user: 1
  }})
  {{
    game{{
      uuid,
      title,
      description,
      gameType
    }}
  }}
}}
"""

delete_game = """
mutation{{
  gameMutate(input:{{
    uuid: "{uuid}",
    method: "DELETE",
    user: 1
  }})
  {{
    game{{
      uuid,
      title,
      description,
      gameType
    }}
  }}
}}
"""

edit_game = """
mutation{{
  gameMutate(input:{{
    uuid: "{uuid}",
    method: "UPDATE",
    title: "test_update",
    gameType: "1",
    description: "test",
    user: 1
  }})
  {{
    game{{
      uuid,
      title,
      description,
      gameType
    }}
  }}
}}
"""


