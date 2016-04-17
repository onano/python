import random
import urllib.request

def downLoadImg(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

downLoadImg("https://instagramstatic-a.akamaihd.net/h1/images/homepage/screenshot1.jpg/63c13211f012.jpg")