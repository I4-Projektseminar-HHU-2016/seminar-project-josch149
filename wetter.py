# -*- coding: utf-8 -*-
import csv
from datetime import date, datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

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


#Weisheiten/Regeln Januar:

#Jan: 1. Regel: Ist der Januar hell und weiß, wird der Sommer sicher heiß.

#1.Teil der Jan: 1. Regel
def jan1_hell(csv_werte):
	
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
	
	ylist=[]
	vlist=[]

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
			if float(liste2[position]) >= 1.0:
				counter=counter + 1
				position=position+1
			else:
				position=position+1
#		print liste2

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
#		vergleich=0
#		ylist.append(year)
#		vergleich=100/len(liste2)*counter
#		vlist.append(vergleich)
#		print len(liste2)
#		print counter
#		print liste2
		year=year+1
	return ergebnis
	

#2.Teil der Jan: 1. Regel
def jan1_weiss(csv_werte):
	
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
	
	ylist=[]
	vlist=[]

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
			if float(liste2[position]) > 0.0:
				counter=counter + 1
				position=position+1
			else:
				position=position+1
#		print liste2

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
#		vergleich=0
#		ylist.append(year)
#		vergleich=100/len(liste2)*counter
#		vlist.append(vergleich)
#		print len(liste2)
#		print counter
#		print liste2
		year=year+1
	return ergebnis
	

		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	

#3.Teil der Jan: 1. Regel
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
	year=1990
	
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
			if float(liste2[position]) >= 25.0:
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


#Jan: 2.Regel: Lässt der Januar Regen fallen, lässt der Lenz es gefrieren.

#1.Teil der Jan: 2. Regel
def jan2_regen(csv_werte):
	
#Zuerst wird das benötigte Datumintervall erezugt

	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
#	dict={}
#	liste1=[]
	ergebnis=[]
	year=1990
	
	ylist=[]
	vlist=[]

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
			if float(liste2[position]) > 0.0:
				counter=counter + 1
				position=position+1
			else:
				position=position+1
#		print liste2

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
#		vergleich=0
#		ylist.append(year)
#		vergleich=100/len(liste2)*counter
#		vlist.append(vergleich)
#		print len(liste2)
#		print counter
#		print liste2
		year=year+1
	return ergebnis
	
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	

#2.Teil der Jan: 2. Regel
def jan2_lenz_frost(csv_werte):
	
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
	year=1990
	
#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 3, 1), date(year, 6, 1), timedelta(days=1)):
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
			if float(liste2[position]) <= 0.0:
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


#Jan: 3.Regel: Friert es auf Vigilius (31.01.), im Märzen Kälte kommen muss.

#1.Teil der Jan: 3. Regel
def jan3_vigilius(csv_werte):
	
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
	
	ylist=[]
	vlist=[]

#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 1, 31), date(year, 2, 1), timedelta(days=1)):
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
			if float(liste2[position]) <= 0.0:
				counter=counter + 1
				position=position+1
			else:
				position=position+1
#		print liste2

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
#		vergleich=0
#		ylist.append(year)
#		vergleich=100/len(liste2)*counter
#		vlist.append(vergleich)
#		print len(liste2)
#		print counter
#		print liste2
		year=year+1
	return ergebnis
	

	
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	

#2.Teil der Jan: 3. Regel
def jan3_maerz_kalt(csv_werte):
	
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
	year=1990
	
#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 3, 1), date(year, 4, 1), timedelta(days=1)):
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
			if float(liste2[position]) <= 5.0:
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

#Feb: 1. Regel: Scheint an Lichtmess (02.02.) die Sonne heiß, kommt noch sehr viel Schnee und Eis.

#1.Teil der Feb: 1. Regel
def feb1_lichtmess_sonne(csv_werte):
	
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
	
	ylist=[]
	vlist=[]

#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 2, 2), date(year, 2, 3), timedelta(days=1)):
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
			if float(liste2[position]) >= 5.0:
				counter=counter + 1
				position=position+1
			else:
				position=position+1
