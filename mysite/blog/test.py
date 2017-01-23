from bs4 import BeautifulSoup

class Inform():
    def __init__(self, html_page):
        self.html_page = html_page
    def links(self):
        lst = []
        soup = BeautifulSoup(self.html_page, 'lxml')
        for link in soup.findAll('a'):
            if "wiki" in link.get('href'):
                lst.append(link.get('href'))
        return lst

if __name__ == '__main__':
    main()
