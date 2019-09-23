all_content = """
query{
  allContents{
    edges{
      node{
        uuid
      }
    }
  }
}
"""

one_content = """
query{{
  allContents(uuid: "{uuid}"){{
    edges{{
      node{{
        uuid
      }}
    }}
  }}
}}
"""

edit_content = """
mutation{{
  contentMutate(input: {{
        description: "test", method: "UPDATE", user: 1, uuid: "{uuid}"}}
    ){{
    content{{
      description,
      title,
      uuid
    }}
  }}
}}
"""

delete_content = """
mutation{{
  contentMutate(input: {{method: "DELETE", uuid: "{uuid}", user: 1}}
    ){{
    content{{
      description,
      title,
      uuid
    }}
  }}
}}
"""

create_content = """
mutation{
  contentMutate(input: {
        description: "test sample",
        method: "CREATE", user: 1, price: 2, title: "test2"})
    {
    content{
      description,
      title,
      uuid
    }
  }
}
"""