#		print liste2

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
#		vergleich=0
#		ylist.append(year)
#		vergleich=100/len(liste2)*counter
#		vlist.append(vergleich)
#		print len(liste2)
#		print counter
#		print liste2
		year=year+1
	return ergebnis
	

	
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	

#2.Teil der Feb: 1. Regel
def feb1_kommt_schnee(csv_werte):
	
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
	year=1990
	
#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 2, 3), date(year, 4, 1), timedelta(days=1)):
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
			if float(liste2[position]) > 0.0:
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
	
#3.Teil der Feb: 1. Regel
def feb1_kommt_eis(csv_werte):
	
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
	year=1990
	
#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 2, 3), date(year, 4, 1), timedelta(days=1)):
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
			if float(liste2[position]) <= 0.0:
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

#Feb. 2. Regel: Im Februar Schnee und Eis, macht den Sommer lang und heiss.


#1.Teil der Feb: 2. Regel
def feb2_feb_schnee(csv_werte):
	
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
	
	ylist=[]
	vlist=[]

#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 2, 1), date(year, 3, 1), timedelta(days=1)):
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
			if float(liste2[position]) > 0.0:
				counter=counter + 1
				position=position+1
			else:
				position=position+1
#		print liste2

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
#		vergleich=0
#		ylist.append(year)
#		vergleich=100/len(liste2)*counter
#		vlist.append(vergleich)
#		print len(liste2)
#		print counter
#		print liste2
		year=year+1
	return ergebnis
	

	
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	

#2.Teil der Feb: 1. Regel
def feb2_feb_eis(csv_werte):
	
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
	year=1990
	
#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 2, 1), date(year, 3, 1), timedelta(days=1)):
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
			if float(liste2[position]) <= 0.0:
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
	
#3.Teil der Feb: 2. Regel
#identisch mit jan1_sommer_heiss

#Mae: 1. Regel: Im März viel Schnee und Regen bringt wenig Sommersegen.

#1.Teil der Mae: 1. Regel
def mae1_mae_schnee(csv_werte):
	
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
	
	ylist=[]
	vlist=[]

#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 3, 1), date(year, 4, 1), timedelta(days=1)):
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
			if float(liste2[position]) > 0.0:
				counter=counter + 1
				position=position+1
			else:
				position=position+1
#		print liste2

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
#		vergleich=0
#		ylist.append(year)
#		vergleich=100/len(liste2)*counter
#		vlist.append(vergleich)
#		print len(liste2)
#		print counter
#		print liste2
		year=year+1
	return ergebnis
	

	
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	

#2.Teil der Mae: 1. Regel
def mae1_mae_regen(csv_werte):
	
#Zuerst wird das benötigte Datumintervall erezugt

	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
#	dict={}
#	liste1=[]
	ergebnis=[]
	year=1990
	
	ylist=[]
	vlist=[]

#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		liste3=[]
		for result in intervall(date(year, 3, 1), date(year, 4, 1), timedelta(days=1)):
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
			if float(liste2[position]) > 0.0:
				counter=counter + 1
				position=position+1
			else:
				position=position+1
#		print liste2

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
#		vergleich=0
#		ylist.append(year)
#		vergleich=100/len(liste2)*counter
#		vlist.append(vergleich)
#		print len(liste2)
#		print counter
#		print liste2
		year=year+1
	return ergebnis
	
#3.Teil der Mae: 1. Regel
# Sommersegen wie jan1_sommer_heiss

#Mae: 2. Regel: Hält St. Ruprecht (28.03.) den Himmel rein, so wird es auch im Juli sein.

#1.Teil der Mae: 2. Regel
def mae2_rup_sonne(csv_werte1, csv_werte2):
	
#Zuerst wird das benötigte Datumintervall erezugt

	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
#	dict={}
#	liste1=[]
	liste2=[]
	liste3=[]
	ergebnis=[]
	year=1990
	
	ylist=[]
	vlist=[]

