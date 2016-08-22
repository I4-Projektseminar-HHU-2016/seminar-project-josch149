# -*- coding: utf-8 -*-
import csv

# Hier werden die Werte aus der .CSV gelesen und für die weitere Verarbeitung gespeichert.
"""def wert (datei, zeile, spalte1, spalte2):
	liste1=[]
	liste2=[]
	with open (datei, 'r') as data_file:
		reader = csv.reader(data_file, delimiter=';')
		for row in reader:
			liste1.append(row)
		liste2=liste1[zeile]
		ergebnis1 = liste2[spalte1]
		ergebnis2 = liste2[spalte2]
		return ergebnis1, ergebnis2
		
w1 = wert ("test.csv", 1, 2, 3)
print w1"""

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
		return listegemischt
		
w1 = wert ("test.csv", 2, 3)
print w1

