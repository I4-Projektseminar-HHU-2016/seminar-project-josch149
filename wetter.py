# -*- coding: utf-8 -*-
import csv
from datetime import date, datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

# Hier werden die Werte aus der .CSV gelesen und für die weitere Verarbeitung gespeichert.
def csv_werte (datei, spalte1, spalte2):
	liste0=[]

	wertedict={}
	with open (datei, 'r') as data_file:
		reader = csv.reader(data_file, delimiter=';')
		for row in reader:
			liste0.append(row)
		for element in liste0:
#			
			wertedict.update({element[spalte1]:element[spalte2]})


# Im wertedict sind die Datumangaben als Schlüssel und die spezifischen Daten als Value enthalten und werden zurückgegeben.
		return wertedict


# Folgedes Segment stammt von: http://stackoverflow.com/questions/10688006/generate-a-list-of-datetimes-between-an-interval abgerufen am 23.08.2016
# Mit dieser Funktion können Datumsintervalle generiert werden.
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
				liste2.append(csv_werte[element])
			

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
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
				liste2.append(csv_werte[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
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
				liste2.append(csv_werte[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
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
				liste2.append(csv_werte[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
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
				liste2.append(csv_werte[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
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
				liste2.append(csv_werte[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
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
				liste2.append(csv_werte[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
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
				liste2.append(csv_werte[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
		year=year+1
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	return ergebnis
	
	

#2.Teil der Feb: 1. Regel
def feb1_kommt_schnee(csv_werte):
	
#Zuerst wird das benötigte Datumintervall erezugt

	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
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
				liste2.append(csv_werte[element])
				

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
				

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
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
				liste2.append(csv_werte[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
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
				liste2.append(csv_werte[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		year=year+1
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	return ergebnis
	
	

#2.Teil der Feb: 1. Regel
def feb2_feb_eis(csv_werte):
	
#Zuerst wird das benötigte Datumintervall erezugt

	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
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
				liste2.append(csv_werte[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
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
				liste2.append(csv_werte[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
		year=year+1
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	return ergebnis

	

#2.Teil der Mae: 1. Regel
def mae1_mae_regen(csv_werte):
	
#Zuerst wird das benötigte Datumintervall erezugt

	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
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
				liste2.append(csv_werte[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
		year=year+1
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
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
				liste2.append(csv_werte1[element])
				
			if element in csv_werte2.iterkeys():
				liste3.append(csv_werte2[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
		year=year+1

#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	return ergebnis
	
	
	
#2.Teil der Mae: 2. Regel
def mae2_juli_sonne(csv_werte):
	
#Zuerst wird das benötigte Datumintervall erezugt

	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
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
				liste2.append(csv_werte[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
		year=year+1
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	return ergebnis
	
	

#3.Teil der Mae: 2. Regel
def mae2_rup_regen(csv_werte):
	
#Zuerst wird das benötigte Datumintervall erezugt

	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
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
				liste2.append(csv_werte[element])
				
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
		year=year+1
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	return ergebnis
	
	

#4.Teil der Mae: 2. Regel
def mae2_juli_regen(csv_werte):
	
#Zuerst wird das benötigte Datumintervall erezugt

	def intervall(start, ende, delta):
		while start < ende:
			yield start
			start += delta
	datumliste=[]
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
				liste2.append(csv_werte[element])
				

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

#Nun werden in der Liste "ergebnis" das Jahr, die Anzahl an entsprechenden Werten und die max. Anzahl der möglichen Werte gespeichert.
		ergebnis.append(year)
		ergebnis.append(counter)
		ergebnis.append(len(liste2))
		
		
		year=year+1
		
#In der Liste "ergenis" wird das ergebnis (Jahr, entsprechenede Elemente, max. Anzahl möglicher Elemente) zurück gegeben.
	return ergebnis


#Funtionen zum zeichnen der Diagramme:

#Tortendiagramm zur visuellen Darstellung wie zutreffend die Weisheiten bzw. egeln sind.
def tortendia (werte1,werte2,titel):
	labels = 'trifft zu','trifft nicht zu'
	sizes = [werte1,werte2]
	colors = ['b','r']
	plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=180)
	plt.title(titel)
	plt.axis('equal')
	plt.show()

#Balkendiagramm1 noch als Backup von früherer Version.
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


#Balkendiagramm2 noch als Backup von früherer Version.
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

#Funktion zur Generierung von addiven Diagrammen

#Diagramm mit 2 Werten:
def adidia2 (werte1, werte2, namen, titel):
	ywerte1=[]
	ywerte2=[]
	xwerte=[]
	x=0
	y=1
	z=2

#maxwert als Skala der y-Achsen Werte (werte1[z] und werte2[z] sind die maximalen Werte von werte1 und werte2)
	maxwert=werte1[z]+werte2[z]

#in dieser Schleife werden die Werte der einzelenen Teile eine Weisheit/Regel für jedes Jahr zusammengeführt.	
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(werte1[y])
		ywerte2.append(werte2[y])
		x=x+3
		y=y+3
		z=z+3
		
	print ywerte1,ywerte2

#nun wird das additive Diagramm erstellt, indem die Teilwerte für jedes Jahr als Säulen aufeinander gestellt werden.
	ind = np.arange(len(xwerte))
	width=0.35
	
	p1=plt.bar(ind, ywerte1, width, color='r')
	p2=plt.bar(ind, ywerte2, width, color='b', bottom=ywerte1)
	
	plt.legend((p1[0],p2[0]), namen)
	plt.ylabel('Zutreffende Werte (Anzahl Tage)')
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

#maxwert als Skala der y-Achsen Werte (werte1[z], werte2[z] und wertte3[z] sind die maximalen Werte von werte1, werte2 und werte3)
	maxwert=werte1[z]+werte2[z]+werte3[z]


#in dieser Schleife werden die Werte der einzelenen Teile eine Weisheit/Regel für jedes Jahr zusammengeführt.		
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(werte1[y])
		ywerte2.append(werte2[y])
		ywerte3.append(werte3[y])
		x=x+3
		y=y+3
		z=z+3
		
	print ywerte1,ywerte2,ywerte3


#nun wird das additive Diagramm erstellt, indem die Teilwerte für jedes Jahr als Säulen aufeinander gestellt werden.
	ind = np.arange(len(xwerte))
	width=0.35
	
	p1=plt.bar(ind, ywerte1, width, color='r')
	p2=plt.bar(ind, ywerte2, width, color='b', bottom=ywerte1)
	p3=plt.bar(ind, ywerte3, width, color='y', bottom=[i+j for i, j in zip(ywerte1,ywerte2)])
	
	plt.legend((p1[0],p2[0],p3[0]), namen)
	plt.ylabel('Zutreffende Werte (Anzahl Tage)')
	plt.title(titel)
	plt.xticks(ind+width/2., xwerte, rotation=45)
	plt.yticks(np.arange(0,maxwert+1,10))
	plt.axhline(y=maxwert/2)
	
	
	plt.show()
	

#Funktion zur Bewertung der Wetterweisheiten und Bauernregeln:
#Jan: 1. Regel: Ist der Januar hell und weiss, wird der Sommer sicher heiss.
def bewertung_jan1 (werte1,werte2,werte3,titel):
	ywerte1=[]
	ywerte2=[]
	ywerte3=[]
	xwerte=[]
	x=0
	y=1
	z=2

#60% als Referenzwert festgelegt um mehr als Durchschnitt 50% zu definieren.
	refwert1=float(werte1[z])/100*60
	refwert2=float(werte2[z])/100*60
	refwert3=float(werte3[z])/100*60
	
#in dieser Schleife werden die Werte der einzelnen Segmente der Weisheit/Regel in verschiedenen Listen gespeichert.
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(float(werte1[y]))
		ywerte2.append(float(werte2[y]))
		ywerte3.append(float(werte3[y]))
		x=x+3
		y=y+3
		z=z+3
		
	x=0
	count_wahr=0
	count_falsch=0
	
#in dieser Schleife wird geprüft, ob die Weisheit/Regel in den einzelnen Jahren zu treffen, oder nicht. 
#Dabei muss der jeweilige Wert über dem Referenzwert liegen.
	while x < len(xwerte):
		if (ywerte1[x] >= refwert1 or ywerte2[x] >= refwert2) and ywerte3[x] >= refwert3:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft zu"
			count_wahr=count_wahr+1
			x=x+1
		else:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft nicht zu"
			count_falsch=count_falsch+1
			x=x+1

#hier wird das entsprechende Tortendiagramm erstellt.
	tortendia(count_wahr,count_falsch,titel)



#Jan: 2.Regel: Laesst der Januar Regen fallen, laesst der Lenz es gefrieren.
def bewertung_jan2 (werte1,werte2,titel):
	ywerte1=[]
	ywerte2=[]
	xwerte=[]
	x=0
	y=1
	z=2
	
#60% als Referenzwert festgelegt um mehr als Durchschnitt 50% zu definieren (der 2. Wert wird durch 3 geteilt, da es in Duesseldorf im Frühjahr selten friert und somit ein angepasstes Verhältniss geschaffen wird)
	refwert1=float(werte1[z])/100*60
	refwert2=float(werte2[z])/100*60/3
	
#in dieser Schleife werden die Werte der einzelnen Segmente der Weisheit/Regel in verschiedenen Listen gespeichert.
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(float(werte1[y]))
		ywerte2.append(float(werte2[y]))
		x=x+3
		y=y+3
		z=z+3
		
	x=0
	count_wahr=0
	count_falsch=0

#in dieser Schleife wird geprüft, ob die Weisheit/Regel in den einzelnen Jahren zu treffen, oder nicht. Dabei muss der jeweilige Wert über dem Referenzwert liegen.
	while x < len(xwerte):
		if ywerte1[x] >= refwert1 and ywerte2[x] >= refwert2:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x]
			print xwerte[x], "trifft zu"
			count_wahr=count_wahr+1
			x=x+1
		else:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x]
			print xwerte[x], "trifft nicht zu"
			count_falsch=count_falsch+1
			x=x+1
	
#hier wird das entsprechende Tortendiagramm erstellt.			
	tortendia(count_wahr,count_falsch,titel)


#Jan: 3.Regel: Friert es auf Vigilius (31.01.), im Maerzen Kaelte kommen muss.
def bewertung_jan3 (werte1,werte2,titel):
	ywerte1=[]
	ywerte2=[]
	xwerte=[]
	x=0
	y=1
	z=2
	
#60% als Referenzwert festgelegt um mehr als Durchschnitt 50% zu definieren.
	refwert1=float(werte1[z])
	refwert2=float(werte2[z])/100*60
	
#in dieser Schleife werden die Werte der einzelnen Segmente der Weisheit/Regel in verschiedenen Listen gespeichert.
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(float(werte1[y]))
		ywerte2.append(float(werte2[y]))
		x=x+3
		y=y+3
		z=z+3
		
	x=0
	count_wahr=0
	count_falsch=0
	
#in dieser Schleife wird geprüft, ob die Weisheit/Regel in den einzelnen Jahren zu treffen, oder nicht. Dabei muss der jeweilige Wert über dem Referenzwert liegen.
	while x < len(xwerte):
		if ywerte1[x] >= refwert1 and ywerte2[x] >= refwert2:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x]
			print xwerte[x], "trifft zu"
			count_wahr=count_wahr+1
			x=x+1
		else:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x]
			print xwerte[x], "trifft nicht zu"
			count_falsch=count_falsch+1
			x=x+1

#hier wird das entsprechende Tortendiagramm erstellt.		
	tortendia(count_wahr,count_falsch,titel)


#Feb: 1. Regel: Scheint an Lichtmess (02.02.) die Sonne heiss, kommt noch sehr viel Schnee und Eis.
def bewertung_feb1 (werte1,werte2,werte3,titel):
	ywerte1=[]
	ywerte2=[]
	ywerte3=[]
	xwerte=[]
	x=0
	y=1
	z=2
	
#30% als Referenzwert festgelegt, da es in Duesseldorf im Frühjahr selten friert und somit ein angepasstes Verhältniss geschaffen wird.
	refwert1=float(werte1[z])
	refwert2=float(werte2[z])/100*30
	refwert3=float(werte3[z])/100*30
	
#in dieser Schleife werden die Werte der einzelnen Segmente der Weisheit/Regel in verschiedenen Listen gespeichert.
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(float(werte1[y]))
		ywerte2.append(float(werte2[y]))
		ywerte3.append(float(werte3[y]))
		x=x+3
		y=y+3
		z=z+3
		
	x=0
	count_wahr=0
	count_falsch=0
	
#in dieser Schleife wird geprüft, ob die Weisheit/Regel in den einzelnen Jahren zu treffen, oder nicht. Dabei muss der jeweilige Wert über dem Referenzwert liegen.
	while x < len(xwerte):
		if ywerte1[x] == refwert1 and (ywerte2[x] >= refwert2 or ywerte3[x] >= refwert3):
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft zu"
			count_wahr=count_wahr+1
			x=x+1
		else:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft nicht zu"
			count_falsch=count_falsch+1
			x=x+1

#hier wird das entsprechende Tortendiagramm erstellt.
	tortendia(count_wahr,count_falsch,titel)


#Feb. 2. Regel: Im Februar Schnee und Eis, macht den Sommer lang und heiss.
def bewertung_feb2 (werte1,werte2,werte3,titel):
	ywerte1=[]
	ywerte2=[]
	ywerte3=[]
	xwerte=[]
	x=0
	y=1
	z=2
	
#60% als Referenzwert festgelegt um mehr als Durchschnitt 50% zu definieren.
	refwert1=float(werte1[z])/100*60
	refwert2=float(werte2[z])/100*60
	refwert3=float(werte3[z])/100*60
	
#in dieser Schleife werden die Werte der einzelnen Segmente der Weisheit/Regel in verschiedenen Listen gespeichert.
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(float(werte1[y]))
		ywerte2.append(float(werte2[y]))
		ywerte3.append(float(werte3[y]))
		x=x+3
		y=y+3
		z=z+3
		
	x=0
	count_wahr=0
	count_falsch=0
	
#in dieser Schleife wird geprüft, ob die Weisheit/Regel in den einzelnen Jahren zu treffen, oder nicht. Dabei muss der jeweilige Wert über dem Referenzwert liegen.
	while x < len(xwerte):
		if (ywerte1[x] == refwert1 or (ywerte2[x] >= refwert2) and ywerte3[x] >= refwert3):
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft zu"
			count_wahr=count_wahr+1
			x=x+1
		else:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft nicht zu"
			count_falsch=count_falsch+1
			x=x+1
	
#hier wird das entsprechende Tortendiagramm erstellt.
	tortendia(count_wahr,count_falsch,titel)
	

#Mae: 1. Regel: Im Maerz viel Schnee und Regen bringt wenig Sommersegen.
def bewertung_mae1 (werte1,werte2,werte3,titel):
	ywerte1=[]
	ywerte2=[]
	ywerte3=[]
	xwerte=[]
	x=0
	y=1
	z=2
	
#30% als Referenzwert festgelegt, da es in Duesseldorf im Frühjahr selten schneit und somit ein angepasstes Verhältniss geschaffen wird.
#40% als Referenzwert festgelegt, damit der Sommer als wenig warm (weniger warme Tage als 40% der gesammten Sommertage)
	refwert1=float(werte1[z])/100*30
	refwert2=float(werte2[z])/100*60
	refwert3=float(werte3[z])/100*40
	
#in dieser Schleife werden die Werte der einzelnen Segmente der Weisheit/Regel in verschiedenen Listen gespeichert.
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(float(werte1[y]))
		ywerte2.append(float(werte2[y]))
		ywerte3.append(float(werte3[y]))
		x=x+3
		y=y+3
		z=z+3
		
	x=0
	count_wahr=0
	count_falsch=0
	
#in dieser Schleife wird geprüft, ob die Weisheit/Regel in den einzelnen Jahren zu treffen, oder nicht. Dabei muss der jeweilige Wert über dem Referenzwert liegen.
	while x < len(xwerte):
		if (ywerte1[x] == refwert1 or (ywerte2[x] >= refwert2) and ywerte3[x] <= refwert3):
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft zu"
			count_wahr=count_wahr+1
			x=x+1
		else:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x],refwert3,ywerte3[x]
			print xwerte[x], "trifft nicht zu"
			count_falsch=count_falsch+1
			x=x+1

#hier wird das entsprechende Tortendiagramm erstellt.	
	tortendia(count_wahr,count_falsch,titel)	


#Mae: 2. Regel: Haelt St. Ruprecht (28.03.) den Himmel rein, so wird es auch im Juli sein.
def bewertung_mae2 (werte1,werte2,titel):
	ywerte1=[]
	ywerte2=[]
	xwerte=[]
	x=0
	y=1
	z=2
	
#40% als Referenzwert festgelegt, damit der Juli weniger Regentage hat (weniger regen Tage als 40% der gesammten Juli Tage)
	refwert1=float(werte1[z])
	refwert2=float(werte2[z])/100*40
	
	
#in dieser Schleife werden die Werte der einzelnen Segmente der Weisheit/Regel in verschiedenen Listen gespeichert.
	while x < len(werte1):
		xwerte.append(werte1[x])
		ywerte1.append(float(werte1[y]))
		ywerte2.append(float(werte2[y]))
		x=x+3
		y=y+3
		z=z+3
		
	x=0
	count_wahr=0
	count_falsch=0
	
#in dieser Schleife wird geprüft, ob die Weisheit/Regel in den einzelnen Jahren zu treffen, oder nicht. Dabei muss der jeweilige Wert über dem Referenzwert liegen.
	while x < len(xwerte):
		if ywerte1[x] < refwert1 and ywerte2[x] <= refwert2:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x]
			print xwerte[x], "trifft zu"
			count_wahr=count_wahr+1
			x=x+1
		else:
			print xwerte[x],refwert1,ywerte1[x],refwert2,ywerte2[x]
			print xwerte[x], "trifft nicht zu"
			count_falsch=count_falsch+1
			x=x+1

#hier wird das entsprechende Tortendiagramm erstellt.
	tortendia(count_wahr,count_falsch,titel)
	

#Hier werden nun erst die "wertedict" mit den benötigten CSV-Daten erzeugt und anschließend die Funktion mit dem entsprechenden wertedict ausgeführt.

werte_lt_max =	csv_werte ("CSVs/Lufttemp_Max_0915.csv", 2,3)
werte_lt_min = csv_werte ("CSVs/Lufttemp_Min_0915.csv", 2,3)
werte_lt_mittel= csv_werte ("CSVs/Lufttemp_Mittel_0915.csv", 2,3)
werte_schnee = csv_werte ("CSVs/Neuschnee_0915.csv", 2,3)
werte_niederschlag = csv_werte ("CSVs/Niederschlag_0915.csv", 2,3)
werte_sonne = csv_werte ("CSVs/Sonnenschein_0915.csv", 2,3)



#balkendia(jan1_sommer_heiss(w3))
#balkendia2(jan1_hell_weiss(w1),jan1_hell_weiss(w2),jan1_sommer_heiss(w3))


#Darstellung der Weisheiten/Regeln als addive Diagramme:
#Jan: 1. Regel: Ist der Januar hell und weiß, wird der Sommer sicher heiß.
adidia3(jan1_hell(werte_sonne),jan1_weiss(werte_schnee),jan1_sommer_heiss(werte_lt_max), ['Jan. Sonnenschein', 'Jan. Schnee', 'Sommer heisse Tage'], 'Jan: 1. Regel: Ist der Januar hell und weiss, wird der Sommer sicher heiss.')
#Jan: 2.Regel: Lässt der Januar Regen fallen, lässt der Lenz es gefrieren.
adidia2(jan2_regen(werte_niederschlag),jan2_lenz_frost(werte_lt_min), ['Jan. Regen', 'Lenz Frost'], 'Jan: 2.Regel: Laesst der Januar Regen fallen, laesst der Lenz es gefrieren.')
#Jan: 3.Regel: Friert es auf Vigilius (31.01.), im Maerzen Kaelte kommen muss.
adidia2(jan3_vigilius(werte_lt_min),jan3_maerz_kalt(werte_lt_mittel), ['Friert Vigilius (31.01.)', 'Kaelte Maerz'], 'Jan: 3.Regel: Friert es auf Vigilius (31.01.), im Maerzen Kaelte kommen muss.')

#Feb: 1. Regel: Scheint an Lichtmess (02.02.) die Sonne heiss, kommt noch sehr viel Schnee und Eis.
adidia3(feb1_lichtmess_sonne(werte_sonne),feb1_kommt_schnee(werte_schnee),feb1_kommt_eis(werte_lt_min), ['Lichtmess (02.02.) Sonnenschein', 'bis Ende Maerz Schnee', 'bis Ende Maerz Eis'], 'Feb: 1. Regel: Scheint an Lichtmess (02.02.) die Sonne heiss, kommt noch sehr viel Schnee und Eis.')
#Feb. 2. Regel: Im Februar Schnee und Eis, macht den Sommer lang und heiss.
adidia3(feb2_feb_schnee(werte_schnee),feb2_feb_eis(werte_lt_min),jan1_sommer_heiss(werte_lt_max), ['Feb. Schnee', 'Feb. Eis', 'Sommer heiss'], 'Feb. 2. Regel: Im Februar Schnee und Eis, macht den Sommer lang und heiss.')

#Mae: 1. Regel: Im Maerz viel Schnee und Regen bringt wenig Sommersegen.
adidia3(mae1_mae_schnee(werte_schnee),mae1_mae_regen(werte_niederschlag),jan1_sommer_heiss(werte_lt_max), ['Mae. Schnee', 'Mae. Regen', 'Sommersegen'], 'Mae: 1. Regel: Im Maerz viel Schnee und Regen bringt wenig Sommersegen.')
#Mae: 2. Regel: Haelt St. Ruprecht (28.03.) den Himmel rein, so wird es auch im Juli sein.
adidia2(mae2_rup_sonne(werte_niederschlag, werte_sonne),mae2_juli_sonne(werte_sonne), ['St.Ruprecht (28.03.) Sonne', 'Juli Sonne'], 'Mae 2. Regel Teil 1: Haelt St. Ruprecht (28.03.) den Himmel rein, so wird es auch im Juli sein.')
adidia2(mae2_rup_regen(werte_niederschlag),mae2_juli_regen(werte_niederschlag), ['St.Ruprecht (28.03.) Regen', 'Juli Regen'], 'Mae 2. Regel Teil 2: Haelt St. Ruprecht (28.03.) den Himmel rein, so wird es auch im Juli sein.')

#Bewertung der Weisheiten/Regeln in der Konsole für jedes Jahr und graphisch als Tortendiagramm für alle Jahre:
#Jan: 1. Regel: Ist der Januar hell und weiss, wird der Sommer sicher heiss.
bewertung_jan1(jan1_hell(werte_sonne),jan1_weiss(werte_schnee),jan1_sommer_heiss(werte_lt_max),'Jan: 1. Regel: Ist der Januar hell und weiss, wird der Sommer sicher heiss.')
#Jan: 2.Regel: Laesst der Januar Regen fallen, laesst der Lenz es gefrieren.
bewertung_jan2(jan2_regen(werte_niederschlag),jan2_lenz_frost(werte_lt_min),'Jan: 2.Regel: Laesst der Januar Regen fallen, laesst der Lenz es gefrieren.')
#Jan: 3.Regel: Friert es auf Vigilius (31.01.), im Märzen Kälte kommen muss.
bewertung_jan3(jan3_vigilius(werte_lt_min),jan3_maerz_kalt(werte_lt_mittel),'Jan: 3.Regel: Friert es auf Vigilius (31.01.), im Maerzen Kaelte kommen muss.')

#Feb: 1. Regel: Scheint an Lichtmess (02.02.) die Sonne heiß, kommt noch sehr viel Schnee und Eis.
bewertung_feb1(feb1_lichtmess_sonne(werte_sonne),feb1_kommt_schnee(werte_schnee),feb1_kommt_eis(werte_lt_min),'Feb: 1. Regel: Scheint an Lichtmess (02.02.) die Sonne heiss, kommt noch sehr viel Schnee und Eis.')
#Feb. 2. Regel: Im Februar Schnee und Eis, macht den Sommer lang und heiss.
bewertung_feb2(feb2_feb_schnee(werte_schnee),feb2_feb_eis(werte_lt_min),jan1_sommer_heiss(werte_lt_max),'Feb. 2. Regel: Im Februar Schnee und Eis, macht den Sommer lang und heiss.')

#Mae: 1. Regel: Im Maerz viel Schnee und Regen bringt wenig Sommersegen.
bewertung_mae1(mae1_mae_schnee(werte_schnee),mae1_mae_regen(werte_niederschlag),jan1_sommer_heiss(werte_lt_max),'Mae: 1. Regel: Im Maerz viel Schnee und Regen bringt wenig Sommersegen.')
#Mae: 2. Regel: Haelt St. Ruprecht (28.03.) den Himmel rein, so wird es auch im Juli sein.
bewertung_mae2(mae2_rup_regen(werte_niederschlag),mae2_juli_regen(werte_niederschlag),'Mae: 2. Regel: Haelt St. Ruprecht (28.03.) den Himmel rein, so wird es auch im Juli sein.')
