from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


list_spells = ["Q", "W", "E", "R"]

def format_spells(spells, name):
    formated_dict = {}
    count = 0
    for spell in spells:
            spell_name = spell["name"]
            spell_description = strip_tags(spell["description"])
            spell_tooltip = spell["tooltip"]
            spell_max_rank = spell["maxrank"]
            spell_cooldowns = spell["cooldown"]
            spell_costs = spell["cost"]
            spell_range = spell["range"]

            formated_dict[list_spells[count]] = {
                "description": spell_description,
                "tooltip": spell_tooltip,
                "max_rank": spell_max_rank,
                "cooldowns": spell_cooldowns,
                "costs": spell_costs,
                "range": spell_range
            }
            count+=1

    # Printing spell information
    # for spell_name, spell_info in formated_dict.items():
    #     print(f"Spell Name: {spell_name}")
    #     print(f"Description: {spell_info['description']}")
    #     print(f"Tooltip: {spell_info['tooltip']}")
    #     print(f"Max Rank: {spell_info['max_rank']}")
    #     print(f"Cooldowns: {spell_info['cooldowns']}")
    #     print(f"Costs: {spell_info['costs']}")
    #     print(f"Range: {spell_info['range']}")
    #     print("\n")

    return formated_dict

def format_champ_data(raw, name):
    formatted = {
        'passive_name': raw['passive']['name'],
        'passive_desc': strip_tags(raw['passive']['description']),
        'title': raw['title'] + "\n",
        'name': name,
        'image_url': raw['image']['full'],
        'spells': format_spells(raw['spells'], name)
    }

    return formatted
