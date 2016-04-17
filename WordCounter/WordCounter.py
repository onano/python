import requests
from bs4 import BeautifulSoup
from collections import Counter
###
# WordCounter: Just Counts the Ocurrences of words
# in a webpage currently used for scraping title
# in xda-developers
#
# For Counting words, Counter from Collections module is used
# link = 'https://docs.python.org/2/library/collections.html#collections.Counter'
# Counter class counts occurences of each word in python
# and returns a list using most_common()
###


def get_words(url):
    source_code = requests.get(url).text
    #Custom Objects!
    soup = BeautifulSoup(source_code,"html.parser")
    cnt = Counter()
    for each_post in soup.findAll('a', {'class': 'threadTitle'}):
        words = each_post.string.lower().split()
        for each_word in words:
            cnt[fix_words(each_word)] += 1
    print(cnt.most_common())

def fix_words(word):
    symbols = '~!@#$%^&*()_+/*-[]+:;?<\'>,."{}\|'
    for alpha in word:
        for sym in symbols:
            if sym is alpha:
                # replace(): returns the string [learn't the hard way]
                word = word.replace(sym, "")

    if len(word) > 0:
        return word

get_words('http://forum.xda-developers.com/redmi-1s/orig-development')