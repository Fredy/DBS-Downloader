import requests
from . import links

# Bytes that are stored in memory before writing them in disc:
CHUNK_SIZE = 200000000

def download_single(eps_num):
    url = links.single_eps(eps_num)
    r = requests.get(url, stream=True)
    with open('{}.mp4'.format(str(eps_num)), 'wb') as file_dl:
        for chunk in r.iter_content(CHUNK_SIZE):
            file_dl.write(chunk)
