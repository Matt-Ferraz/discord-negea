import os
from utils.https_util import get_request
from dotenv import load_dotenv
load_dotenv()

RIOT_URL_LOL = os.getenv('RIOT_URL_LOL')
RIOT_KEY_DEVELOPMENT = os.getenv('RIOT_KEY_DEVELOPMENT')

rotation_route = "platform/v3/champion-rotations"

async def test_url():
    return await get_request(RIOT_URL_LOL + rotation_route + "?api_key=" + RIOT_KEY_DEVELOPMENT)
