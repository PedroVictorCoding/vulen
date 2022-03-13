import os
import re
import requests
from bs4 import BeautifulSoup
import nltk
import sqlite3

# thread crawl
# get a top world from a frequency list.
# get x amount of result, and their webpage data.
# check full domain to remove duplicates.
# parse page data, remove non relevant words. make a library of word frequency. dog=0.03;
# store data in a file.
# Repeate.


def random_word_selector():
    

    request(random_word)

#for getting scholar.google.com search subdomains
def request(current_word):
    r = requests.get('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=' + current_word +'&btnG=')

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        #print(soup.title)
        # Subdomains
        ## Cycles through all the h3 (where the articles are)
        list_of_links = []
        for link in soup.find_all('h3'):
            ## Gets article link.
            print(link.a.get('href'))
            index(link.a.get('href'))

        #print(soup.prettify())
    else:
        print(r.status_code)


def index(url_to_index):
    connection = sqlite3.connect("indexer.db")
    crsr = connection.cursor()
    print("Connected to the db.")

    if url_to_index.endswith(".pdf") or url_to_index.endswith(".pdf/"):
        pass
    else:
        r = requests.get(url_to_index)

        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            print("Title: " + soup.title.text)

            #abstract_data1 = soup.find("meta", name="citation_abstract")
            #print(abstract_data.get('content'))

            abstract_data = soup.find("meta", property="og:description")

            print(url_to_index)
                
            print("Abstract: " + abstract_data.get('content'))

            authors_data = ""
            for author in soup.find_all("dc.creator"):
                authors_data = authors_data + ", " + author.get('content')
                
            print(authors_data)


            sql_command = "INSERT INTO domains (website_url, abstract, url_title)\n VALUES ('" + url_to_index +  "', '" + abstract_data.get('content') + "', '" + soup.title.text + "')"

            crsr.execute(sql_command)
            connection.commit()

            exit()


        else:
            print(r.status_code)

        

        sql_command = """SELECT * from domains"""
        crsr.execute(sql_command)
        connection.commit()



    connection.close()
    print("Connection closed.")
    

def test(word):
    request(word)


test("Finasteride")


# title
# language : get from scholar search url.
# main text : maybe search for asbtract in bs4; cleaned with nltk
# author : search for author in bs4
