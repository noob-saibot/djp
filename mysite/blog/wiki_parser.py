from grab import Grab
from bs4 import BeautifulSoup

class Inform():
    def __init__(self, html_page):
        self.html_page = html_page
    def links(self):
        dct = {}
        soup = BeautifulSoup(self.html_page, 'lxml')
        for link in soup.findAll('a'):
            if "wiki" in link.get('href'):
                dct[link.get('href')] = self.travel(link.get('href'))
        return dct
    def travel(self, url):
        g= Grab()
        g.go(url)
        try:
            return g.doc.select('//div[@class="mw-content-ltr"]/p[1]').html().replace('/wiki/', 'https://en.wikipedia.org/wiki/')
        except:
            return ""
if __name__ == '__main__':
    main()
