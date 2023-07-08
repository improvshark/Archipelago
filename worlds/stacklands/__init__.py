
from ..AutoWorld import World
from .Options import stacklands_options

client_version = 5

class StacklandsWorld(World):
    game: str = "Stacklands"
    options = stacklands_options