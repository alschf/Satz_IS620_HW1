# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:27:59 2016

@author: alexandersatz
"""

from Bio import Entrez
from Bio import Medline
import re

MAX_COUNT = 17
TERM = 'Crispr editing'

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

## Acquire Author and Affiliation Data for each record

for record in records:
    perm.append(record) 
    auth = []
    au = record.get('AU','?')
    for a in au: 
        auth.append(au)
    af = record.get('AD','?')
    d = record.get('EDAT', '?')
    pubs.append([auth, af, d])
    

#Assign Authors to each other (source-targets)  
audict = {}
for x in pubs:
    x = x[0]
    x = x[0]
    for z in range(0,len(x)):
        for i in range(z, len(x)):
            try:
                audict[str(x[z]) +'WWW'+ str(x[i])] += 1
            except KeyError:
                audict[str(x[z]) +'WWW'+ str(x[i])] = 1


         
##Assign affiliations to each author                
auaffil = {}
count = 0
bad = 0
for x in pubs:
    au = x[0][0]
    af = x[1]
    af = af.split(". ")
    #af = re.split(r'.;', af)    
    #b = copy.deepcopy(af)
    if isinstance(af, list):
        for x in af:
            if len(x) < 80:
                af.remove(x)
            if len(x) > 400:
                af.remove(x)
    if not isinstance(af, list):
        if len(af) > 80 and len(af) <400:
            af = list(af)
        else:
            af = []
        
    for a in range(0, min(len(af),len(au))):
        try:
            ans = auaffil[au[a]]
            if len(ans)>len(af[a]):
                auaffil[au[a]] = af[a]

        except KeyError:
            auaffil[au[a]] = af[a]
    
        

    
f = open('saveCrisprSearch.txt','w')
f.write('Source,Target\n')
for k,v in audict.iteritems():
    s = k.split('WWW')
    for i in range(0,v):
        f.write(s[0] + "," + s[1] + "\n") 
f.close() # you can omit in most cases as the destructor will call it


##in final, assign each author to USA or not.
def hasUSA(line):
    line = line.lower()
    if 'usa' in line:
        return True
    if 'u.s.a' in line:
        return True
    if 'america' in line:
        return True
    return False

f = open('saveCrisprAuthorAffilUSA.txt','w')
f.write('Author,InUSA\n')
for k,v in auaffil.iteritems():
    if hasUSA(v):
        f.write(k + "," + str(1) + "\n") 
    else:
        f.write(k + "," + str(0) + "\n") 
f.close() # you can omit in most cases as the destructor will call it


    