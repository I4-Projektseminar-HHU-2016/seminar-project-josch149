# -*- coding: utf-8 -*-
import csv
from datetime import date, datetime, timedelta

# Hier werden die Werte aus der .CSV gelesen und für die weitere Verarbeitung gespeichert.
def csv_werte (datei, spalte1, spalte2):
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
		#return listespalte1
		#return listespalte2
		#return listegemischt
		return wertedict


w1 = csv_werte ("CSVs/Sonnenschein_0915.csv", 2,3)
w2 = csv_werte ("CSVs/Neuschnee_0915.csv", 2,3)
w3 = csv_werte ("CSVs/Lufttemp_Max_0915.csv", 2,3)

# folgedes Segment stammt von: http://stackoverflow.com/questions/10688006/generate-a-list-of-datetimes-between-an-interval abgerufen am 23.08.2016
"""from datetime import date, datetime, timedelta

def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

for result in perdelta(date(2016, 01, 01), date(2016, 12, 31), timedelta(days=1)):
     print result"""

# altes Segment als Vorlage zur generierung von Datumsintevall:
"""
# Durch die Intervall Funktion wird das erstellen eines Datumintervalls vorbereitet.
def intervall(start, ende, delta):
    while start < ende:
        yield start
        start += delta

datumliste=[]
for result in intervall(date(2015, 12, 01), date(2016, 01, 02), timedelta(days=1)):
     datumliste.append(str(result))
#     print result
#print liste


for element in datumliste:
	if element in w1.iterkeys():
		print element, w1[element]
	else:
		print element, "ist nicht in der Liste"

"""


#Weisheiten/Regeln Januar:

#Jan: 1. Regel: Ist der Januar hell und weiß, wird der Sommer sicher heiß.

def jan1_hell_weiss(csv_werte):
	
#Zuerst wird das benötigte Datumintervall erezugt
	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
#	dict={}
	liste1=[]
	liste2=[]
	for result in intervall(date(2015, 1, 1), date(2015, 2, 1), timedelta(days=1)):
		datumliste.append(str(result))
	for element in datumliste:
		if element in csv_werte.iterkeys():
#			dict.update({element:csv_werte[element]})
			liste1.append(element)
			liste2.append(csv_werte[element])
		else:
			pass
			
#Hier wird das Komma in einen Punkt umgewandelt, damit später die Strings durch Floats ersetzt werden.		
	counter=0
	position=0
	for element in liste2:
		element_neu=element.replace(",", ".")
		liste2[position]=element_neu
		position=position+1

#Hier wird gezählt, wie viele Werte den Anforderungen entsprechen.		
	position=0
	while position < len(liste2):
		if liste2[position] != "0.0":
			counter=counter + 1
			position=position+1
		else:
			position=position+1
	print liste2
	ergebnis=[counter, len(liste2)]
	return ergebnis

#Zuerst wird das benötigte Datumintervall erezugt
def jan1_sommer_heiss(csv_werte):
	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
#	dict={}
	liste1=[]
	liste2=[]
	for result in intervall(date(2015, 6, 1), date(2015, 9, 1), timedelta(days=1)):
		datumliste.append(str(result))
	for element in datumliste:
		if element in csv_werte.iterkeys():
#			dict.update({element:csv_werte[element]})
			liste1.append(element)
			liste2.append(csv_werte[element])
		else:
			pass

#Hier wird das Komma in einen Punkt umgewandelt, damit später die Strings durch Floats ersetzt werden.			
	counter=0
	position=0
	for element in liste2:
		element_neu=element.replace(",", ".")
		liste2[position]=element_neu
		position=position+1

#Hier wird gezählt, wie viele Werte den Anforderungen entsprechen.
	position=0
	while position < len(liste2):
		if float(liste2[position]) > 30.0:
			counter=counter + 1
			position=position+1
		else:
			position=position+1
	print liste2
	ergebnis=[counter, len(liste2)]
	return ergebnis
			
print jan1_hell_weiss(w1)
print jan1_hell_weiss(w2)
print jan1_sommer_heiss(w3)

#Jan: 2.Regel: Lässt der Januar Regen fallen, lässt der Lenz es gefrieren.

#Jan: 3.Regel: Auf trockenen, kalten Januar folgt viel Schnee im Februar.

#Jan: 4.Regel: So viele Tropfen im Januar, so viel Schnee im Mai.
	
