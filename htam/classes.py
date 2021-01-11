# LICENSE

# Copyright (c) 2020 Cristiano Sansò

# Permission is hereby granted, free of charge,
# to any person obtaining a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



## -------------------- SETUP -------------------- ##



try:
    from random import choice
    from requests import get
    from googlesearch import get_random_user_agent
    from bs4 import BeautifulSoup as bs
    from urllib import parse
except ImportError:
    print('ImportError\nInstalling missing packages...')
    from subprocess import run
    run(['pip', 'install', 'requests'])
    run(['pip', 'install', 'google'])
    run(['pip', 'install', 'beautifulsoup4'])



## -------------------- OEIS -------------------- ##



def _result(table, word):
    try:
        result = ''
        for i in [bs(str(i), 'lxml') for i in table.findAll('tr')]:
            if i.find('td', {'width': '100'}).text == f'\n{word}\n':
                result += i.find('td', {'width': '600'}).text
        if result != '':
            return result[1:-1].strip()
        else:
            return None
    except:
        return None



class OEIS:
    '''search for a sequence on https://oeis.org/
and return any attribute like description, links, comments, etc.\n
if no argument is given for the constructor,
OEIS will return a random sequence from https://oeis.org/'''
    def __init__(self, seq:str = None):
        self.__isvalid = True
        self.__number = 339960

        if seq != None:
            seq = str(int(seq))
            if not 0 < int(seq) < self.__number:
                self.__isvalid = False
            self.__seq = 'A' + '0' * (6 - len(seq)) + seq
            self.__isrand = False
        else:
            self.__seq = str(choice(range(1, self.__number)))
            self.__seq = 'A' + '0' * (6 - len(self.__seq)) + self.__seq
            self.__isrand = True

        self.__url = f'https://oeis.org/search?q={self.__seq}'
        self.__html = bs(get(self.__url, headers = {'User-Agent': str(get_random_user_agent())}).text, 'lxml')
        self.__elem = self.__html.find('p', {'style': 'text-indent: -1em; margin-left: 1em; margin-top: 0; margin-bottom: 0;'})
        self.__table = self.__html.findAll('table')[9]

    def __repr__(self):
        if self.__isrand:
            return f'Random Sequence: {self.__seq}'
        elif self.__isvalid:
            return f'Valid Sequence: {self.__seq}'
        else:
            return f'Invalid Sequence: {self.__seq}'

    # Returning Basic Values
    def isvalid(self):
        return self.__isvalid

    def isrand(self):
        return self.__isrand
        
    def isapproved(self):
        if OEIS(self.__seq[1:]).status() == 'approved':
            return True
        else:
            return False

    def sequence(self):
        return self.__seq

    def url(self):
        return self.__url

    # Sequence Information
    def description(self):
        desc = self.__html.findAll('table')[6]
        try:
            return desc.findAll('td', {'align': 'left'})[1].text.strip()
        except:
            return None

    def terms(self):
        terms = self.__html.findAll('table')[8]
        try:
            for i in terms.find('tt').text.split(', '):
                yield int(i)
        except:
            return None

    def offset(self):
        try:
            return self.__elem.find('tt').text
        except:
            return None

    def comments(self):
        return _result(self.__table, 'COMMENTS')

    def references(self):
        return _result(self.__table, 'REFERENCES')

    def links(self):
        return _result(self.__table, 'LINKS')

    def formula(self):
        return _result(self.__table, 'FORMULA')

    def example(self):
        return _result(self.__table, 'EXAMPLE')

    def mathematica(self):
        return _result(self.__table, 'MATHEMATICA')

    def prog(self):
        return _result(self.__table, 'PROG')

    def crossrefs(self):
        return _result(self.__table, 'CROSSREFS')

    def keyword(self):
        return _result(self.__table, 'KEYWORD')

    def author(self):
        return _result(self.__table, 'AUTHOR')

    def extensions(self):
        return _result(self.__table, 'EXTENSIONS')

    def status(self):
        return _result(self.__table, 'STATUS')



## ------------------- SCHOLAR ------------------- ##



class Scholar:
    def __init__(self, query):
        self.__query = query
        self.__url = f'https://scholar.google.it/scholar?hl=en&as_sdt=0%2C5&q={parse.quote_plus(query)}&btnG=&oq=we'
        self.__html = bs(get(self.__url, headers = {'User-Agent':str(get_random_user_agent())}).text, 'lxml')
        ids = (i['data-cid'] for i in self.__html.findAll('div', {'class':'gs_r gs_or gs_scl'}))
        gs = self.__html.findAll('div', {'class':'gs_fl'})
        a = (i.findAll('a') for i in gs)
        self.__cit = (i[2].text.split()[-1] for i in a if len(i) > 2)
        self.__rel = ('https://scholar.google.it' + i[3]['href'] for i in a if len(i) > 3)
        self.__results = [self.__res(i['href'], i.text, next(self.__rel)) for i in (self.__html.find('a', {'id':i}) for i in ids)]

    def url(self):
        return self.__url

    def results(self):
        return self.__results

    def citations(self):
        return self.__cit

    class __res:
        def __init__(self, url, title, rel = '', cit = '', html = ''):
            self.__url = url
            self.__rel = rel
            self.__cit = cit
            self.__html = html
            self.__title = title
            
        def __scrape(self):
            if self.__html == '':
                self.__html = bs(get(self.__url, headers = {'User-Agent':str(get_random_user_agent())}).text, 'lxml')
        
        def get_html(self):
            if self.__html == '':
                self.__scrape()
            return self.__html

        def get_title(self):
            return self.__title

        def get_url(self):
            return self.__url

        def get_related_url(self):
            return self.__rel

        def get_citations(self):
            return self.__cit