#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 3, 28), date(year, 3, 29), timedelta(days=1)):
			datumliste.append(str(result))
		for element in datumliste:

#Es gibt manche Werte die nicht gemessen wurden z.B. 20.01.1993 Sonnenscheindauer
			if element in csv_werte1.iterkeys():
#				dict.update({element:csv_werte[element]})
#				liste1.append(element)
				liste2.append(csv_werte1[element])
				
			if element in csv_werte2.iterkeys():
#				dict.update({element:csv_werte[element]})
#				liste1.append(element)
				liste3.append(csv_werte2[element])
				
#			else:
				#pass

#Hier wird das Komma in einen Punkt umgewandelt, damit später die Strings durch Floats ersetzt werden.			
		counter=0
		position=0
		for element in liste2:
			element_neu=element.replace(",", ".")
			liste2[position]=element_neu
			position=position+1
			
		position=0
		for element in liste3:
			element_neu=element.replace(",", ".")
			liste3[position]=element_neu
			position=position+1

#Hier wird gezählt, wie viele Werte den Anforderungen entsprechen.
		position=0
		while position < len(liste2):
			if float(liste2[position]) == 0.0 and  float(liste3[position]) >= 0.0:
				counter=counter + 1
				position=position+1
			else:
				position=position+1
#		print liste2

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
#		vergleich=0
#		ylist.append(year)
#		vergleich=100/len(liste2)*counter
#		vlist.append(vergleich)
#		print len(liste2)
#		print counter
#		print liste2
		year=year+1
	return ergebnis
	
#2.Teil der Mae: 2. Regel
def mae2_juli_sonne(csv_werte):
	
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
	
	ylist=[]
	vlist=[]

#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 7, 1), date(year, 8, 1), timedelta(days=1)):
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
			if float(liste2[position]) > 0.0:
				counter=counter + 1
				position=position+1
			else:
				position=position+1
#		print liste2

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
#		vergleich=0
#		ylist.append(year)
#		vergleich=100/len(liste2)*counter
#		vlist.append(vergleich)
#		print len(liste2)
#		print counter
#		print liste2
		year=year+1
	return ergebnis
	
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	

#3.Teil der Mae: 2. Regel
def mae2_rup_regen(csv_werte):
	
#Zuerst wird das benötigte Datumintervall erezugt

	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
#	dict={}
#	liste1=[]
	ergebnis=[]
	year=1990
	
	ylist=[]
	vlist=[]

#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 3, 28), date(year, 3, 29), timedelta(days=1)):
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
			if float(liste2[position]) > 0.0:
				counter=counter + 1
				position=position+1
			else:
				position=position+1
#		print liste2

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
#		vergleich=0
#		ylist.append(year)
#		vergleich=100/len(liste2)*counter
#		vlist.append(vergleich)
#		print len(liste2)
#		print counter
#		print liste2
		year=year+1
	return ergebnis

#4.Teil der Mae: 2. Regel
def mae2_juli_regen(csv_werte):
	
#Zuerst wird das benötigte Datumintervall erezugt

	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
#	dict={}
#	liste1=[]
	ergebnis=[]
	year=1990
	
	ylist=[]
	vlist=[]

#In der folgenden while Schleife werden die gleichen Intervalle in unterschiedlichen Jahren max. 1990-2015 erzeugt.
	while year<2016:
		datumliste=[]
		liste2=[]
		for result in intervall(date(year, 7, 1), date(year, 8, 1), timedelta(days=1)):
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
			if float(liste2[position]) > 0.0:
				counter=counter + 1
				position=position+1
			else:
				position=position+1
#		print liste2

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
#		vergleich=0
#		ylist.append(year)
#		vergleich=100/len(liste2)*counter
#		vlist.append(vergleich)
#		print len(liste2)
#		print counter
#		print liste2
		year=year+1
	return ergebnis


