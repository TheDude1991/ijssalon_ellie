from helper import *

def presenteer(dictionary, totaal):
    for key, value in dictionary.items():
        print(f"{key} : {value} euro")

    print("=" * 30)
    
    print(f"Totaal : {totaal} euro")

