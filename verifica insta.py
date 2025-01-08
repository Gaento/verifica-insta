import urllib
import urllib.error
import urllib.request
from termcolor import colored
try:
    site = urllib.request.urlopen('https://www.instagram.com')
except urllib.error.URLError:
    print(colored('O site instagram não esta acessivel no momento.', 'red'))
else:
    print(colored('Consegui acessar o site instagram com sucesso!', 'green'))