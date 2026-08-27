#!/usr/bin/env python3

#variablen
x = 10
y = 5

# Einfache if-Bedingung
if x <= y:
  print("x ist größer als y")
else:
  print("x ist nicht kleiner als y")

#if-elif-else-Bedingung
if x == y:
  print("x ist gleich groß wie y")
elif x > y:
  print("x ist größer als y")
else:
  print("x ist nicht kleiner als y")

# Aufgabe 1:
# Legen Sie zwei Variablen mit verschiedenen float Zahlenwerten an.
# Schreiben Sie eine if-else-Bedingung, die prüft, ob die erste Zahl
# größer gleich oder kleiner der zweiten Zahl ist, und geben Sie das 
# entsprechende Ergebnis aus.

# and-Verküpfung: Beide Bedingungen müssen wahr sein
# if x > y and x < z:
#   print("x ist größer als y und kleiner als z")

# or-Verknüpfung: Eine der beiden Bedingungen muss wahr sein
# if x < y or x < z:


meine_floatzahl1 = 1.5
meine_floatzahl2 = 5.5

z = 15

if meine_floatzahl1 >= meine_floatzahl2:
  print("Die Zahl", meine_floatzahl1, "ist größer als", meine_floatzahl2)
else:
  print("Die Zahl", meine_floatzahl1, "ist kleiner als", meine_floatzahl2)


# Aufgabe 2:
# Legen Sie drei Variablen mit verschiedenen Zahlenwerten an.
# Schreiben Sie eine if-Bedingung mit einer and-Verknüpfung und eine mit einer or-Verknüpfung
# die bestimme Bedingung überprüft und entsprechende Nachrichten ausgibt.

meine_variable_1 = 5.6
meine_variable_2 = 10.9
meine_variable_3 = 50.2

if meine_variable_1 < meine_variable_2 and meine_variable_1 < meine_variable_3:
    print(meine_variable_1, "ist kleiner als", meine_variable_2, "und", meine_variable_3)
if meine_variable_1 < meine_variable_2 or meine_variable_1 > meine_variable_3:
    print(meine_variable_1, "ist entweder kleiner als", meine_variable_2, "oder größer als", meine_variable_3)