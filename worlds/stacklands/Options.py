from typing import Dict
from Options import Choice, Option, Toggle, Range

class AmountOfCoins(Range):
    """How many Coins to give."""
    range_start = 1
    range_end = 100
    default = 10

stacklands_options: Dict[str, type(Option)] = {
    "give_coin": AmountOfCoins,
}