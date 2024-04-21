import requests

async def get_request(url: str) -> object:
    if url.__len__ == 0:
        return {}
    
    print(url)
    res = requests.get(url)

    return res.text