import requests
from . import links

# Bytes that are stored in memory before writing them in disc:
CHUNK_SIZE = 200000000

def download_single(eps_num):
    url = links.single_eps(eps_num)
    if not download_error(eps_num, url):
        downloader(url, name_format(eps_num))

def download_range(start, end):
    # urls is a dictionary with the episode number (int) as key
    # and the link (str) as data
    urls = links.range_eps(start, end)
    for eps, url in urls.items():
        if not download_error(eps, url):
            downloader(url, name_format(eps))

def downloader(url, file_name):
    dwl_request = requests.get(url, stream=True)
    with open(file_name, 'wb') as file_dl:
        for chunk in dwl_request.iter_content(CHUNK_SIZE):
            file_dl.write(chunk)



def name_format(eps_num):
    return '{}.mp4'.format(str(eps_num))

def download_error(eps_num, url):
    if url.split('.')[-1] == "mp4":
        return False
    else:
        with open("errorFile.txt", 'w') as error_file:
            error_file.write(''.join([str(eps_num), ' ', url, '\n']))
        return True
