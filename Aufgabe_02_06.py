#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen einfachen Taschenrechner

# Ihr Taschenrechner soll folgende Funktionen unterstützen:
# - Addition (+)
# - Subtraktion (-)
# - Multiplikation (*)
# - Division (/)

# Der Benutzer sollte aufgefordert werden, zwei Zahlen einzugeben.
# Anschließend sollte der Benutzer die gewünschte Operation wählen können.

# Beispielablauf:
# 1. Benutzer gibt die erste Zahl ein.
# 2. Benutzer gibt die zweite Zahl ein.
# 3. Benutzer wählt die Operation (+, -, *, /).
# 4. Das Programm führt die Berechnung durch und gibt das Ergebnis aus.

# Optional: Erweitern Sie den Taschenrechner um weitere Funktionen wie Potenzierung oder Modulo.

ergebnis = 0

user_eingabe = []
user_eingabe.append(input("Bitte geben Sie eine Zahl ein "))

print(user_eingabe)




operator = user_eingabe.append(input("Bitte geben Sie (+, -, *, /, **, %) ein "))
while user_eingabe[1] not in ["+", "-", "*", "/", "**", "%"]:
  print("Eingabe Ungültig")
  user_eingabe[1] = input("Bitte geben Sie (+, -, *, /, **, %) ein ")





print(user_eingabe)


user_eingabe.append(input("Bitte geben Sie eine Zahl ein "))


addition = int(user_eingabe[0]) + int(user_eingabe[2])
subtraktion = int(user_eingabe[0]) - int(user_eingabe[2])
division = int(user_eingabe[0]) / int(user_eingabe[2])
multiplikation = int(user_eingabe[0]) * int(user_eingabe[2])
potenzierung = int(user_eingabe[0]) ** int(user_eingabe[2])
modulo = int(user_eingabe[0]) % int(user_eingabe[2])








print(user_eingabe)





if user_eingabe[1] == "+":
  ergebnis = addition
elif user_eingabe[1] == "-":
  ergebnis = subtraktion
elif user_eingabe[1] == "/":
  ergebnis = division
elif user_eingabe[1] == "*":
  ergebnis = multiplikation
elif user_eingabe[1] == "**":
  ergebnis = potenzierung
elif user_eingabe[1] == "%":
  ergebnis = modulo



else: 
  print("Eingabe ungültig, bitte geben Sie (+, -, *, /, **, %) ein")



print(f"Ergebnis: {ergebnis}")
