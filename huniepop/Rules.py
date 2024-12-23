from worlds.generic.Rules import set_rule, forbid_item


def set_rules(multiworld, player, girls, starting):
    panties = set()
<<<<<<< Updated upstream
=======
    
    add_rule(multiworld.get_location("tiffany gift location 1", player),
             lambda state: state.has("academy gift item 1", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 2", player),
             lambda state: state.has("academy gift item 2", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 3", player),
             lambda state: state.has("academy gift item 3", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 4", player),
             lambda state: state.has("academy gift item 4", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 5", player),
             lambda state: state.has("academy gift item 5", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 6", player),
             lambda state: state.has("academy gift item 6", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 7", player),
             lambda state: state.has("rave gift item 1", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 8", player),
             lambda state: state.has("rave gift item 2", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 9", player),
             lambda state: state.has("rave gift item 3", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 10", player),
             lambda state: state.has("rave gift item 4", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 11", player),
             lambda state: state.has("rave gift item 5", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 12", player),
             lambda state: state.has("rave gift item 6", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 13", player),
             lambda state: state.has("scuba gift item 1", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 14", player),
             lambda state: state.has("scuba gift item 2", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 15", player),
             lambda state: state.has("scuba gift item 3", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 16", player),
             lambda state: state.has("scuba gift item 4", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 17", player),
             lambda state: state.has("scuba gift item 5", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 18", player),
             lambda state: state.has("scuba gift item 6", player, 3))
    add_rule(multiworld.get_location("tiffany gift location 19", player),
             lambda state: state.has("tiffany unique item 1", player))
    add_rule(multiworld.get_location("tiffany gift location 20", player),
             lambda state: state.has("tiffany unique item 2", player))
    add_rule(multiworld.get_location("tiffany gift location 21", player),
             lambda state: state.has(f"tiffany unique item 3", player))
    add_rule(multiworld.get_location("tiffany gift location 22", player),
             lambda state: state.has(f"tiffany unique item 4", player))
    add_rule(multiworld.get_location("tiffany gift location 23", player),
             lambda state: state.has(f"tiffany unique item 5", player))
    add_rule(multiworld.get_location("tiffany gift location 24", player),
             lambda state: state.has(f"tiffany unique item 6", player))

    add_rule(multiworld.get_location("aiko gift location 1", player),
             lambda state: state.has("toys gift item 1", player, 3))
    add_rule(multiworld.get_location("aiko gift location 2", player),
             lambda state: state.has("toys gift item 2", player, 3))
    add_rule(multiworld.get_location("aiko gift location 3", player),
             lambda state: state.has("toys gift item 3", player, 3))
    add_rule(multiworld.get_location("aiko gift location 4", player),
             lambda state: state.has("toys gift item 4", player, 3))
    add_rule(multiworld.get_location("aiko gift location 5", player),
             lambda state: state.has("toys gift item 5", player, 3))
    add_rule(multiworld.get_location("aiko gift location 6", player),
             lambda state: state.has("toys gift item 6", player, 3))
    add_rule(multiworld.get_location("aiko gift location 7", player),
             lambda state: state.has("artist gift item 1", player, 3))
    add_rule(multiworld.get_location("aiko gift location 8", player),
             lambda state: state.has("artist gift item 2", player, 3))
    add_rule(multiworld.get_location("aiko gift location 9", player),
             lambda state: state.has("artist gift item 3", player, 3))
    add_rule(multiworld.get_location("aiko gift location 10", player),
             lambda state: state.has("artist gift item 4", player, 3))
    add_rule(multiworld.get_location("aiko gift location 11", player),
             lambda state: state.has("artist gift item 5", player, 3))
    add_rule(multiworld.get_location("aiko gift location 12", player),
             lambda state: state.has("artist gift item 6", player, 3))
    add_rule(multiworld.get_location("aiko gift location 13", player),
             lambda state: state.has("garden gift item 1", player, 3))
    add_rule(multiworld.get_location("aiko gift location 14", player),
             lambda state: state.has("garden gift item 2", player, 3))
    add_rule(multiworld.get_location("aiko gift location 15", player),
             lambda state: state.has("garden gift item 3", player, 3))
    add_rule(multiworld.get_location("aiko gift location 16", player),
             lambda state: state.has("garden gift item 4", player, 3))
    add_rule(multiworld.get_location("aiko gift location 17", player),
             lambda state: state.has("garden gift item 5", player, 3))
    add_rule(multiworld.get_location("aiko gift location 18", player),
             lambda state: state.has("garden gift item 6", player, 3))
    add_rule(multiworld.get_location("aiko gift location 19", player),
             lambda state: state.has("aiko unique item 1", player))
    add_rule(multiworld.get_location("aiko gift location 20", player),
             lambda state: state.has("aiko unique item 2", player))
    add_rule(multiworld.get_location("aiko gift location 21", player),
             lambda state: state.has("aiko unique item 3", player))
    add_rule(multiworld.get_location("aiko gift location 22", player),
             lambda state: state.has("aiko unique item 4", player))
    add_rule(multiworld.get_location("aiko gift location 23", player),
             lambda state: state.has("aiko unique item 5", player))
    add_rule(multiworld.get_location("aiko gift location 24", player),
             lambda state: state.has("aiko unique item 6", player))

    add_rule(multiworld.get_location("kyanna gift location 1", player),
             lambda state: state.has("fitness gift item 1", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 2", player),
             lambda state: state.has("fitness gift item 2", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 3", player),
             lambda state: state.has("fitness gift item 3", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 4", player),
             lambda state: state.has("fitness gift item 4", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 5", player),
             lambda state: state.has("fitness gift item 5", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 6", player),
             lambda state: state.has("fitness gift item 6", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 7", player),
             lambda state: state.has("yoga gift item 1", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 8", player),
             lambda state: state.has("yoga gift item 2", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 9", player),
             lambda state: state.has("yoga gift item 3", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 10", player),
             lambda state: state.has("yoga gift item 4", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 11", player),
             lambda state: state.has("yoga gift item 5", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 12", player),
             lambda state: state.has("yoga gift item 6", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 13", player),
             lambda state: state.has("dancer gift item 1", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 14", player),
             lambda state: state.has("dancer gift item 2", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 15", player),
             lambda state: state.has("dancer gift item 3", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 16", player),
             lambda state: state.has("dancer gift item 4", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 17", player),
             lambda state: state.has("dancer gift item 5", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 18", player),
             lambda state: state.has("dancer gift item 6", player, 3))
    add_rule(multiworld.get_location("kyanna gift location 19", player),
             lambda state: state.has("kyanna unique item 1", player))
    add_rule(multiworld.get_location("kyanna gift location 20", player),
             lambda state: state.has("kyanna unique item 2", player))
    add_rule(multiworld.get_location("kyanna gift location 21", player),
             lambda state: state.has("kyanna unique item 3", player))
    add_rule(multiworld.get_location("kyanna gift location 22", player),
             lambda state: state.has("kyanna unique item 4", player))
    add_rule(multiworld.get_location("kyanna gift location 23", player),
             lambda state: state.has("kyanna unique item 5", player))
    add_rule(multiworld.get_location("kyanna gift location 24", player),
             lambda state: state.has("kyanna unique item 6", player))

    add_rule(multiworld.get_location("audrey gift location 1", player),
             lambda state: state.has("rave gift item 1", player, 3))
    add_rule(multiworld.get_location("audrey gift location 2", player),
             lambda state: state.has("rave gift item 2", player, 3))
    add_rule(multiworld.get_location("audrey gift location 3", player),
             lambda state: state.has("rave gift item 3", player, 3))
    add_rule(multiworld.get_location("audrey gift location 4", player),
             lambda state: state.has("rave gift item 4", player, 3))
    add_rule(multiworld.get_location("audrey gift location 5", player),
             lambda state: state.has("rave gift item 5", player, 3))
    add_rule(multiworld.get_location("audrey gift location 6", player),
             lambda state: state.has("rave gift item 6", player, 3))
    add_rule(multiworld.get_location("audrey gift location 7", player),
             lambda state: state.has("toys gift item 1", player, 3))
    add_rule(multiworld.get_location("audrey gift location 8", player),
             lambda state: state.has("toys gift item 2", player, 3))
    add_rule(multiworld.get_location("audrey gift location 9", player),
             lambda state: state.has("toys gift item 3", player, 3))
    add_rule(multiworld.get_location("audrey gift location 10", player),
             lambda state: state.has("toys gift item 4", player, 3))
    add_rule(multiworld.get_location("audrey gift location 11", player),
             lambda state: state.has("toys gift item 5", player, 3))
    add_rule(multiworld.get_location("audrey gift location 12", player),
             lambda state: state.has("toys gift item 6", player, 3))
    add_rule(multiworld.get_location("audrey gift location 13", player),
             lambda state: state.has("aquarium gift item 1", player, 3))
    add_rule(multiworld.get_location("audrey gift location 14", player),
             lambda state: state.has("aquarium gift item 2", player, 3))
    add_rule(multiworld.get_location("audrey gift location 15", player),
             lambda state: state.has("aquarium gift item 3", player, 3))
    add_rule(multiworld.get_location("audrey gift location 16", player),
             lambda state: state.has("aquarium gift item 4", player, 3))
    add_rule(multiworld.get_location("audrey gift location 17", player),
             lambda state: state.has("aquarium gift item 5", player, 3))
    add_rule(multiworld.get_location("audrey gift location 18", player),
             lambda state: state.has("aquarium gift item 6", player, 3))
    add_rule(multiworld.get_location("audrey gift location 19", player),
             lambda state: state.has("audrey unique item 1", player))
    add_rule(multiworld.get_location("audrey gift location 20", player),
             lambda state: state.has("audrey unique item 2", player))
    add_rule(multiworld.get_location("audrey gift location 21", player),
             lambda state: state.has("audrey unique item 3", player))
    add_rule(multiworld.get_location("audrey gift location 22", player),
             lambda state: state.has("audrey unique item 4", player))
    add_rule(multiworld.get_location("audrey gift location 23", player),
             lambda state: state.has("audrey unique item 5", player))
    add_rule(multiworld.get_location("audrey gift location 24", player),
             lambda state: state.has("audrey unique item 6", player))

    add_rule(multiworld.get_location("lola gift location 1", player),
             lambda state: state.has("sports gift item 1", player, 3))
    add_rule(multiworld.get_location("lola gift location 2", player),
             lambda state: state.has("sports gift item 2", player, 3))
    add_rule(multiworld.get_location("lola gift location 3", player),
             lambda state: state.has("sports gift item 3", player, 3))
    add_rule(multiworld.get_location("lola gift location 4", player),
             lambda state: state.has("sports gift item 4", player, 3))
    add_rule(multiworld.get_location("lola gift location 5", player),
             lambda state: state.has("sports gift item 5", player, 3))
    add_rule(multiworld.get_location("lola gift location 6", player),
             lambda state: state.has("sports gift item 6", player, 3))
    add_rule(multiworld.get_location("lola gift location 7", player),
             lambda state: state.has("baking gift item 1", player, 3))
    add_rule(multiworld.get_location("lola gift location 8", player),
             lambda state: state.has("baking gift item 2", player, 3))
    add_rule(multiworld.get_location("lola gift location 9", player),
             lambda state: state.has("baking gift item 3", player, 3))
    add_rule(multiworld.get_location("lola gift location 10", player),
             lambda state: state.has("baking gift item 4", player, 3))
    add_rule(multiworld.get_location("lola gift location 11", player),
             lambda state: state.has("baking gift item 5", player, 3))
    add_rule(multiworld.get_location("lola gift location 12", player),
             lambda state: state.has("baking gift item 6", player, 3))
    add_rule(multiworld.get_location("lola gift location 13", player),
             lambda state: state.has("scuba gift item 1", player, 3))
    add_rule(multiworld.get_location("lola gift location 14", player),
             lambda state: state.has("scuba gift item 2", player, 3))
    add_rule(multiworld.get_location("lola gift location 15", player),
             lambda state: state.has("scuba gift item 3", player, 3))
    add_rule(multiworld.get_location("lola gift location 16", player),
             lambda state: state.has("scuba gift item 4", player, 3))
    add_rule(multiworld.get_location("lola gift location 17", player),
             lambda state: state.has("scuba gift item 5", player, 3))
    add_rule(multiworld.get_location("lola gift location 18", player),
             lambda state: state.has("scuba gift item 6", player, 3))
    add_rule(multiworld.get_location("lola gift location 19", player),
             lambda state: state.has("lola unique item 1", player))
    add_rule(multiworld.get_location("lola gift location 20", player),
             lambda state: state.has("lola unique item 2", player))
    add_rule(multiworld.get_location("lola gift location 21", player),
             lambda state: state.has("lola unique item 3", player))
    add_rule(multiworld.get_location("lola gift location 22", player),
             lambda state: state.has("lola unique item 4", player))
    add_rule(multiworld.get_location("lola gift location 23", player),
             lambda state: state.has("lola unique item 5", player))
    add_rule(multiworld.get_location("lola gift location 24", player),
             lambda state: state.has("lola unique item 6", player))

    add_rule(multiworld.get_location("nikki gift location 1", player),
             lambda state: state.has("artist gift item 1", player, 3))
    add_rule(multiworld.get_location("nikki gift location 2", player),
             lambda state: state.has("artist gift item 2", player, 3))
    add_rule(multiworld.get_location("nikki gift location 3", player),
             lambda state: state.has("artist gift item 3", player, 3))
    add_rule(multiworld.get_location("nikki gift location 4", player),
             lambda state: state.has("artist gift item 4", player, 3))
    add_rule(multiworld.get_location("nikki gift location 5", player),
             lambda state: state.has("artist gift item 5", player, 3))
    add_rule(multiworld.get_location("nikki gift location 6", player),
             lambda state: state.has("artist gift item 6", player, 3))
    add_rule(multiworld.get_location("nikki gift location 7", player),
             lambda state: state.has("academy gift item 1", player, 3))
    add_rule(multiworld.get_location("nikki gift location 8", player),
             lambda state: state.has("academy gift item 2", player, 3))
    add_rule(multiworld.get_location("nikki gift location 9", player),
             lambda state: state.has("academy gift item 3", player, 3))
    add_rule(multiworld.get_location("nikki gift location 10", player),
             lambda state: state.has("academy gift item 4", player, 3))
    add_rule(multiworld.get_location("nikki gift location 11", player),
             lambda state: state.has("academy gift item 5", player, 3))
    add_rule(multiworld.get_location("nikki gift location 12", player),
             lambda state: state.has("academy gift item 6", player, 3))
    add_rule(multiworld.get_location("nikki gift location 13", player),
             lambda state: state.has("aquarium gift item 1", player, 3))
    add_rule(multiworld.get_location("nikki gift location 14", player),
             lambda state: state.has("aquarium gift item 2", player, 3))
    add_rule(multiworld.get_location("nikki gift location 15", player),
             lambda state: state.has("aquarium gift item 3", player, 3))
    add_rule(multiworld.get_location("nikki gift location 16", player),
             lambda state: state.has("aquarium gift item 4", player, 3))
    add_rule(multiworld.get_location("nikki gift location 17", player),
             lambda state: state.has("aquarium gift item 5", player, 3))
    add_rule(multiworld.get_location("nikki gift location 18", player),
             lambda state: state.has("aquarium gift item 6", player, 3))
    add_rule(multiworld.get_location("nikki gift location 19", player),
             lambda state: state.has("nikki unique item 1", player))
    add_rule(multiworld.get_location("nikki gift location 20", player),
             lambda state: state.has("nikki unique item 2", player))
    add_rule(multiworld.get_location("nikki gift location 21", player),
             lambda state: state.has("nikki unique item 3", player))
    add_rule(multiworld.get_location("nikki gift location 22", player),
             lambda state: state.has("nikki unique item 4", player))
    add_rule(multiworld.get_location("nikki gift location 23", player),
             lambda state: state.has("nikki unique item 5", player))
    add_rule(multiworld.get_location("nikki gift location 24", player),
             lambda state: state.has("nikki unique item 6", player))

    add_rule(multiworld.get_location("jessie gift location 1", player),
             lambda state: state.has("baking gift item 1", player, 3))
    add_rule(multiworld.get_location("jessie gift location 2", player),
             lambda state: state.has("baking gift item 2", player, 3))
    add_rule(multiworld.get_location("jessie gift location 3", player),
             lambda state: state.has("baking gift item 3", player, 3))
    add_rule(multiworld.get_location("jessie gift location 4", player),
             lambda state: state.has("baking gift item 4", player, 3))
    add_rule(multiworld.get_location("jessie gift location 5", player),
             lambda state: state.has("baking gift item 5", player, 3))
    add_rule(multiworld.get_location("jessie gift location 6", player),
             lambda state: state.has("baking gift item 6", player, 3))
    add_rule(multiworld.get_location("jessie gift location 7", player),
             lambda state: state.has("fitness gift item 1", player, 3))
    add_rule(multiworld.get_location("jessie gift location 8", player),
             lambda state: state.has("fitness gift item 2", player, 3))
    add_rule(multiworld.get_location("jessie gift location 9", player),
             lambda state: state.has("fitness gift item 3", player, 3))
    add_rule(multiworld.get_location("jessie gift location 10", player),
             lambda state: state.has("fitness gift item 4", player, 3))
    add_rule(multiworld.get_location("jessie gift location 11", player),
             lambda state: state.has("fitness gift item 5", player, 3))
    add_rule(multiworld.get_location("jessie gift location 12", player),
             lambda state: state.has("fitness gift item 6", player, 3))
    add_rule(multiworld.get_location("jessie gift location 13", player),
             lambda state: state.has("dancer gift item 1", player, 3))
    add_rule(multiworld.get_location("jessie gift location 14", player),
             lambda state: state.has("dancer gift item 2", player, 3))
    add_rule(multiworld.get_location("jessie gift location 15", player),
             lambda state: state.has("dancer gift item 3", player, 3))
    add_rule(multiworld.get_location("jessie gift location 16", player),
             lambda state: state.has("dancer gift item 4", player, 3))
    add_rule(multiworld.get_location("jessie gift location 17", player),
             lambda state: state.has("dancer gift item 5", player, 3))
    add_rule(multiworld.get_location("jessie gift location 18", player),
             lambda state: state.has("dancer gift item 6", player, 3))
    add_rule(multiworld.get_location("jessie gift location 19", player),
             lambda state: state.has("jessie unique item 1", player))
    add_rule(multiworld.get_location("jessie gift location 20", player),
             lambda state: state.has("jessie unique item 2", player))
    add_rule(multiworld.get_location("jessie gift location 21", player),
             lambda state: state.has("jessie unique item 3", player))
    add_rule(multiworld.get_location("jessie gift location 22", player),
             lambda state: state.has("jessie unique item 4", player))
    add_rule(multiworld.get_location("jessie gift location 23", player),
             lambda state: state.has("jessie unique item 5", player))
    add_rule(multiworld.get_location("jessie gift location 24", player),
             lambda state: state.has("jessie unique item 6", player))

    add_rule(multiworld.get_location("beli gift location 1", player),
             lambda state: state.has("yoga gift item 1", player, 3))
    add_rule(multiworld.get_location("beli gift location 2", player),
             lambda state: state.has("yoga gift item 2", player, 3))
    add_rule(multiworld.get_location("beli gift location 3", player),
             lambda state: state.has("yoga gift item 3", player, 3))
    add_rule(multiworld.get_location("beli gift location 4", player),
             lambda state: state.has("yoga gift item 4", player, 3))
    add_rule(multiworld.get_location("beli gift location 5", player),
             lambda state: state.has("yoga gift item 5", player, 3))
    add_rule(multiworld.get_location("beli gift location 6", player),
             lambda state: state.has("yoga gift item 6", player, 3))
    add_rule(multiworld.get_location("beli gift location 7", player),
             lambda state: state.has("sports gift item 1", player, 3))
    add_rule(multiworld.get_location("beli gift location 8", player),
             lambda state: state.has("sports gift item 2", player, 3))
    add_rule(multiworld.get_location("beli gift location 9", player),
             lambda state: state.has("sports gift item 3", player, 3))
    add_rule(multiworld.get_location("beli gift location 10", player),
             lambda state: state.has("sports gift item 4", player, 3))
    add_rule(multiworld.get_location("beli gift location 11", player),
             lambda state: state.has("sports gift item 5", player, 3))
    add_rule(multiworld.get_location("beli gift location 12", player),
             lambda state: state.has("sports gift item 6", player, 3))
    add_rule(multiworld.get_location("beli gift location 13", player),
             lambda state: state.has("garden gift item 1", player, 3))
    add_rule(multiworld.get_location("beli gift location 14", player),
             lambda state: state.has("garden gift item 2", player, 3))
    add_rule(multiworld.get_location("beli gift location 15", player),
             lambda state: state.has("garden gift item 3", player, 3))
    add_rule(multiworld.get_location("beli gift location 16", player),
             lambda state: state.has("garden gift item 4", player, 3))
    add_rule(multiworld.get_location("beli gift location 17", player),
             lambda state: state.has("garden gift item 5", player, 3))
    add_rule(multiworld.get_location("beli gift location 18", player),
             lambda state: state.has("garden gift item 6", player, 3))
    add_rule(multiworld.get_location("beli gift location 19", player),
             lambda state: state.has("beli unique item 1", player))
    add_rule(multiworld.get_location("beli gift location 20", player),
             lambda state: state.has("beli unique item 2", player))
    add_rule(multiworld.get_location("beli gift location 21", player),
             lambda state: state.has("beli unique item 3", player))
    add_rule(multiworld.get_location("beli gift location 22", player),
             lambda state: state.has("beli unique item 4", player))
    add_rule(multiworld.get_location("beli gift location 23", player),
             lambda state: state.has("beli unique item 5", player))
    add_rule(multiworld.get_location("beli gift location 24", player),
             lambda state: state.has("beli unique item 6", player))

    add_rule(multiworld.get_location("kyu gift location 1", player),
             lambda state: state.has("dancer gift item 1", player, 3))
    add_rule(multiworld.get_location("kyu gift location 2", player),
             lambda state: state.has("dancer gift item 2", player, 3))
    add_rule(multiworld.get_location("kyu gift location 3", player),
             lambda state: state.has("dancer gift item 3", player, 3))
    add_rule(multiworld.get_location("kyu gift location 4", player),
             lambda state: state.has("dancer gift item 4", player, 3))
    add_rule(multiworld.get_location("kyu gift location 5", player),
             lambda state: state.has("dancer gift item 5", player, 3))
    add_rule(multiworld.get_location("kyu gift location 6", player),
             lambda state: state.has("dancer gift item 6", player, 3))
    add_rule(multiworld.get_location("kyu gift location 7", player),
             lambda state: state.has("rave gift item 1", player, 3))
    add_rule(multiworld.get_location("kyu gift location 8", player),
             lambda state: state.has("rave gift item 2", player, 3))
    add_rule(multiworld.get_location("kyu gift location 9", player),
             lambda state: state.has("rave gift item 3", player, 3))
    add_rule(multiworld.get_location("kyu gift location 10", player),
             lambda state: state.has("rave gift item 4", player, 3))
    add_rule(multiworld.get_location("kyu gift location 11", player),
             lambda state: state.has("rave gift item 5", player, 3))
    add_rule(multiworld.get_location("kyu gift location 12", player),
             lambda state: state.has("rave gift item 6", player, 3))
    add_rule(multiworld.get_location("kyu gift location 13", player),
             lambda state: state.has("artist gift item 1", player, 3))
    add_rule(multiworld.get_location("kyu gift location 14", player),
             lambda state: state.has("artist gift item 2", player, 3))
    add_rule(multiworld.get_location("kyu gift location 15", player),
             lambda state: state.has("artist gift item 3", player, 3))
    add_rule(multiworld.get_location("kyu gift location 16", player),
             lambda state: state.has("artist gift item 4", player, 3))
    add_rule(multiworld.get_location("kyu gift location 17", player),
             lambda state: state.has("artist gift item 5", player, 3))
    add_rule(multiworld.get_location("kyu gift location 18", player),
             lambda state: state.has("artist gift item 6", player, 3))
    add_rule(multiworld.get_location("kyu gift location 19", player),
             lambda state: state.has("kyu unique item 1", player))
    add_rule(multiworld.get_location("kyu gift location 20", player),
             lambda state: state.has("kyu unique item 2", player))
    add_rule(multiworld.get_location("kyu gift location 21", player),
             lambda state: state.has("kyu unique item 3", player))
    add_rule(multiworld.get_location("kyu gift location 22", player),
             lambda state: state.has("kyu unique item 4", player))
    add_rule(multiworld.get_location("kyu gift location 23", player),
             lambda state: state.has("kyu unique item 5", player))
    add_rule(multiworld.get_location("kyu gift location 24", player),
             lambda state: state.has("kyu unique item 6", player))

    add_rule(multiworld.get_location("momo gift location 1", player),
             lambda state: state.has("aquarium gift item 1", player, 3))
    add_rule(multiworld.get_location("momo gift location 2", player),
             lambda state: state.has("aquarium gift item 2", player, 3))
    add_rule(multiworld.get_location("momo gift location 3", player),
             lambda state: state.has("aquarium gift item 3", player, 3))
    add_rule(multiworld.get_location("momo gift location 4", player),
             lambda state: state.has("aquarium gift item 4", player, 3))
    add_rule(multiworld.get_location("momo gift location 5", player),
             lambda state: state.has("aquarium gift item 5", player, 3))
    add_rule(multiworld.get_location("momo gift location 6", player),
             lambda state: state.has("aquarium gift item 6", player, 3))
    add_rule(multiworld.get_location("momo gift location 7", player),
             lambda state: state.has("toys gift item 1", player, 3))
    add_rule(multiworld.get_location("momo gift location 8", player),
             lambda state: state.has("toys gift item 2", player, 3))
    add_rule(multiworld.get_location("momo gift location 9", player),
             lambda state: state.has("toys gift item 3", player, 3))
    add_rule(multiworld.get_location("momo gift location 10", player),
             lambda state: state.has("toys gift item 4", player, 3))
    add_rule(multiworld.get_location("momo gift location 11", player),
             lambda state: state.has("toys gift item 5", player, 3))
    add_rule(multiworld.get_location("momo gift location 12", player),
             lambda state: state.has("toys gift item 6", player, 3))
    add_rule(multiworld.get_location("momo gift location 13", player),
             lambda state: state.has("sports gift item 1", player, 3))
    add_rule(multiworld.get_location("momo gift location 14", player),
             lambda state: state.has("sports gift item 2", player, 3))
    add_rule(multiworld.get_location("momo gift location 15", player),
             lambda state: state.has("sports gift item 3", player, 3))
    add_rule(multiworld.get_location("momo gift location 16", player),
             lambda state: state.has("sports gift item 4", player, 3))
    add_rule(multiworld.get_location("momo gift location 17", player),
             lambda state: state.has("sports gift item 5", player, 3))
    add_rule(multiworld.get_location("momo gift location 18", player),
             lambda state: state.has("sports gift item 6", player, 3))
    add_rule(multiworld.get_location("momo gift location 19", player),
             lambda state: state.has("momo unique item 1", player))
    add_rule(multiworld.get_location("momo gift location 20", player),
             lambda state: state.has("momo unique item 2", player))
    add_rule(multiworld.get_location("momo gift location 21", player),
             lambda state: state.has("momo unique item 3", player))
    add_rule(multiworld.get_location("momo gift location 22", player),
             lambda state: state.has("momo unique item 4", player))
    add_rule(multiworld.get_location("momo gift location 23", player),
             lambda state: state.has("momo unique item 5", player))
    add_rule(multiworld.get_location("momo gift location 24", player),
             lambda state: state.has("momo unique item 6", player))

    add_rule(multiworld.get_location("celeste gift location 1", player),
             lambda state: state.has("scuba gift item 1", player, 3))
    add_rule(multiworld.get_location("celeste gift location 2", player),
             lambda state: state.has("scuba gift item 2", player, 3))
    add_rule(multiworld.get_location("celeste gift location 3", player),
             lambda state: state.has("scuba gift item 3", player, 3))
    add_rule(multiworld.get_location("celeste gift location 4", player),
             lambda state: state.has("scuba gift item 4", player, 3))
    add_rule(multiworld.get_location("celeste gift location 5", player),
             lambda state: state.has("scuba gift item 5", player, 3))
    add_rule(multiworld.get_location("celeste gift location 6", player),
             lambda state: state.has("scuba gift item 6", player, 3))
    add_rule(multiworld.get_location("celeste gift location 7", player),
             lambda state: state.has("academy gift item 1", player, 3))
    add_rule(multiworld.get_location("celeste gift location 8", player),
             lambda state: state.has("academy gift item 2", player, 3))
    add_rule(multiworld.get_location("celeste gift location 9", player),
             lambda state: state.has("academy gift item 3", player, 3))
    add_rule(multiworld.get_location("celeste gift location 10", player),
             lambda state: state.has("academy gift item 4", player, 3))
    add_rule(multiworld.get_location("celeste gift location 11", player),
             lambda state: state.has("academy gift item 5", player, 3))
    add_rule(multiworld.get_location("celeste gift location 12", player),
             lambda state: state.has("academy gift item 6", player, 3))
    add_rule(multiworld.get_location("celeste gift location 13", player),
             lambda state: state.has("fitness gift item 1", player, 3))
    add_rule(multiworld.get_location("celeste gift location 14", player),
             lambda state: state.has("fitness gift item 2", player, 3))
    add_rule(multiworld.get_location("celeste gift location 15", player),
             lambda state: state.has("fitness gift item 3", player, 3))
    add_rule(multiworld.get_location("celeste gift location 16", player),
             lambda state: state.has("fitness gift item 4", player, 3))
    add_rule(multiworld.get_location("celeste gift location 17", player),
             lambda state: state.has("fitness gift item 5", player, 3))
    add_rule(multiworld.get_location("celeste gift location 18", player),
             lambda state: state.has("fitness gift item 6", player, 3))
    add_rule(multiworld.get_location("celeste gift location 19", player),
             lambda state: state.has("celeste unique item 1", player))
    add_rule(multiworld.get_location("celeste gift location 20", player),
             lambda state: state.has("celeste unique item 2", player))
    add_rule(multiworld.get_location("celeste gift location 21", player),
             lambda state: state.has("celeste unique item 3", player))
    add_rule(multiworld.get_location("celeste gift location 22", player),
             lambda state: state.has("celeste unique item 4", player))
    add_rule(multiworld.get_location("celeste gift location 23", player),
             lambda state: state.has("celeste unique item 5", player))
    add_rule(multiworld.get_location("celeste gift location 24", player),
             lambda state: state.has("celeste unique item 6", player))

    add_rule(multiworld.get_location("venus gift location 1", player),
             lambda state: state.has("academy gift item 1", player, 3))
    add_rule(multiworld.get_location("venus gift location 2", player),
             lambda state: state.has("academy gift item 2", player, 3))
    add_rule(multiworld.get_location("venus gift location 3", player),
             lambda state: state.has("academy gift item 3", player, 3))
    add_rule(multiworld.get_location("venus gift location 4", player),
             lambda state: state.has("academy gift item 4", player, 3))
    add_rule(multiworld.get_location("venus gift location 5", player),
             lambda state: state.has("academy gift item 5", player, 3))
    add_rule(multiworld.get_location("venus gift location 6", player),
             lambda state: state.has("academy gift item 6", player, 3))
    add_rule(multiworld.get_location("venus gift location 7", player),
             lambda state: state.has("rave gift item 1", player, 3))
    add_rule(multiworld.get_location("venus gift location 8", player),
             lambda state: state.has("rave gift item 2", player, 3))
    add_rule(multiworld.get_location("venus gift location 9", player),
             lambda state: state.has("rave gift item 3", player, 3))
    add_rule(multiworld.get_location("venus gift location 10", player),
             lambda state: state.has("rave gift item 4", player, 3))
    add_rule(multiworld.get_location("venus gift location 11", player),
             lambda state: state.has("rave gift item 5", player, 3))
    add_rule(multiworld.get_location("venus gift location 12", player),
             lambda state: state.has("rave gift item 6", player, 3))
    add_rule(multiworld.get_location("venus gift location 13", player),
             lambda state: state.has("scuba gift item 1", player, 3))
    add_rule(multiworld.get_location("venus gift location 14", player),
             lambda state: state.has("scuba gift item 2", player, 3))
    add_rule(multiworld.get_location("venus gift location 15", player),
             lambda state: state.has("scuba gift item 3", player, 3))
    add_rule(multiworld.get_location("venus gift location 16", player),
             lambda state: state.has("scuba gift item 4", player, 3))
    add_rule(multiworld.get_location("venus gift location 17", player),
             lambda state: state.has("scuba gift item 5", player, 3))
    add_rule(multiworld.get_location("venus gift location 18", player),
             lambda state: state.has("scuba gift item 6", player, 3))
    add_rule(multiworld.get_location("venus gift location 19", player),
             lambda state: state.has("venus unique item 1", player))
    add_rule(multiworld.get_location("venus gift location 20", player),
             lambda state: state.has("venus unique item 2", player))
    add_rule(multiworld.get_location("venus gift location 21", player),
             lambda state: state.has("venus unique item 3", player))
    add_rule(multiworld.get_location("venus gift location 22", player),
             lambda state: state.has("venus unique item 4", player))
    add_rule(multiworld.get_location("venus gift location 23", player),
             lambda state: state.has("venus unique item 5", player))
    add_rule(multiworld.get_location("venus gift location 24", player),
             lambda state: state.has("venus unique item 6", player))
>>>>>>> Stashed changes

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