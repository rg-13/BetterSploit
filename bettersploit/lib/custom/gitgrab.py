from github import Github
import os
import sys
import time
import requests
import json

class GitGrab:
    def __init__(self, username, password, repo, branch, path):
        self.username = username
        self.password = password
        self.acess_token = None
        self.repo_url = None
        self.repo_name = None
        self.repo_description = None
        
    def get_repo_info(self):
        return {
            'repo_url': self.repo_url,
            'repo_name': self.repo_name,
            'repo_description': self.repo_description,
            'repo_created_at': self.repo_created_at,
            'repo_updated_at': self.repo_updated_at,
            'repo_pushed_at': self.repo_pushed_at,
            'repo_size': self.repo_size,
            'repo_open_issues': self.repo_open_issues,
            'repo_watchers': self.repo_watchers,
            'repo_language': self.repo_language,
            'repo_forks': self.repo_forks
        }


    def save2json(self, filename, data):
        with open(filename, 'w') as f:
            json.dump(data, f)

    def search_github(self, keywords):
        self.keywords = [keyword.strip() for keyword in keywords.split(',')]
        query = '+'.join(keywords) + '+in:name,description,readme'
        results = g.search_repositories(query, sort='stars', order='desc')
        return results

        for result in results:
           self.save2json(result.name, json_result)

            print('Repo name: {}'.format(repo_name))
            print('Repo description: {}'.format(repo_description))
            print('Repo url: {}'.format(repo_url))
            print('\n')

    def search_files(self, keywords):
        rate_limit = g.get_rate_limit()
        rate = rate_limit.rate
        remaining = rate.remaining
    
        if remaining == 0:
            print('Rate limit reached, waiting for {} seconds'.format(rate.reset - time.time()))
            time.sleep(rate.reset - time.time())
            rate_limit = g.get_rate_limit()
            rate = rate_limit.rate
            remaining = rate.remaining
        
        query = f'"{keywords}" english" in:file'
        result = g.search_code(query, sort='stars', order='desc')
        
        max_size = 100  
        return('Found: {result.totalCount} files matching "{keywords}"')
        file_name = g.repo_name
        if result.totalCount > max_size:
            result = result[:max_size]
        for item in result:
                self.save2json(file_name, item.raw_data)

        return result
        
                
    def clone_repo(self, repo_url):
        self.repo_url = repo_url
        repo_name = repo_url.split('/')[-1]
        self.repo_name = repo_name
        repo_path = os.path.join(self.path, repo_name)
        if os.path.exists(repo_path):
            print('Repo already cloned')
            return
        os.system('git clone {} {}'.format(repo_url, repo_path))
        print('Repo cloned')
        return repo_path

    def load_googledorks(self, filename):
        with open(filename, 'r') as f:
            self.keywords = f.read().splitlines()
        return self.keywords
        
    def search_with_list(self, list):
        self.load_googledorks(list)
        for item in list:
            hub = self.search_github(item)
            files = self.search_files(item)
            for item in hub:
                for item in files:
                    self.save2json(item.name, item.raw_data)
                    print(item)