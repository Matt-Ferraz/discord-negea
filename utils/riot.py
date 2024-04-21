import os
from utils.https_util import get_request
from dotenv import load_dotenv

load_dotenv()

RIOT_URL_LOL = os.getenv('RIOT_URL_LOL')
RIOT_KEY_DEVELOPMENT = os.getenv('RIOT_KEY_DEVELOPMENT')
rotation_route = "platform/v3/champion-rotations"
CHAMPS_URL = "https://ddragon.leagueoflegends.com/cdn/14.8.1/data/pt_BR/champion.json"
CHAMP_URL = "https://ddragon.leagueoflegends.com/cdn/14.8.1/data/pt_BR/champion/"

async def get_champ_by_name(name):
    return await get_request(CHAMP_URL + name + ".json")

async def test_url():
    return await get_request(RIOT_URL_LOL + rotation_route + "?api_key=" + RIOT_KEY_DEVELOPMENT)

async def get_all_champs():
    return await get_request(RIOT_URL_LOL + rotation_route + "?api_key=" + RIOT_KEY_DEVELOPMENT)