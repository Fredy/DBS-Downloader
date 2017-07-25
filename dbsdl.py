import requests
import re
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://www.supergoku.com/dragon-ball-super-{}-sub-espanol/"
URL2 = "https://www.supergoku.com/dragon-ball-super-capitulo-{}-sub-espanol/"
HEADERS = {'User-agent': 'Mozilla/5.0'}

def decript_url(crip_url):
    page = requests.post("http://www.linkexpander.com/get_url.php",
                         headers=HEADERS,
                         data={'url': crip_url})
    soup = BeautifulSoup(page.content, "html.parser")
    url = soup.find(text=True)
    return url


def range_eps(start, end):
    res = {}
    for i in range(start, end + 1):
        try:
            page = requests.get(URL.format(str(i)), headers=HEADERS)
            if page.status_code == 404:
                # TODO: find a way to replace the url in the original page
                page = requests.get(URL2.format(str(i)), headers=HEADERS)
            if page.status_code == 404:
                res[i] = "ERROR 404"
                pass

            soup = BeautifulSoup(page.content, "html.parser")

            fnd = soup.find("a", string=re.compile("Descargar"))
            if fnd:
                dlurl = fnd.attrs["href"]
                res[i] = decript_url(dlurl)
            else:
                res[i] = "ERROR: Could find the download link."
        except:
            res[i] = "Something gone wrong :("
    return res

def single_eps(eps_num):
    eps_str = str(eps_num)
    page = requests.get(URL.format(eps_str), headers=HEADERS)
    if page.status_code == 404:
        # TODO: find a way to replace the url in the original page
        page = requests.get(URL2.format(eps_str), headers=HEADERS)
    if page.status_code == 404:
        return "ERROR 404"

    soup = BeautifulSoup(page.content, "html.parser")

    fnd = soup.find("a", string=re.compile("Descargar"))
    if fnd:
        dlurl = fnd.attrs["href"]
        return decript_url(dlurl)
    else:
        return "ERROR: Could find the download link."

# TODO: try except inside this function !

pprint(range_eps(68,69))
pprint(single_eps(68))
