from BaseClasses import Item
from typing import NamedTuple, Dict, Optional

class ItemData(NamedTuple):
    code: Optional[int]
    progression: bool

item_table: Dict[str, ItemData] = {
    "Coin": ItemData(1,False)
}

item_frequencies = {
    "Coin": 50
}

lookup_id_to_name: Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}