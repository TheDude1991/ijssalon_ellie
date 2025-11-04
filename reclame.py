from algemene_functie import mijn_functie_2

def aandieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de {smaak}, van {prijs}, voor {nieuwe_prijs:.2f} euro."
    return uitvoer

print(aandieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw_percentage):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw_percentage
    uitvoer = f"Het totaal van alle inkomsten van deze week is €{totaal}, waarover €{btw_bedrag:.2f} btw betaald dient te worden"
    return uitvoer
    
inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(inkomsten_totaal(inkomsten, 0.09))

def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [laagste, hoogste]

print(laag_en_hoog(inkomsten))

from statistics import mean

def gemiddelde(mijn_lijst):
    gemiddeld = mean(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten deze week zijn €{gemiddeld:.2f}."
    return uitvoer

print(gemiddelde(inkomsten))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

print(meervoudig([10, 5, 3, 2, 1, 2, 9]))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

resultaat = combinatie([10, 5, 3, 2, 1, 2, 9])
print(resultaat)
