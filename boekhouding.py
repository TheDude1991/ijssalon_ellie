from helper import som
from presentatie import *
import csv

inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}

from helper import som

totaal_inkomsten = som(inkomsten)
print(som(inkomsten))

presenteer(inkomsten, totaal_inkomsten)

#Ik kwam er niet helemaal uit en bleef foutmeldingen krijgen.
# AI heeft me hier mee opweg geholpen. Vandaar dat de volgorde is aangepast.
with open("boekhouding.csv","w",newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    for key, value in inkomsten.items():
        writer.writerow([key,value])

