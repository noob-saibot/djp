from bs4 import BeautifulSoup

class Inform():
    def __init__(self, html_page, lst=[]):
        self.html_page = html_page
        self.lst = lst
    def links(self):
        soup = BeautifulSoup(self.html_page, 'lxml')
        for link in soup.findAll('a'):
            self.lst.append(link.get('href'))
        return self.lst

if __name__ == '__main__':
    main()
