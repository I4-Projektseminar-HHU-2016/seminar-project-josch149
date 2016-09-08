# -*- coding: utf-8 -*-
import csv
from datetime import date, datetime, timedelta

# Hier werden die Werte aus der .CSV gelesen und für die weitere Verarbeitung gespeichert.
def csv_werte (datei, spalte1, spalte2):
	liste0=[]
#	listespalte1=[]
#	listespalte2=[]
#	listegemischt=[]
	wertedict={}
	with open (datei, 'r') as data_file:
		reader = csv.reader(data_file, delimiter=';')
		for row in reader:
			liste0.append(row)
		for element in liste0:
#			listespalte1.append(element[spalte1])
#			listespalte2.append(element[spalte2])
#			listegemischt.append(element[spalte1])
#			listegemischt.append(element[spalte2])
			wertedict.update({element[spalte1]:element[spalte2]})
#		return listespalte1
#		return listespalte2
#		return listegemischt

# Im wertedict sind die Datumangaben als Schlüssel und die spezifischen Daten als Value enthalten und werden zurückgegeben.
		return wertedict


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

#1.Teil der Jan: 1. Regel
def jan1_hell_weiss(csv_werte):
	
#Zuerst wird das benötigte Datumintervall erezugt

	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
#	dict={}
#	liste1=[]
	liste2=[]
	ergebnis=[]
	year=1990

#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 1, 1), date(year, 2, 1), timedelta(days=1)):
			datumliste.append(str(result))
		for element in datumliste:

#Es gibt manche Werte die nicht gemessen wurden z.B. 20.01.1993 Sonnenscheindauer
			if element in csv_werte.iterkeys():
#				dict.update({element:csv_werte[element]})
#				liste1.append(element)
				liste2.append(csv_werte[element])
				
#			else:
				#pass

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
			if float(liste2[position]) != 0.0:
				counter=counter + 1
				position=position+1
			else:
				position=position+1
#		print liste2

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
#		print len(liste2)
#		print counter
#		print liste2
		year=year+1
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	return ergebnis

#2.Teil der Jan: 1. Regel
def jan1_sommer_heiss(csv_werte):
	
#Zuerst wird das benötigte Datumintervall erezugt

	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
#	dict={}
	liste1=[]
	liste2=[]
	ergebnis=[]
	year=1995
	
#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 6, 1), date(year, 9, 1), timedelta(days=1)):
			datumliste.append(str(result))
		for element in datumliste:
			
#Es gibt manche Werte die nicht gemessen wurden z.B. 20.01.1993 Sonnenscheindauer
			if element in csv_werte.iterkeys():
#				dict.update({element:csv_werte[element]})
#				liste1.append(element)
				liste2.append(csv_werte[element])
				
#			else:
#				pass

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
#		print liste2

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
#		print len(liste2)
#		print counter
#		print liste2
		year=year+1
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	return ergebnis

#Hier werden nun erst die "wertedict" mit den benötigten CSV-Daten erzeugt und anschließend die Funktion mit dem entsprechenden wertedict ausgeführt.
w1 = csv_werte ("CSVs/Sonnenschein_0915.csv", 2,3)
print jan1_hell_weiss(w1)
w2 = csv_werte ("CSVs/Neuschnee_0915.csv", 2,3)	
print jan1_hell_weiss(w2)
w3 = csv_werte ("CSVs/Lufttemp_Max_0915.csv", 2,3)	
print jan1_sommer_heiss(w3)

#Jan: 2.Regel: Lässt der Januar Regen fallen, lässt der Lenz es gefrieren.

#Jan: 3.Regel: Auf trockenen, kalten Januar folgt viel Schnee im Februar.

#Jan: 4.Regel: So viele Tropfen im Januar, so viel Schnee im Mai.
	
