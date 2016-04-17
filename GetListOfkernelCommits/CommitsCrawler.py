import requests
from bs4 import BeautifulSoup

def get_scode(page):
    url = 'https://github.com/onano/android_kernel_xiaomi_armani/commits/cm-13.0?page=' + str(page)
    sourcecode = requests.get(url)
    return sourcecode.text


def track_allcommits(max_pages):
    page = 1
    while page <= max_pages:
        soup = BeautifulSoup(get_scode(page), "html.parser")
        for link in soup.findAll('a', {'class': 'message'}):
            href = link.get('href')
            title = link.string
            link = "https://github.com" + href
            print(title)
            #print("https://github.com" + href)
            #track_commit(link)
        page += 1

def track_commit(url):
    source_code = requests.get(url)
    plain_txt = source_code.text
    soup = BeautifulSoup(plain_txt, "html.parser")
    for each_title in soup.findAll('span', {'class': 'user-select-contain'}):
        title = each_title.string
        print(title)

track_allcommits(1)