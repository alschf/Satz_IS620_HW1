# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:27:59 2016

@author: alexandersatz
"""

from Bio import Entrez
from Bio import Medline
import re

MAX_COUNT = 4215
TERM = 'Crispr'

print('Getting {0} publications containing {1}...'.format(MAX_COUNT, TERM))
Entrez.email = 'A.N.Other@example.com'
h = Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
result = Entrez.read(h)
print('Total number of publications containing {0}: {1}'.format(TERM, result['Count']))
ids = result['IdList']
h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
records = Medline.parse(h)

pubs = []
perm = []

for record in records:
    perm.append(record) 
    auth = []
    au = record.get('AU','?')
    for a in au: 
        auth.append(au)
    af = record.get('AD','?')
    d = record.get('EDAT', '?')
    ta = record.get('TA', '?')
    jt = record.get('JT', '?')
    pubs.append([auth, af, d, ta, jt])
    
f = open('project2pubs.txt','w')
for x in pubs:
    s = ','.join(map(str, x))
    f.write(s+ "\n") 
f.close() # you can omit in most cases as the destructor will call it

S_T = []  
    
for x in pubs:
    a = x[0]
    a = a[0]
    for z in range(0,len(a)):
        S_T.append([a[z],x[3]])
        
f = open('Source_Target_P2IS620.txt','w')
f.write("Source,Target\n")
for x in S_T:
    f.write(x[1] + "," + x[0] + "\n") 
f.close() # you can omit in most cases as the destructor will call it
        



    