# Content

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

# ContentTag

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

# ContentInv

all_content_invs = """
query{
  allContentInvestigators{
    edges{
      node{
        uuid,
        content{
          title
        },
        inv{
          name,
          uuid
        }
      }
    }
  }
}
"""

one_content_inv = """
query{{
  allContentInvestigators(uuid:"{uuid}"){{
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
        inv{{
          uuid,
          name
        }}
      }}
    }}
  }}
}}
"""

create_content_inv = """
mutation{{
    contentInvestigatorMutate(input:{{
        method: "CREATE",
        content: "{content_uuid}",
        inv: "{inv_uuid}"
    }}){{
        contentInv{{
            uuid
        }}
    }}
}}
"""

edit_content_inv = """
mutation{{
    contentInvestigatorMutate(input:{{
        method: "UPDATE",
        content: "{content_uuid}",
        inv: "{inv_uuid_2}",
        uuid: "{uuid}"
    }}){{
        contentInv{{
            uuid,
            content{{
                uuid
            }},
            inv{{
                uuid
            }}
        }}
    }}
}}
"""

delete_content_inv = """
mutation{{
    contentInvestigatorMutate(input:{{
        method: "DELETE",
        content: "{content_uuid}",
        inv: "{inv_uuid}",
        uuid: "{uuid}"
    }}){{
        contentInv{{
            uuid,
            content{{
                uuid
            }},
            inv{{
                uuid
            }}
        }}
    }}
}}
"""

# ContentItems

all_content_items = """
query{{
  allContentItems{{
    edges{{
      node{{
        uuid,
        content{{
          uuid,
          title
        }},
        item{{
          uuid,
          title,
          user{{
            username
          }}
        }}
      }}
    }}
  }}
}}
"""

one_content_item = """
query{{
  allContentItems(uuid: "{uuid}"){{
    edges{{
      node{{
        uuid,
        content{{
          uuid,
          title
        }},
        item{{
          uuid,
          title,
          user{{
            username
          }}
        }}
      }}
    }}
  }}
}}
"""

all_content_spells = """
query{{
  allContentSpells{{
    edges{{
      node{{
        uuid,
        content{{
          uuid,
          title
        }},
        spell{{
          name,
          alternativeNames,
          uuid
        }}
      }}
    }}
  }}
}}
"""

one_content_spell = """
query{{
  allContentSpells(uuid: "{uuid}"){{
    edges{{
      node{{
        uuid,
        content{{
          uuid,
          title
        }},
        spell{{
          name,
          alternativeNames,
          uuid
        }}
      }}
    }}
  }}
}}
"""

all_content_weapons = """
query{{
  allContentWeapons{{
    edges{{
      node{{
        uuid,
        content{{
          uuid,
          title
        }},
        weapon{{
          uuid,
          title
        }}
      }}
    }}
  }}
}}
"""

one_content_weapon = """
query{{
  allContentWeapons(uuid: "{uuid}"){{
    edges{{
      node{{
        uuid,
        content{{
          uuid,
          title
        }},
        weapon{{
          uuid,
          title
        }}
      }}
    }}
  }}
}}
"""

all_content_manias = """
query{{
  allContentManias{{
    edges{{
      node{{
        uuid,
        content{{
          uuid,
          title
        }},
        mania{{
          uuid,
          title
        }}
      }}
    }}
  }}
}}
"""

one_content_mania = """
query{{
  allContentManias(uuid: "{uuid}"){{
    edges{{
      node{{
        uuid,
        content{{
          uuid,
          title
        }},
        mania{{
          uuid,
          title
        }}
      }}
    }}
  }}
}}
"""

all_content_phobias = """
query{{
  allContentPhobias{{
    edges{{
      node{{
        uuid,
        content{{
          uuid,
          title
        }},
        phobia{{
          uuid,
          title
        }}
      }}
    }}
  }}
}}
"""

one_content_phobia = """
query{{
  allContentPhobias(uuid: "{uuid}"){{
    edges{{
      node{{
        uuid,
        content{{
          uuid,
          title
        }},
        phobia{{
          uuid,
          title
        }}
      }}
    }}
  }}
}}
"""
