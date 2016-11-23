import json
from urllib2 import urlopen
from bs4 import BeautifulSoup

#Opens the upcoming list from ctftime.org and parses it
html = urlopen("https://ctftime.org/event/list/upcoming")
bso = BeautifulSoup(html, "html.parser")

#Specifying the table since the upcoming events are in table in the website
table = bso.findAll("table",{"class":"table-striped"})[0] #table class is table-striped. finds everything with it
rows = table.findAll("tr")

with open("calendar.json", 'w') as f:

    table  = [ [cell.get_text() for cell in row.findAll(['td','th'])] for row in rows ]

    column = table[0]
    table  = table[1:]
    tableDict = [ {column[j]: table[i][j] for j in range(len(column))} for i in range(len(table)) ]
    json.dump(tableDict,f, indent=2)
    #f.write('\n')

    for c in tableDict:
	    print c


