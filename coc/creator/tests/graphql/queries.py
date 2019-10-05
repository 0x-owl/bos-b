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
                title,
                description,
                defaultValue
            }}
        }}
    }}
}}
"""

create_skill = """
mutation{{
  skillMutate(
    input:{{
      method: "CREATE",
      user: 1,
      title: "Test",
      description: "Created skill",
      defaultValue: 1
    }}){{
    skill{{
      uuid,
      user{{
        username,
        id
      }}
      title,
      description,
      defaultValue
    }}
  }}
}}
"""

edit_skill = """
mutation{{
  skillMutate(
    input:{{
      method: "UPDATE",
      uuid: "{uuid}",
      user: 1,
      title: "Test-2",
      description: "Update test",
      defaultValue: 0
  }}){{
    skill{{
      uuid,
      user{{
        username,
        id
      }}
      title,
      description,
      defaultValue
    }}
  }}
}}
"""

delete_skill = """
mutation{{
  skillMutate(
    input:{{
      uuid: "{uuid}",
      method: "DELETE",
      user: 1
    }}){{
    skill{{
      uuid,
      user{{
        username,
        id
      }}
      title,
      description,
      defaultValue
    }}
  }}
}}
"""

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
        title,
        price,
        description,
        itemType,
        id
      }}
    }}
  }}
}}
"""

search_item = """
{{
  item(id: "{uuid}"){{
    uuid,
    title,
    price,
    description,
    itemType
  }}
}}
"""

create_item = """
mutation{{
  itemMutate(
    input:{{
      user: 1,
      method: "CREATE",
      title: "test-item-create",
      itemType: 2,
      description: "Created item",
      price: 25.6
    }}){{
    item{{
      uuid,
      title,
      itemType,
      description,
      price
    }}
  }}
}}
"""

edit_item = """
mutation{{
  itemMutate(
      input:{{
        user: 1,
        method: "UPDATE",
        uuid: "{uuid}",
        title: "Test-2",
        description: "TestUpdate",
        itemType: 4,
        price: 5
      }}){{
    item{{
      uuid,
      title,
      itemType,
      description,
      price
    }}
  }}
}}
"""

delete_item = """
mutation{{
  itemMutate(
      input:{{
        user: 1,
        method: "DELETE",
        uuid: "{uuid}"
      }}){{
    item{{
      uuid,
      title,
      itemType,
      description,
      price
    }}
  }}
}}
"""

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
