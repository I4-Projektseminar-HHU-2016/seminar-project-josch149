# -*- coding: utf-8 -*-
import csv
from datetime import date, datetime, timedelta

# Hier werden die Werte aus der .CSV gelesen und für die weitere Verarbeitung gespeichert.
def wert (datei, spalte1, spalte2):
	liste0=[]
	listespalte1=[]
	listespalte2=[]
	listegemischt=[]
	wertedict={}
	with open (datei, 'r') as data_file:
		reader = csv.reader(data_file, delimiter=';')
		for row in reader:
			liste0.append(row)
		for element in liste0:
			listespalte1.append(element[spalte1])
			listespalte2.append(element[spalte2])
			listegemischt.append(element[spalte1])
			listegemischt.append(element[spalte2])
			wertedict.update({element[spalte1]:element[spalte2]})
		#return listespalte1, listespalte2
		#return listegemischt
		return wertedict
		
w1 = wert ("test.csv", 2, 3)
print w1

# folgedes Segment stammt von: http://stackoverflow.com/questions/10688006/generate-a-list-of-datetimes-between-an-interval abgerufen am 23.08.2016
"""from datetime import date, datetime, timedelta

def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

for result in perdelta(date(2016, 01, 01), date(2016, 12, 31), timedelta(days=1)):
     print result"""

# Hier wird eine Liste erzeugt, in der ein bestimmtes Datumintervall generiert wird.
def intervall(start, ende, delta):
    while start < ende:
        yield start
        start += delta

liste=[]
for result in intervall(date(2016, 01, 01), date(2017, 01, 01), timedelta(days=1)):
     liste.append(str(result))
#     print result
print liste
