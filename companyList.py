#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 13:12:52 2021

@author: yiransun
"""
import pandas as pd
import numpy as np

class CompanyList():
    def __init__(self):
        self.companies = None
        self.flag = -1
        self.affiliations = None
    
    def process_csv(self, csv_path):
        df_raw = pd.read_csv(csv_path, sep=";")
        df = df_raw[df_raw['Extra'].isna()]
        df = df.drop(labels = ['Weighting', 'Extra'], axis = 1) #size = 135
        
        df2 = df_raw.dropna() #size = 210
        df2 = df2.rename(columns={"Holding": "Holding", "Symbol":"Extra", "Weighting":"Symbol", "Extra":"Weighting"})
        df2 = df2.drop(labels = ["Extra", 'Weighting'], axis = 1)
        
        df = pd.concat([df, df2])
        
        if(self.flag == -1):
            self.companies = df
            self.flag = 1
        else:
            self.companies = pd.concat([self.companies, df])
            self.companies = self.companies.drop_duplicates().reset_index(drop=True)
            print(self.companies.shape)
    
    def __is_affiliation__(self, company):
        '''
        company: string, name of the company
        '''
        
        for af in self.affiliations:  
            if(company.split()[0].lower()) in af[2].lower().split():
                return af
        return None
    
    def check_affiliation(self, affiliations_path):
        affiliations_path = 'Affiliations.txt'
        f = open(affiliations_path, 'r')
        text = f.readlines()
        text = filter(lambda x: 'university' not in x.lower(), text)
        self.affiliations = [x.split("\t") for x in text]
        
        l = len(self.companies)
        self.companies["NormalizedName"] = [[] for _ in range(l)]
        self.companies["PaperCount"] = [[] for _ in range(l)]
        self.companies["PaperFamilyCount"] = [[] for _ in range(l)]
        self.companies["CitationCount"] = [[] for _ in range(l)]
        
        for index, row in self.companies.iterrows():
            af = self.__is_affiliation__(row['Holding'])
            if af is None:
                self.companies = self.companies.drop(index = index)
            else:
                self.companies.at[index, 'NormalizedName'] = af[2]
                self.companies.at[index, 'PaperCount'] = af[7]
                self.companies.at[index, 'PaperFamilyCount'] = af[8]
                self.companies.at[index, 'CitationCount'] = af[9]
            
    
    def export_list(self, export_path):
        self.companies.to_csv(export_path, index=False)
        

cl = CompanyList()
csv_list = ['VGT-holdings.csv', 'DRIV-holdings.csv', 'BOTZ-holdings.csv']
for csv in csv_list:
    cl.process_csv(csv)
cl.check_affiliation("Affiliations.txt")
cl.export_list('company_list.csv')




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        







    