#Funtionen zum zeichnen der Diagramme:
def balkendia (werte):
	ywerte=[]
	xwerte=[]
	zwerte=[]
	x=0
	y=1
	z=2
	
	while x < len(werte):
		xwerte.append(werte[x])
		ywerte.append(werte[y])
		zwerte.append(100/float(werte[z])*float(werte[y]))
		x=x+3
		y=y+3
		z=z+3
		
	fig=plt.figure()
	plt.bar(xwerte,zwerte)
	plt.xticks(xwerte,rotation=45, ha='right')
	plt.tight_layout()
	plt.show()	
	
def balkendia2 (werte1, werte2, werte3):
	ywerte=[]
	xwerte=[]
	zwerte=[]
	x=0
	y=1
	z=2
	
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte.append(werte1[y]+werte2[y]+werte3[y])
		zwerte.append(100/float(werte1[z]+werte2[z]+werte3[z])*float(werte1[y]+werte2[y]+werte3[y]))
		x=x+3
		y=y+3
		z=z+3
	print zwerte
			
			
	
	fig=plt.figure()
	plt.bar(xwerte,zwerte)
	plt.xticks(xwerte,rotation=45, ha='right')
	plt.tight_layout()
	plt.show()	

#Funktion zur Generierung eines addiven Diagramms

#Diagramm mit 2 Werten:
def adidia2 (werte1, werte2, namen, titel):
	ywerte1=[]
	ywerte2=[]
	xwerte=[]
	x=0
	y=1
	z=2
	maxwert=werte1[z]+werte2[z]
	
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(werte1[y])
		ywerte2.append(werte2[y])
#		ywerte.append(100/float(werte1[z]+werte2[z]+werte3[z])*float(werte1[y]+werte2[y]+werte3[y]))
		x=x+3
		y=y+3
		z=z+3
		
	print ywerte1,ywerte2
	
	ind = np.arange(len(xwerte))
	width=0.35
	
	p1=plt.bar(ind, ywerte1, width, color='r')
	p2=plt.bar(ind, ywerte2, width, color='b', bottom=ywerte1)
	
	plt.legend((p1[0],p2[0]), namen)
	plt.ylabel('Zutreffende Werte (Anzahl Tage)')
	#plt.xlabel('Jahreszahlen')
	plt.title(titel)
	plt.xticks(ind+width/2., xwerte, rotation=45)
	plt.yticks(np.arange(0,maxwert+1,10))
	plt.axhline(y=maxwert/2)
	
	plt.show()

#Diagramm mit drei Werten:
def adidia3 (werte1, werte2, werte3, namen, titel):
	ywerte1=[]
	ywerte2=[]
	ywerte3=[]
	xwerte=[]
	x=0
	y=1
	z=2
	maxwert=werte1[z]+werte2[z]+werte3[z]
	
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(werte1[y])
		ywerte2.append(werte2[y])
		ywerte3.append(werte3[y])
#		ywerte.append(100/float(werte1[z]+werte2[z]+werte3[z])*float(werte1[y]+werte2[y]+werte3[y]))
		x=x+3
		y=y+3
		z=z+3
		
	print ywerte1,ywerte2,ywerte3
	
	ind = np.arange(len(xwerte))
	width=0.35
	
	p1=plt.bar(ind, ywerte1, width, color='r')
	p2=plt.bar(ind, ywerte2, width, color='b', bottom=ywerte1)
	p3=plt.bar(ind, ywerte3, width, color='y', bottom=[i+j for i, j in zip(ywerte1,ywerte2)])
	
	plt.legend((p1[0],p2[0],p3[0]), namen)
	plt.ylabel('Zutreffende Werte (Anzahl Tage)')
	#plt.xlabel('Jahreszahlen')
	plt.title(titel)
	plt.xticks(ind+width/2., xwerte, rotation=45)
	plt.yticks(np.arange(0,maxwert+1,10))
	plt.axhline(y=maxwert/2)
	
	
	plt.show()
	

