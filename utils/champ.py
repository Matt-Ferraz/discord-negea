def format_spells(spells, name):
    formated_dict = {}
    for spell in spells:
        key_by_spell_keybind = spell['id'].replace(name, '').upper()
        formated_dict[key_by_spell_keybind] = {
            'name': spell['name'],
            'desc': spell['description'],
            'image_url': "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/spell/" +spell['image']['full']
        }

    return formated_dict

def format_champ_data(raw, name):
    formatted = {
        'passive_name': raw['passive']['name'],
        'passive_desc': raw['passive']['description'],
        'title': raw['title'],
        'name': name,
        'image_url': raw['image']['full'],
        'spells': format_spells(raw['spells'], name)
    }

    return formatted
