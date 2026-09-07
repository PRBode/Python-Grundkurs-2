#!/usr/bin/env python3

### Eingabe über die Kommandozeile
#name = input("Bitte geben Sie Ihren Namen ein: ")
#print(f"Hallo, {name}!")

### Einlesen eines Integers und Umwandlung
#alter = input("Bitte geben Sie Ihr Alter ein: ")
#alter = int(alter)
#print(f"Sie sind,{alter} Jahre alt.")
#print("Sie sind " + str(alter) + "Jahre alt.") #Im Print sind nur Strings erlaubt. Mit "+" kann man Strings aneinanderketten

### Berechnung mit der Eingabe
#jahre_bis_30 = 30 - alter
#if jahre_bis_30 > 0:
#  print(f"In {jahre_bis_30} Jahren werden Sie 30.")
#else:
#  print("Sie sind bereits 30 Jahre alt oder älter.")



####  Aufgabe: Schreiben Sie ein Skript, das den Benutzer nach seinem Lieblingsfilm fragt
##### und nach seiner Lieblingszahl. Addieren Sie 14.5 zu dieser Zahl. Geben Sie 
####  dann eine personalisierte Nachricht aus, die diese Information enthält.


lieblingsfilm = input("Was ist ihr Lieblingsfilm? ")
#print(lieblingsfilm)
lieblingszahl = input("Was ist ihre Lieblingszahl? ")
#print(lieblingszahl)
lieblingszahl = float(lieblingszahl) + 14.5
#print(lieblingszahl)
print(f'Ihre Lieblingsfilm lautet "{lieblingsfilm}" und ihre Lieblingszahl addiert mit 14.5 lautet "{lieblingszahl}".')