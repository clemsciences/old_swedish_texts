from bs4 import BeautifulSoup

with open('texts/moses.html', 'r') as f:
    b = BeautifulSoup(f.read(), 'html5lib')

print(b.text[1000:2100])
