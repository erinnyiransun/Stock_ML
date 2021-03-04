#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 21:54:48 2021

@author: yiransun
"""
import requests
from bs4 import BeautifulSoup


class StarHistory():
    
    def __init__(self, company):
        self.company = company
        
        self.headers = {'Accept':'application/vnd.github.v3.star+json', 'Authorization':'token 03560a7e0ae265951f79131d72a0def11f77a986'}
        
        self.repo_list = None
        self.star_history = None 
    
    def __get_page_num__(self, url):
        pos = url.find("page=")
        return int(url[pos:][5:])
    
    def __no_repo__(self, response):
        text = response.text
        soup = BeautifulSoup(text)
        element = soup.findAll("div", {"class": "blankslate"})
        print(element)
        if(len(element) == 0):
            return False
        else:
            return True
        
    def get_repo_list(self):
        self.repo_list = []
        
        company = self.company
        url = f"https://github.com/{company}?page="
        page = 1
        response = requests.get(url+str(page), verify=False)
        
        while not self.__no_repo__(response):
            text = response.text
            soup = BeautifulSoup(text)
            for repo in soup.findAll('a', {"itemprop":"name codeRepository", "data-hovercard-type":"repository"}):
                repo = repo.text.split()[0]
                self.repo_list.append(repo)
            page += 1
            response = requests.get(url+str(page), verify=False)
    
    def __add_to_star_history__(self, data):
        for i in range(len(data)):
            starred_at = data[i]['starred_at'][:10]
            if(starred_at in self.star_history.keys()):
                self.star_history[starred_at] += 1
            else:
                self.star_history[starred_at] = 1
    
    def get_star_history(self):
        self.star_history = {}
        
        company = self.company
        
        for repo in self.repo_list:
            page = 1
            url = f"http://api.github.com/repos/{company}/{repo}/stargazers?page={page}"
            response = requests.get(url, headers = self.headers)
            page_num = self.__get_page_num__(response.links['last']['url'])
            
            for page in range(1, page_num+1):
                response = requests.get(url, headers = self.headers)
                data = response.json()
                self.__add_to_star_history__(data)
    
        


company = "facebook"
s = StarHistory(company)
s.repo_list = ['componentkit',
 'fboss',
 'docusaurus',
 'buck',
 'jest',
 'infer',
 'idb',
 'sapp',
 'flipper',
 'mysql-5.6',
 'fbthrift',
 'relay',
 'react-native',
 'hhvm',
 'proxygen',
 'openbmc',
 'hermes',
 'Ax',
 'rocksdb',
 'metro',
 'openr',
 'prophet',
 'pyre-check',
 'react',
 'folly',
 'react-native-website',
 'create-react-app',
 'facebook-python-business-sdk',
 'facebook-java-business-sdk',
 'facebook-ruby-business-sdk',
 'facebook-php-business-sdk',
 'facebook-nodejs-business-sdk',
 'zstd',
 'facebook-android-sdk',
 'redex',
 'litho',
 'yoga',
 'fbt',
 'draft-js',
 'mcrouter',
 'duckling',
 'fresco',
 'Haxl',
 'facebook-ios-sdk',
 'watchman',
 'wangle',
 'fbzmq',
 'fatal',
 'flow',
 'ThreatExchange',
 'jscodeshift',
 'fishhook',
 'fb303',
 'squangle',
 'TestSlide',
 'homebrew-fb',
 'openbmc-linux',
 'chef-cookbooks',
 'instant-articles-builder',
 'fbshipit',
 'treadmill',
 'FAI-PEP',
 'PathPicker',
 'bistro',
 'SPARTA',
 'facebook-business-sdk-codegen',
 'IT-CPE',
 'openbmc-uboot',
 'regenerator',
 'remodel',
 'facebook360_dep',
 'react-native-fbsdk',
 'prop-types',
 'chisel',
 'SoLoader',
 'TextLayoutBuilder',
 'jsx',
 'taste-tester',
 'wdt',
 'facebook-sdk-for-unity',
 'fbghc',
 'prepack',
 'mysql-8.0',
 'fbjs',
 'pcicrawler',
 'flux',
 'FBRetainCycleDetector',
 'facebook-instant-articles-sdk-php',
 'screenshot-tests-for-android',
 'shimmer-android']



# page = 6 
# url = f"https://github.com/{company}?page={page}"
# response = requests.get(url, verify=False)
# text = response.text
# soup = BeautifulSoup(text)
# element = soup.findAll("div", {"class": "blankslate"})



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



