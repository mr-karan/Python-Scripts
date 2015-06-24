import requests,os,bs4

os.makedirs('xkcd',exist_ok=True)

url='http://xkcd.com/'

while url!='http://xkcd.com/#': #Last of XKCD
    print("At : %s" %url)
    res=requests.get(url)
    res.raise_for_status() #If we made a bad request (a 4XX client error or 5XX server error response), we can raise it with Response.raise_for_status():
    soup = bs4.BeautifulSoup(res.text)
    imgelt=soup.select('#content img')
    if len(imgelt)==0:
        print ('Nothing downloaded')
    else:
        imgUrl = imgelt[0].get('src')
        print('Downloading image %s' % (imgUrll))
        res = requests.get(imgUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(imgUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
            imageFile.close()
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')


