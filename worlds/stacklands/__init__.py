from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld
from .Options import stacklands_options

client_version = 5


class StackLandsWebworld(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up the Archipelago Stacklands game on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["improvshark"]
    )]


class StacklandsWorld(World):
    """
    Stacklands is a card game where everything is an in-game stack.
    """
    game: str = "Stacklands"
    topology_present = False
    web = StackLandsWebworld()
    data_version = 1

    option_definitions = stacklands_options
    item_name_to_id = {}
    location_name_to_id = {}
