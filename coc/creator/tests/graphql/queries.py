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
    allInvestigators(uuid: "{investigator}"){{
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
