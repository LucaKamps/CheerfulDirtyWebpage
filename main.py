# Openingszinnen
print ("Welkom bij galgje!")
print ("Ik denk aan een woord. Raad het woord door letters te raden. Je mag maximaal 5 fouten maken.")

# Woord Kiezer
def woord_kiezer ():
  WoordLijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

  # Hier wordt een willekurig woord uit de lijst gekozen
  import random
  woord = random.choice(WoordLijst)
  return woord
   
# Lengte van het woord
def woord_lengte(woord):
  return len(woord)

def GeradenAntwoord(woord, geradenLetters):
  # Maakt een string met de letters die geraden zijn en underscores voor de letters die nog niet geraden zijn
  
  gesloten_woord = ""
  # Eerst legen we de string gesloten_woord
  
  for letter in woord:
  # We lopen alle letters van het woord af
    
    if letter in geradenLetters:
      # Als de letter in de geraden letters zit, dan voegen we deze letter toe aan gesloten_woord
      gesloten_woord += letter
    else:
      # Als de letter niet in de geraden letters zit, dan voegen we een underscore toe aan gesloten_woord
      gesloten_woord += "-"
  return gesloten_woord
    
# Hoofdprogramma
def Hoofdprogramma ():
  woord = woord_kiezer()
  woordLengte = woord_lengte(woord)
  geradenLetters = set()
  # We maken een lege set aan voor de geraden letters
  
  geprobeerdeLetters = list()
  # Een lijst om de geprobeerde letters op te slaan, om ze later te kunnen printen
  
  fouten = 0
  MaxFouten = 5
  
  print ("Het woord heeft " + str(woordLengte) + " letters.")
  # We printen de lengte van het woord

  while fouten < MaxFouten:
    # We lopen door de while loop totdat de gebruiker het woord heeft geraden of de maximale aantal fouten heeft bereikt
    GeradenAntwoordString = GeradenAntwoord(woord, geradenLetters)
    geprobeerdeLetters.sort()
    # We sorteren de geprobeerde letters op alfabetische volgorde
    
    print ("woord: " + GeradenAntwoordString)
    print ("Fouten: " + str(fouten))
    print ("Geprobeerde letters: " + ", ".join(geprobeerdeLetters))
    # We printen het woord met de geraden letters, we gebruiken de join functie om de lijst om te zetten naar een string en een komma tussen de letters te zetten, oftewel een seperator.
    
    if "-" not in GeradenAntwoordString:
      # Als er geen underscores meer in de string zitten, dan is het woord geraden
      # We printen het woord en vragen of de gebruiker opnieuw wil spelen
     print("Je hebt het woord geraden: ", woord)
     Opnieuw = input("typ 'ja' als je door wil spelen en 'nee' als je wil stoppen: ")
     if Opnieuw == "ja":
        Hoofdprogramma()
     elif Opnieuw == "nee":
        print("Bedankt voor het spelen!")
     else:
        print("Ongeldige invoer. Het spel wordt afgesloten.")
     return

    letter = input("Raad een letter: ").lower()
    # We vragen de gebruiker om een letter te raden en zetten deze om naar kleine letters
    
    if len(letter) > 1:
      # Als de gebruiker meer dan 1 letter invoert, dan is er een fout
      fouten += 1
      print("Je mag alleen 1 letter invoeren. Je krijgt een fout")
      
    elif letter.isdigit():
      # Als de gebruiker een cijfer invoert moet deze opniew proberen. We maken gebruik van de functie isdigit.
      print("Je mag alleen letters invoeren. probeer opnieuw")
      
    else:
      
      if letter not in geprobeerdeLetters:
       geprobeerdeLetters.append(letter)

      geradenLetters.add(letter)
      # We voegen de geraden letter toe aan de set geradenLetters
  
      if letter not in woord:
        # Als de letter niet in het woord zit, dan is er een fout
          fouten += 1
          
      else:
         print("Goed geraden!")
          
  # We printen het woord en vragen of de gebruiker opnieuw wil spelen
  print("Je hebt het woord niet geraden. Het woord was: ", woord)

  opnieuw = input("typ 'ja' als je door wil spelen en 'nee' als je wil stoppen: ")
  if opnieuw == "ja":
    Hoofdprogramma()
  elif opnieuw == "nee":
    print("Bedankt voor het spelen!")
  else:
    print("Ongeldige invoer. Het spel wordt afgesloten.")

Hoofdprogramma()

    