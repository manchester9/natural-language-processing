# -*- coding: utf-8 -*-
#URL: http://jmcauley.ucsd.edu/data/amazon/

import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

import sklearn
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

import scrapy
import requests
import beautifulsoup4
import nltk
nltk.download('all')
from gensim.models import Word2Vec
from nltk.corpus import stopwords

import gzip
from tkinter import *

#%matplotlib inline

path = 'C:\\Users\\Roland.Ferrao\\Desktop\\Desktop\\Miscellaneous\\Mental\\Career\\Python\\Natural language processing\\reviews_Grocery_and_Gourmet_Food_5.json.gz'
#Read the json file in pandas?
def parse(path):
    with open(path) as in_file:
        for line in in_file:
            yield eval(line)

def getDF(path):
    i = 0 
    df = {}
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient = 'index')
df = getDF(path)
print(df)

#Count how many lines are in data frame
def count_lines():
    pass


#Descriptive stats
def get_column_names():
    """Descriptive stats on our dataframe"""
    pass


#Get data types for each column
def get_data_type():
    pass


#Get unique values for columns: 
def get_unique_values():
    pass
    
     
#Save the data frame to an excel file
def write_data():
    pass

#Excel file
def open_excel_file():
    pass


#Get first 5 rows
def extract_rows():
    pass

def standardization():
    pass 

#Check if there are reviews written by the same reviewer
def reviewer_check():
    pass


#Extract most positive and most negative reviews
def sentiment():
    pass

#Extract reviews that contain a keyword (e.g. “very useful”)
def keyword_search():
    pass

def tokenization():
    pass 

def summarization():
    pass 

def create_dashboard():
    pass 

def launch_dashboard_online():
    pass 

def deploy_on_aws():
    pass 

#A bit of NLP processing
#Tokenize first 10 reviews
def tokenize():
    pass

#Pos tagging first 10 reviews
def tag_reviews():
    pass

#Extract all adjectives from the first ten reviews
def extract_adjectives():
    pass


#Tag named entities for the first ten reviews
def tag_entities():
    pass

def linguistic_markers():
    pass 


def partition_markers():
    pass 


def get_tag_entries():
    pass


# Build models
def classification():
    pass 

def document_classifier():
    pass 


def google_bert():
    pass 


def vader_statistics():
    pass 


def build_final_model():
    pass 


def external_adjective():
    pass 


def internal_adjectives():
    pass 


def main():
    pass 


if __name__ == "__main__":
    main()