#Funktion zur Bewertung der Wetterweisheiten und Bauernregeln:
#Jan: 1. Regel: Ist der Januar hell und weiß, wird der Sommer sicher heiß.
def bewertung_jan1 (werte1,werte2,werte3):
	ywerte1=[]
	ywerte2=[]
	ywerte3=[]
	xwerte=[]
	x=0
	y=1
	z=2
	refwert1=float(werte1[z])/100*60
	refwert2=float(werte2[z])/100*60
	refwert3=float(werte3[z])/100*60
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(float(werte1[y]))
		ywerte2.append(float(werte2[y]))
		ywerte3.append(float(werte3[y]))
		x=x+3
		y=y+3
		z=z+3
		
	x=0
	while x < len(xwerte):
		if (ywerte1[x] >= refwert1 or ywerte2[x] >= refwert2) and ywerte3[x] >= refwert3:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft zu"
			x=x+1
		else:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft nicht zu"
			x=x+1

#Jan: 2.Regel: Lässt der Januar Regen fallen, lässt der Lenz es gefrieren.
def bewertung_jan2 (werte1,werte2):
	ywerte1=[]
	ywerte2=[]
	xwerte=[]
	x=0
	y=1
	z=2
	refwert1=float(werte1[z])/100*60
	refwert2=float(werte2[z])/100*60/3
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(float(werte1[y]))
		ywerte2.append(float(werte2[y]))
		x=x+3
		y=y+3
		z=z+3
		
	x=0
	while x < len(xwerte):
		if ywerte1[x] >= refwert1 and ywerte2[x] >= refwert2:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x]
			print xwerte[x], "trifft zu"
			x=x+1
		else:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x]
			print xwerte[x], "trifft nicht zu"
			x=x+1



#Jan: 3.Regel: Friert es auf Vigilius (31.01.), im Märzen Kälte kommen muss.
def bewertung_jan3 (werte1,werte2):
	ywerte1=[]
	ywerte2=[]
	xwerte=[]
	x=0
	y=1
	z=2
	refwert1=float(werte1[z])
	refwert2=float(werte2[z])/100*60
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(float(werte1[y]))
		ywerte2.append(float(werte2[y]))
		x=x+3
		y=y+3
		z=z+3
		
	x=0
	while x < len(xwerte):
		if ywerte1[x] >= refwert1 and ywerte2[x] >= refwert2:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x]
			print xwerte[x], "trifft zu"
			x=x+1
		else:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x]
			print xwerte[x], "trifft nicht zu"
			x=x+1


#Feb: 1. Regel: Scheint an Lichtmess (02.02.) die Sonne heiß, kommt noch sehr viel Schnee und Eis.
def bewertung_feb1 (werte1,werte2,werte3):
	ywerte1=[]
	ywerte2=[]
	ywerte3=[]
	xwerte=[]
	x=0
	y=1
	z=2
	refwert1=float(werte1[z])
	refwert2=float(werte2[z])/100*30
	refwert3=float(werte3[z])/100*30
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(float(werte1[y]))
		ywerte2.append(float(werte2[y]))
		ywerte3.append(float(werte3[y]))
		x=x+3
		y=y+3
		z=z+3
		
	x=0
	while x < len(xwerte):
		if ywerte1[x] == refwert1 and (ywerte2[x] >= refwert2 or ywerte3[x] >= refwert3):
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft zu"
			x=x+1
		else:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft nicht zu"
			x=x+1


#Feb. 2. Regel: Im Februar Schnee und Eis, macht den Sommer lang und heiss.
def bewertung_feb2 (werte1,werte2,werte3):
	ywerte1=[]
	ywerte2=[]
	ywerte3=[]
	xwerte=[]
	x=0
	y=1
	z=2
	refwert1=float(werte1[z])/100*60
	refwert2=float(werte2[z])/100*60
	refwert3=float(werte3[z])/100*60
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(float(werte1[y]))
		ywerte2.append(float(werte2[y]))
		ywerte3.append(float(werte3[y]))
		x=x+3
		y=y+3
		z=z+3
		
	x=0
	while x < len(xwerte):
		if (ywerte1[x] == refwert1 or (ywerte2[x] >= refwert2) and ywerte3[x] >= refwert3):
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft zu"
			x=x+1
		else:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft nicht zu"
			x=x+1
	

