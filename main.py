#Openingszinnen
print ("Welkom bij galgje!")
print ("Ik denk aan een woord. Raad het woord door letters te raden.")

#Defineren van functies
fouten = 0
geraden = 0

#Woord Kiezer
def woord_kiezer ():
  WoordLijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]
  import random
  woord = random.choice(WoordLijst)
  return woord

def WoordRaden (woord):
  KiesLetter = input("Kies een Letter: ")
  if KiesLetter in woord:
   
    
# Lengte van het woord
def woord_lengte (woord):
  LengteWoord = len(woord)
  return LengteWoord
  
print ("Het woord heeft " + str(woord_lengte) + " letters.")