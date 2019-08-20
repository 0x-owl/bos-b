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
