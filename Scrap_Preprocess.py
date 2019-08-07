# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 13:36:21 2019

@author: TIKI
"""

import re
import csv
import Stop_words_Remover

data_preprocessed = []

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>.*<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def extraction(soup):
    fresh_elements = []
    all_elements =[]
    for tag in soup.find_all():
        all_elements.append(tag.name)
    wanted_tags = ['h1','h2','h3','h4','h5','h6','td','b','p','span','div']
    fresh_elements = [el for el in all_elements if el in wanted_tags]
    unique_elem = set(fresh_elements)
    unique_list = list(unique_elem)
    tag_texts = []
    limit = len(unique_list)
    for i in range(limit):
        for tag in soup.find_all(str(unique_list[i])):
            html = tag.getText()
            first_extract=cleanhtml(html)
            if(len(first_extract)<130 and len(first_extract)>3):
                tag_texts.append(first_extract)
    cleaning(tag_texts)

def cleaning(tag_texts):
    global data_preprocessed
    cleaned = re.sub(r'[?|!|\'|"|#]',r'',str(tag_texts))
    cleaned = re.sub(r'[.|,|)|(|\|/]',r' ',cleaned)
    cleaned = cleaned.strip()
    cleaned = cleaned.replace("\n"," ")
    removed_regex = re.sub(r'[^\w]', ' ', cleaned)
    cleaned_scrap = re.sub(' +', ' ',removed_regex)
    result = ''.join([i for i in cleaned_scrap if not i.isdigit()])
    text = ' '.join([word for word in result.split() if word not in Stop_words_Remover.new_stop_words])
    data_preprocessed = text.split("delimiter")
    with open('testarrayData.csv', 'a',encoding='utf-8') as output:
        writer = csv.writer(output,lineterminator ='\n')
        for val in data_preprocessed:
            writer.writerow([val])
