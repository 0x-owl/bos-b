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
    contentInvMutate(input:{{
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
    contentInvMutate(input:{{
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
    contentInvMutate(input:{{
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
query{
  allContentItems{
    edges{
      node{
        uuid,
        item{
          uuid,
          title
        },
        content{
          uuid,
          title
        }
      }
    }
  }
}
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


create_content_item = """
mutation{{
    contentItemMutate(input:{{
        method: "CREATE",
        content: "{content_uuid}",
        item: "{item_uuid}"
    }}){{
        contentItem{{
            uuid
        }}
    }}
}}
"""

edit_content_item = """
mutation{{
    contentItemMutate(input:{{
        method: "UPDATE",
        content: "{content_uuid}",
        item: "{item_uuid_2}",
        uuid: "{uuid}"
    }}){{
        contentItem{{
            uuid,
            content{{
                uuid
            }},
            item{{
                uuid
            }}
        }}
    }}
}}
"""

delete_content_item = """
mutation{{
    contentItemMutate(input:{{
        method: "DELETE",
        content: "{content_uuid}",
        item: "{item_uuid}",
        uuid: "{uuid}"
    }}){{
        contentItem{{
            uuid,
            content{{
                uuid
            }},
            item{{
                uuid
            }}
        }}
    }}
}}
"""

# ContentSpell


all_content_spells = """
query{
  allContentSpells{
    edges{
      node{
        uuid,
        content{
          uuid,
          title
        },
        spell{
          name,
          alternativeNames,
          uuid
        }
      }
    }
  }
}
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

create_content_spell = """
mutation{{
    contentSpellMutate(input:{{
        method: "CREATE",
        content: "{content_uuid}",
        spell: "{spell_uuid}"
    }}){{
        contentSpell{{
            uuid
        }}
    }}
}}
"""

edit_content_spell = """
mutation{{
    contentSpellMutate(input:{{
        method: "UPDATE",
        content: "{content_uuid}",
        spell: "{spell_uuid_2}",
        uuid: "{uuid}"
    }}){{
        contentSpell{{
            uuid,
            content{{
                uuid
            }},
            spell{{
                uuid
            }}
        }}
    }}
}}
"""

delete_content_spell = """
mutation{{
    contentSpellMutate(input:{{
        method: "DELETE",
        content: "{content_uuid}",
        spell: "{spell_uuid}",
        uuid: "{uuid}"
    }}){{
        contentSpell{{
            uuid,
            content{{
                uuid
            }},
            spell{{
                uuid
            }}
        }}
    }}
}}
"""

# ContentWeapons

all_content_weapons = """
query{
  allContentWeapons{
    edges{
      node{
        uuid,
        content{
          uuid,
          title
        },
        weapon{
          uuid,
          title
        }
      }
    }
  }
}
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


create_content_weapon = """
mutation{{
    contentWeaponMutate(input:{{
        method: "CREATE",
        content: "{content_uuid}",
        weapon: "{weapon_uuid}"
    }}){{
        contentWeapon{{
            uuid
        }}
    }}
}}
"""

edit_content_weapon = """
mutation{{
    contentWeaponMutate(input:{{
        method: "UPDATE",
        content: "{content_uuid}",
        weapon: "{weapon_uuid_2}",
        uuid: "{uuid}"
    }}){{
        contentWeapon{{
            uuid,
            content{{
                uuid
            }},
            weapon{{
                uuid
            }}
        }}
    }}
}}
"""

delete_content_weapon = """
mutation{{
    contentWeaponMutate(input:{{
        method: "DELETE",
        content: "{content_uuid}",
        weapon: "{weapon_uuid}",
        uuid: "{uuid}"
    }}){{
        contentWeapon{{
            uuid,
            content{{
                uuid
            }},
            weapon{{
                uuid
            }}
        }}
    }}
}}
"""

# Content Mania

all_content_manias = """
query{
  allContentManias{
    edges{
      node{
        uuid,
        content{
          uuid,
          title
        },
        mania{
          uuid,
          title
        }
      }
    }
  }
}
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

create_content_mania = """
mutation{{
    contentManiaMutate(input:{{
        method: "CREATE",
        content: "{content_uuid}",
        mania: "{mania_uuid}"
    }}){{
        contentMania{{
            uuid
        }}
    }}
}}
"""

edit_content_mania = """
mutation{{
    contentManiaMutate(input:{{
        method: "UPDATE",
        content: "{content_uuid}",
        mania: "{mania_uuid_2}",
        uuid: "{uuid}"
    }}){{
        contentMania{{
            uuid,
            content{{
                uuid
            }},
            mania{{
                uuid
            }}
        }}
    }}
}}
"""

delete_content_mania = """
mutation{{
    contentManiaMutate(input:{{
        method: "DELETE",
        content: "{content_uuid}",
        mania: "{mania_uuid}",
        uuid: "{uuid}"
    }}){{
        contentMania{{
            uuid,
            content{{
                uuid
            }},
            mania{{
                uuid
            }}
        }}
    }}
}}
"""

# ContentPhobia

all_content_phobias = """
query{
  allContentPhobias{
    edges{
      node{
        uuid,
        content{
          uuid,
          title
        },
        phobia{
          uuid,
          title
        }
      }
    }
  }
}
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

create_content_phobia = """
mutation{{
    contentPhobiaMutate(input:{{
        method: "CREATE",
        content: "{content_uuid}",
        phobia: "{phobia_uuid}"
    }}){{
        contentPhobia{{
            uuid
        }}
    }}
}}
"""

edit_content_phobia = """
mutation{{
    contentPhobiaMutate(input:{{
        method: "UPDATE",
        content: "{content_uuid}",
        phobia: "{phobia_uuid_2}",
        uuid: "{uuid}"
    }}){{
        contentPhobia{{
            uuid,
            content{{
                uuid
            }},
            phobia{{
                uuid
            }}
        }}
    }}
}}
"""

delete_content_phobia = """
mutation{{
    contentPhobiaMutate(input:{{
        method: "DELETE",
        content: "{content_uuid}",
        phobia: "{phobia_uuid}",
        uuid: "{uuid}"
    }}){{
        contentPhobia{{
            uuid,
            content{{
                uuid
            }},
            phobia{{
                uuid
            }}
        }}
    }}
}}
"""
