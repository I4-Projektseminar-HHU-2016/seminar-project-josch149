# -*- coding: utf-8 -*-
import csv

# Hier werden die Werte aus der .CSV gelesen und für die weitere Verarbeitung gespeichert.
def wert (datei, spalte, zeile):
	liste1=[]
	liste2=[]
	with open (datei, 'r') as data_file:
		reader = csv.reader(data_file, delimiter=';')
		for row in reader:
			liste1.append(row)
		liste2=liste1[zeile]
		ergebnis = liste2[spalte]
		return ergebnis
		
w1 = wert ("test.csv", 2, 1)
print w1
