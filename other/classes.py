# Setup
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
    run(['pip', 'install', 'urllib'])



###############################
#                             #
#            OEIS             #
#                             #
###############################



class OEIS:
    '''search for a sequence on https://oeis.org/
and return any attribute like description, links, comments, etc.\n
if no argument is given for the constructor,
OEIS will return a random sequence from https://oeis.org/'''
    def __init__(self, seq:str = None):
        self.__isvalid = True
        self.__number = 339920

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
        self.__html = bs(get(self.__url, headers = {'user_agent': get_random_user_agent()}).text, 'lxml')
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
    def __result(self, word):
        try:
            result = ''
            for i in [bs(str(i), 'lxml') for i in self.__table.findAll('tr')]:
                if i.find('td', {'width': '100'}).text == f'\n{word}\n':
                    result += i.find('td', {'width': '600'}).text
            if result != '':
                return result[1:-1].strip()
            else:
                return None
        except:
            return None

    def description(self):
        desc = self.__html.findAll('table')[6]
        try:
            desc = '\n'.join(i for i in desc.findAll('td', {'align': 'left'})[1].text.split('\n') if i != '')
            return desc.replace('  ', '').split('(Formerly')[0].rstrip()
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
        return OEIS(self.__seq[1:]).__result('COMMENTS')

    def references(self):
        return OEIS(self.__seq[1:]).__result('REFERENCES')

    def links(self):
        return OEIS(self.__seq[1:]).__result('LINKS')

    def formula(self):
        return OEIS(self.__seq[1:]).__result('FORMULA')

    def example(self):
        return OEIS(self.__seq[1:]).__result('EXAMPLE')

    def mathematica(self):
        return OEIS(self.__seq[1:]).__result('MATHEMATICA')

    def prog(self):
        return OEIS(self.__seq[1:]).__result('PROG')

    def crossrefs(self):
        return OEIS(self.__seq[1:]).__result('CROSSREFS')

    def keyword(self):
        return OEIS(self.__seq[1:]).__result('KEYWORD')

    def author(self):
        return OEIS(self.__seq[1:]).__result('AUTHOR')

    def extensions(self):
        return OEIS(self.__seq[1:]).__result('EXTENSIONS')

    def status(self):
        return OEIS(self.__seq[1:]).__result('STATUS')


################################
#                              #
#           WOLFRAM            #
#                              #
################################



def _result(results, word):
    try:
        return results[word]
    except:
        return None

class Wolfram:
    '''Performs a search on https://www.wolframalpha.com/ \n
You can get almost any search's result or information.\n
So far you can't get images and plots but maybe I'll add the possibility to get the images and plots' urls'''
    def __init__(self, code:str):
        self.__code = code
        self.__appid = 'HQ5Y8A-2YGXW93GQ8'
        self.__query = parse.quote_plus(self.__code)
        self.__url = f"http://api.wolframalpha.com/v2/query?" \
                     f"appid={self.__appid}" \
                     f"&input={self.__query}" \
                     f"&format=plaintext" \
                     f"&output=json"
        self.__json = get(self.__url).json()
        try:
            self.__pods = self.__json['queryresult']['pods']
            self.__results = {self.__pods[i]['title']:self.__pods[i]['subpods'][0]['plaintext'] for i in range(len(self.__pods))}
        except:
            self.__pods = None
            self.__results = None

    # General Informations
    def timing(self):
        return self.__json['queryresult']['timing']

    def id(self):
        return self.__json['queryresult']['id']

    def host(self):
        return self.__json['queryresult']['host']

    def server(self):
        return self.__json['queryresult']['server']

    def related(self):
        return self.__json['queryresult']['related']

    def version(self):
        return self.__json['queryresult']['version']

    def error(self):
        return self.__json['queryresult']['error']

    def success(self):
        return self.__json['queryresult']['success']


    # Attributes
    def first_result(self):
        return list(self.__results.keys())[1]

    def alternate_scientific_names(self):
        return _result(self.__results, 'Alternate scientific names')

    def basic_information(self):
        return _result(self.__results, 'Basic information')

    def binary_form(self):
        return _result(self.__results, 'Binary form')

    def biological_properties(self):
        return _result(self.__results, 'Biological properties')

    def character_code(self):
        inp = self.__results['Input']
        return _result(self.__results, f'Character code {inp}')

    def definite_integral(self):
        return _result(self.__results, f'Definite integral')

    def derivative(self):
        return _result(self.__results, f'Derivative')

    def indefinite_integral(self):
        return _result(self.__results, f'Inefinite integral')

    def genome_information(self):
        return _result(self.__results, 'Genome information')

    def input(self):
        return _result(self.__results, 'Input')

    def input_interpretation(self):
        return _result(self.__results, 'Input interpretation')

    def notable_facts(self):
        return _result(self.__results, 'Notable facts')

    def number_name(self):
        return _result(self.__results, 'Number name')

    def physical_characteristics(self):
        return _result(self.__results, 'Physical characteristics')
        
    def response(self):
        return _result(self.__results, 'Response')
        
    def result(self):
        return _result(self.__results, 'Result')

    def roman_numerals(self):
        return _result(self.__results, 'Roman numerals')
        
    def scientific_name(self):
        return _result(self.__results, 'Scientific name')

    def solution(self):
        return _result(self.__results, 'Solution')

    def solutions(self):
        return _result(self.__results, 'Solutions')
        
    def species_authority(self):
        return _result(self.__results, 'Species authority')

    def taxonomy(self):
        return _result(self.__results, 'Taxonomy')

    def wikipedia_summary(self):
        return _result(self.__results, 'Wikipedia summary')

a = Wolfram(r'dy/dx = 3y + 2(dy/dx)^2')
print(a.first_result())