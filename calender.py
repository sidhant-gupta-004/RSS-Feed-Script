import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Opens the upcoming list from ctftime.org and parses it
html = urlopen("https://ctftime.org/event/list/upcoming")
bso = BeautifulSoup(html, "html.parser")

#Specifying the table since the upcoming events are in table in the website
table = bso.findAll("table",{"class":"table-striped"})[0] #table class is table-striped. finds everything with it
rows = table.findAll("tr")

f = open("calendar.json", 'wt', newline = '', encoding = 'utf-8')

try:
	table = 
