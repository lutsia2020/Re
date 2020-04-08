# -*- coding: utf-8 -*-
"""
@author: Люция
"""

import re 
comment='#'
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

for r in records:
 standart=""
 dictionary = {}
 
 i = search_author(r)
 if i:
  dictionary['author'] = i.group('author')
  standart+=dictionary['author']+" ,"
 i = search_title(r)
 if i:
  dictionary['title'] = i.group('title')
  standart+=dictionary['title']+" // "

 i = search_journal(r)
 if i:
  dictionary['journal'] = i.group('journal')
  standart+=dictionary['journal'] +" , -"
 i = search_year(r)
 if i:
  dictionary['year'] = i.group('year')
  standart+=dictionary['year']+".- VOL."
 i = search_volume(r)
 if i:
  dictionary['volume'] = i.group('volume')
  standart+=dictionary['volume']+". , cтp-P."
 i = search_pages(r)
 if i:
  dictionary['pages'] = i.group('pages')
  standart+=dictionary['pages']+". , lang."
  
 i = search_language(r)
 if i:
  dictionary['language'] = i.group('language')
  standart+=dictionary['language']+". , publish.-"

 i = search_publisher(r)
 if i:
  dictionary['publisher'] = i.group('publisher')
  standart+=dictionary['publisher']
 print(standart)