from worlds.generic.Rules import set_rule, forbid_item


def set_rules(multiworld, player, girls, starting):
    panties = set()

    for girl in girls:
        panties.add(f"{girl}'s panties")
        if girl not in starting:
            set_rule(multiworld.get_entrance(f"hub-{girl}", player), lambda state: state.has(f"Unlock Girl({girl})", player))

        forbid_item(multiworld.get_location(f"{girl} date 1", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} date 2", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} date 3", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} date 4", player), f"Unlock Girl({girl})", player)

        forbid_item(multiworld.get_location(f"received {girl}'s panties", player), f"Unlock Girl({girl})", player)

        forbid_item(multiworld.get_location(f"{girl}'s Last Name", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl}'s Age", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl}'s Education", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl}'s Height", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl}'s Weight", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl}'s Occupation", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl}'s Cup Size", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl}'s Birthday", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl}'s Hobby", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl}'s Favourite Color", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl}'s Favourite Season", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl}'s Favourite Hangout", player), f"Unlock Girl({girl})", player)

        forbid_item(multiworld.get_location(f"{girl} gift location 1", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 2", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 3", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 4", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 5", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 6", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 7", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 8", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 9", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 10", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 11", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 12", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 13", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 14", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 15", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 16", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 17", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 18", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 19", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 20", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 21", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 22", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 23", player), f"Unlock Girl({girl})", player)
        forbid_item(multiworld.get_location(f"{girl} gift location 24", player), f"Unlock Girl({girl})", player)

    set_rule(multiworld.get_location("boss", player), lambda state: state.has_all(panties, player))