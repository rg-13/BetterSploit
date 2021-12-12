import requests
from bs4 import BeautifulSoup
import re
import csv
import time
import json
import sqlite3


class EmailExtractor:
    def __init__(self, keyword):
        self.keyword = keyword
        self.emails = []
        self.search_engines = ['google', 'bing', 'yahoo']
        self.search_engines_urls = ['https://www.google.com/search?q=', 'https://www.bing.com/search?q=', 'https://search.yahoo.com/search?p=']
        self.search_engines_urls_end = ['&ei=UTF-8&start=0&sa=N&filter=0', '&start=0&sa=N&filter=0', '&p=0']


    def get_emails(self):

        for i in range(len(self.search_engines)):
            url = self.search_engines_urls[i] + self.keyword + self.search_engines_urls_end[i]
            emails = self.get_emails_from_search_engine(url, self.search_engines[i])
            self.emails.extend(emails)
        self.emails = list(set(self.emails))
        self.write_emails_to_file()

    def get_emails_from_search_engine(self, url, search_engine):

        emails = []
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        if search_engine == 'google':
            emails = self.get_emails_from_google(soup)
        elif search_engine == 'bing':
            emails = self.get_emails_from_bing(soup)
        elif search_engine == 'yahoo':
            emails = self.get_emails_from_yahoo(soup)
        return emails

    def get_emails_from_google(self, soup):
        emails = []
        for link in soup.find_all('a'):
            if 'href' in link.attrs:
                url = link.attrs['href']
                if url.startswith('mailto:'):
                    emails.append(url[7:])
        return emails

    def get_emails_from_bing(self, soup):
            emails = []
            for link in soup.find_all('a'):
                if 'href' in link.attrs:
                    url = link.attrs['href']
                    if url.startswith('mailto:'):
                        emails.append(url[7:])
            return emails

    def get_emails_from_yahoo(self, soup):
            emails = []
            for link in soup.find_all('a'):
                if 'href' in link.attrs:
                    url = link.attrs['href']
                    if url.startswith('mailto:'):
                        emails.append(url[7:])
            return emails

    def write_emails_to_file(self):
            with open('emails.txt', 'w') as f:
                for email in self.emails:
                    f.write(email + '\n')

    def write_emails_to_database(self):
                conn = sqlite3.connect('emails.db')
                c = conn.cursor()
                c.execute('CREATE TABLE IF NOT EXISTS emails (email TEXT)')
                for email in self.emails:
                    c.execute('INSERT INTO emails (email) VALUES (?)', (email,))
                conn.commit()
                conn.close()

    def write_emails_to_csv(self):
        with open('emails.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['email'])
            for email in self.emails:
                writer.writerow([email])

    def write_emails_to_json(self):            
        with open('emails.json', 'w') as f:
            json.dump(self.emails, f)