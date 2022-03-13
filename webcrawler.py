import os
import threading
import requests
from bs4 import BeautifulSoup
import nltk

# thread crawl
# get a top world from a frequency list.
# get x amount of result, and their webpage data.
# check full domain to remove duplicates.
# parse page data, remove non relevant words. make a library of word frequency. dog=0.03;
# store data in a file.
# Repeate.


def random_word_selector():
    

    request(random_word)


def request(current_word):
    r = requests.get('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=' + current_word +'&btnG=')

    if r.status_code == 200:
        r.text
        soup = BeautifulSoup(r.text, 'html.parser')
        #print(soup.title)
        # Subdomains
        ## Cycles through all the h3 (where the articles are)
        for link in soup.find_all('h3'):
            ## Gets article link.
            print(link.a.get('href'))

        #print(soup.prettify())
    else:
        print(r.status_code)


def index():


def test(word):
    request(word)


test("Finasteride")


