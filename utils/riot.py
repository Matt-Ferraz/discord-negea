import os
from dotenv import load_dotenv
load_dotenv()

RIOT_URL_LOL = os.getenv('RIOT_URL_LOL')
RIOT_KEY_DEVELOPMENT = os.getenv('RIOT_KEY_DEVELOPMENT')

rotation_route = "platform/v3/champion-rotations"


def test_url():
    print(RIOT_URL_LOL + rotation_route + "?api_url=" + RIOT_KEY_DEVELOPMENT)
