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
mutation{
  investigatorMutate(
    input: {
      uuid: "testtesttestuuid", user:1, name: "Test", player: "Test",
      sex: "M", residence: "Capital", birthplace: "Capital", age: 23,
      occupation: 7, ideologies: "prueba", description: "prueba",
      traits: "prueba", injureScars: "prueba", significantPeople:
      "prueba", treasuredPossessions: "prueba",
      encountersWithStrangeEntities: "prueba",
      meaningfulLocations: "prueba", method: "CREATE"
    }){
    investigator{
        uuid,
        name,
        player,
        sex,
        residence,
        birthplace,
        age,
        occupation{
          title
        }
        ideologies,
        description,
        traits,
        meaningfulLocations,
        injureScars,
        significantPeople,
        treasuredPossessions,
        encountersWithStrangeEntities
      }
  }
}

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
mutation{
  skillMutate(
    input:{
      method: "CREATE",
      user: 1,
      title: "Test",
      description: "Created skill",
      defaultValue: 1
    }){
    skill{
      uuid,
      user{
        username,
        id
      }
      title,
      description,
      defaultValue
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
mutation{
  tagMutate(
    input:{
      method: "CREATE",
      title: "test-tag",
      user: 1
    }){
      tag{
        uuid
        title
      }
  }
}
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
mutation{
  itemMutate(
    input:{
      user: 1,
      method: "CREATE",
      title: "test-item-create",
      itemType: 2,
      description: "Created item",
      price: 25.6
    }){
    item{
      uuid,
      title,
      itemType,
      description,
      price
    }
  }
}
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
