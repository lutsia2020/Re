# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 11:07:09 2020

@author: Люция
"""

import sqlite3

conn = sqlite3.connect("Opensystem.db")
cursor = conn.cursor()
cursor.execute(''' CREATE TABLE biobio (title,author,journal,year,volume,pages,language,publisher)''')

import re 
with open('biblio.bib', encoding='utf-8') as file:
    
 text = file.read()
 
 records = [i for i in re.split('\n@', text)]
 search_title = re.compile("\s*Title\s*=\s*{\s?(?P<title>\S.*\s?)}", re.MULTILINE).search
 search_author = re.compile("\s*Author\s*=\s*{\s?(?P<author>\S.*\s?)}", re.MULTILINE).search
 search_journal = re.compile("\s*Journal\s*=\s*{\s(?P<journal>\S.*\s?)}", re.MULTILINE).search
 search_year = re.compile("\s*Year\s*=\s*{\s*(?P<year>\S.*\s?)}", re.MULTILINE).search
 search_pages = re.compile("\s*Pages\s*=\s*{\s*(?P<pages>\S.*\s?)}", re.MULTILINE).search
 search_volume = re.compile("\s*Volume\s*=\s*{\s*(?P<volume>\S.*)}", re.MULTILINE).search
 search_language = re.compile("\s*Language\s*=\s*{\s*(?P<language>\S.*)}", re.MULTILINE).search
 search_publisher = re.compile("\s*Publisher\s*=\s*{\s*(?P<publisher>\S.*\s?)}", re.MULTILINE).search
name=''

for r in records:
 standart=""
 dictionary = {}
 def takeinfo(namelink,namekolomn):
     data=""
     i = namelink(r)
     if i:
       dictionary[namekolomn] = i.group(namekolomn)
       data+=dictionary[namekolomn]
     return data
 
    
 name='author'
 Author=takeinfo(search_author,name)
                
 name='title'
 Title=takeinfo(search_title,name)

 name='journal'
 Journal=takeinfo(search_journal,name)
 
 name='year'
 Year=takeinfo(search_year,name)

 name='volume'
 Volume=takeinfo(search_volume,name)
 
 name='pages'
 Pages=takeinfo(search_pages,name)
  
 name='language'
 Language=takeinfo(search_language,name)
 
 name='publisher'
 Publisher=takeinfo(search_publisher,name)
 
 secure=[(Title, Author,Journal,Year,Volume ,Pages,Language,Publisher)]
 cursor.executemany("INSERT INTO biobio VALUES (?,?,?,?,?,?,?,?)",secure)
 conn.commit()

#for row in  cursor:
#    print(row)