#Mae: 1. Regel: Im März viel Schnee und Regen bringt wenig Sommersegen.
def bewertung_mae1 (werte1,werte2,werte3):
	ywerte1=[]
	ywerte2=[]
	ywerte3=[]
	xwerte=[]
	x=0
	y=1
	z=2
	refwert1=float(werte1[z])/100*30
	refwert2=float(werte2[z])/100*60
	refwert3=float(werte3[z])/100*40
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(float(werte1[y]))
		ywerte2.append(float(werte2[y]))
		ywerte3.append(float(werte3[y]))
		x=x+3
		y=y+3
		z=z+3
		
	x=0
	while x < len(xwerte):
		if (ywerte1[x] == refwert1 or (ywerte2[x] >= refwert2) and ywerte3[x] <= refwert3):
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft zu"
			x=x+1
		else:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft nicht zu"
			x=x+1
			


#Mae: 2. Regel: Hält St. Ruprecht (28.03.) den Himmel rein, so wird es auch im Juli sein.
def bewertung_mae2 (werte1,werte2):
	ywerte1=[]
	ywerte2=[]
	xwerte=[]
	x=0
	y=1
	z=2
	refwert1=float(werte1[z])
	refwert2=float(werte2[z])/100*40
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(float(werte1[y]))
		ywerte2.append(float(werte2[y]))
		x=x+3
		y=y+3
		z=z+3
		
	x=0
	while x < len(xwerte):
		if ywerte1[x] < refwert1 and ywerte2[x] <= refwert2:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x]
			print xwerte[x], "trifft zu"
			x=x+1
		else:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x]
			print xwerte[x], "trifft nicht zu"
			x=x+1

	

#Hier werden nun erst die "wertedict" mit den benötigten CSV-Daten erzeugt und anschließend die Funktion mit dem entsprechenden wertedict ausgeführt.

werte_lt_max =	csv_werte ("CSVs/Lufttemp_Max_0915.csv", 2,3)
werte_lt_min = csv_werte ("CSVs/Lufttemp_Min_0915.csv", 2,3)
werte_lt_mittel= csv_werte ("CSVs/Lufttemp_Mittel_0915.csv", 2,3)
werte_schnee = csv_werte ("CSVs/Neuschnee_0915.csv", 2,3)
werte_niederschlag = csv_werte ("CSVs/Niederschlag_0915.csv", 2,3)
werte_sonne = csv_werte ("CSVs/Sonnenschein_0915.csv", 2,3)



#balkendia(jan1_sommer_heiss(w3))
#balkendia2(jan1_hell_weiss(w1),jan1_hell_weiss(w2),jan1_sommer_heiss(w3))

#Jan: 1. Regel: Ist der Januar hell und weiß, wird der Sommer sicher heiß.
#adidia3(jan1_hell(werte_sonne),jan1_weiss(werte_schnee),jan1_sommer_heiss(werte_lt_max), ['Jan. Sonnenschein', 'Jan. Schnee', 'Sommer heisse Tage'], 'Auswertung 1. Jan. Weisheit/Regel')
#Jan: 2.Regel: Lässt der Januar Regen fallen, lässt der Lenz es gefrieren.
#adidia2(jan2_regen(werte_niederschlag),jan2_lenz_frost(werte_lt_min), ['Jan. Regen', 'Lenz Frost'], 'Auswertung 2. Jan. Weisheit/Regel')
#Jan: 3.Regel: Friert es auf Vigilius (31.01.), im Märzen Kälte kommen muss.
#adidia2(jan3_vigilius(werte_lt_min),jan3_maerz_kalt(werte_lt_mittel), ['Friert Vigilius (31.01.)', 'Kaelte Maerz'], 'Auswertung 3. Jan. Weisheit/Regel')

