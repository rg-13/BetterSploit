#Adversary Hunting Tool for DarkSearch
#RG13.

import requests, sys, os, time, random, argparse, re, json, urllib3, threading, socket, ssl, urllib, urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse, urllib.robotparser
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.parse import urlparse

class darksearch:
    def __init__(self):
        self.headers = []
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
        self.url = ""
        self.urls_found = []
        self.headers = [""
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"\
        "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0",
        "Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3",
        "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0"]


    def random_header(self):
        return {'User-Agent': random.choice(self.headers)}

    def rotate_headers(self):
        self.headers.append(self.headers.pop(0))
        
    def get_urls_from_file(self, filename):
        with open(filename) as f:
            for line in f:
                self.urls_found.append(line.strip())

    def get_urls_from_file_json(self, filename):
        with open(filename) as f:
            self.urls_found = json.load(f)
  
    def match_urls_from_file(self, searchTerm, url_file):
        self.urls_found = []
        self.get_urls_from_file_json(url_file)
        if len(self.urls_found) > 0:
            self.get_urls(searchTerm)
            if len(self.urls_found) > 0:
                for url in self.urls_found:
                    if searchTerm in url:
                        self.urls_found.append(url)
                self.write_urls_json(url_file)  # write urls to file
                print("[*] Total Matches: " + str(len(self.urls_found)))
        else:   
            print("[!] No URLs found.")


    def get_urls(self, searchTerm):
        print("[*] Searching for: " + searchTerm)
        self.url = " https://darksearch.io/search?query=" + searchTerm + ""
        try:
            req = requests.get(self.url, headers=self.headers, verify=False)
            soup = BeautifulSoup(req.content, 'html.parser')
            urls = soup.find_all('a')
            for url in urls:
                if url.get('href') is not None:
                    self.urls_found.append(url.get('href'))
        except:
            print("[!] Error: " + str(sys.exc_info()[0]))
            pass
        
    def print_urls(self):
        for url in self.urls_found:
            print(url)
    
    def write_urls(self, filename):
        with open(filename, 'w') as f:
            for url in self.urls_found:
                f.write(url + "\n")
        print("[*] URLs written to: " + filename)
    
    def write_urls_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.urls_found, f)
        print("[*] URLs written to: " + filename)

    def write_urls_json_pretty(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.urls_found, f, indent=4)
        print("[*] URLs written to: " + filename)



