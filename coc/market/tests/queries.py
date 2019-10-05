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
mutation{{
  contentMutate(input: {{
        description: "test sample",
        method: "CREATE", user: 1, price: 2, title: "test2"}})
    {{
    content{{
      description,
      title,
      uuid
    }}
  }}
}}
"""

all_content_tags = """
query{
  allContentTags{
    edges{
      node{
        uuid
        content{
          uuid,
          title,
          user{
            username
          }
        }
        tag{
          uuid,
          title
        }
      }
    }
  }
}
"""

one_content_tag = """
query{{
  allContentTags(uuid:"{uuid}"){{
    edges{{
      node{{
        uuid
        content{{
          uuid,
          title,
          user{{
            username
          }}
        }}
        tag{{
          uuid,
          title
        }}
      }}
    }}
  }}
}}
"""

create_content_tag = """
mutation{{
    contentTagMutate(input:{{
        method: "CREATE",
        content: "{content_uuid}",
        tag: "{tag_uuid}"
    }}){{
        contentTag{{
            uuid
        }}
    }}
}}
"""

edit_content_tag = """
mutation{{
    contentTagMutate(input:{{
        method: "UPDATE",
        content: "{content_uuid}",
        tag: "{tag_uuid_2}",
        uuid: "{uuid}"
    }}){{
        contentTag{{
            uuid,
            content{{
                uuid
            }},
            tag{{
                uuid
            }}
        }}
    }}
}}
"""

delete_content_tag = """
mutation{{
    contentTagMutate(input:{{
        method: "DELETE",
        content: "{content_uuid}",
        tag: "{tag_uuid}",
        uuid: "{uuid}"
    }}){{
        contentTag{{
            uuid,
            content{{
                uuid
            }},
            tag{{
                uuid
            }}
        }}
    }}
}}
"""