#Feb: 1. Regel: Scheint an Lichtmess (02.02.) die Sonne heiß, kommt noch sehr viel Schnee und Eis.
#adidia3(feb1_lichtmess_sonne(werte_sonne),feb1_kommt_schnee(werte_schnee),feb1_kommt_eis(werte_lt_min), ['Lichtmess (02.02.) Sonnenschein', 'bis Ende Maerz Schnee', 'bis Ende Maerz Eis'], 'Auswertung 1. Feb. Weisheit/Regel')
#Feb. 2. Regel: Im Februar Schnee und Eis, macht den Sommer lang und heiss.
#adidia3(feb2_feb_schnee(werte_schnee),feb2_feb_eis(werte_lt_min),jan1_sommer_heiss(werte_lt_max), ['Feb. Schnee', 'Feb. Eis', 'Sommer heiss'], 'Auswertung 2. Feb. Weisheit/Regel')

#Mae: 1. Regel: Im März viel Schnee und Regen bringt wenig Sommersegen.
#adidia3(mae1_mae_schnee(werte_schnee),mae1_mae_regen(werte_niederschlag),jan1_sommer_heiss(werte_lt_max), ['Mae. Schnee', 'Mae. Regen', 'Sommersegen'], 'Auswertung 1. Mae. Weisheit/Regel')
#Mae: 2. Regel: Hält St. Ruprecht (28.03.) den Himmel rein, so wird es auch im Juli sein.
#adidia2(mae2_rup_sonne(werte_niederschlag, werte_sonne),mae2_juli_sonne(werte_sonne), ['St.Ruprecht (28.03.) Sonne', 'Juli Sonne'], 'Auswertung 2. Mae. Weisheit/Regel 1.Teil')
#adidia2(mae2_rup_regen(werte_niederschlag),mae2_juli_regen(werte_niederschlag), ['St.Ruprecht (28.03.) Regen', 'Juli Regen'], 'Auswertung 2. Mae. Weisheit/Regel 2.Teil')

#Bewertung:
#Jan: 1. Regel: Ist der Januar hell und weiß, wird der Sommer sicher heiß.
#bewertung_jan1(jan1_hell(werte_sonne),jan1_weiss(werte_schnee),jan1_sommer_heiss(werte_lt_max))
#Jan: 2.Regel: Lässt der Januar Regen fallen, lässt der Lenz es gefrieren.
#bewertung_jan2(jan2_regen(werte_niederschlag),jan2_lenz_frost(werte_lt_min))
#Jan: 3.Regel: Friert es auf Vigilius (31.01.), im Märzen Kälte kommen muss.
#bewertung_jan3(jan3_vigilius(werte_lt_min),jan3_maerz_kalt(werte_lt_mittel))

#Feb: 1. Regel: Scheint an Lichtmess (02.02.) die Sonne heiß, kommt noch sehr viel Schnee und Eis.
#bewertung_feb1(feb1_lichtmess_sonne(werte_sonne),feb1_kommt_schnee(werte_schnee),feb1_kommt_eis(werte_lt_min))
#Feb. 2. Regel: Im Februar Schnee und Eis, macht den Sommer lang und heiss.
#bewertung_feb2(feb2_feb_schnee(werte_schnee),feb2_feb_eis(werte_lt_min),jan1_sommer_heiss(werte_lt_max))

#Mae: 1. Regel: Im März viel Schnee und Regen bringt wenig Sommersegen.
#bewertung_mae1(mae1_mae_schnee(werte_schnee),mae1_mae_regen(werte_niederschlag),jan1_sommer_heiss(werte_lt_max))
#Mae: 2. Regel: Hält St. Ruprecht (28.03.) den Himmel rein, so wird es auch im Juli sein.
#bewertung_mae2(mae2_rup_regen(werte_niederschlag),mae2_juli_regen(werte_niederschlag))
