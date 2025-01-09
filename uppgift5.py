'''
2 Skriv ett program som räknar ut längden på hypotenusan i en rätvinklig triangel. Användaren behöver skriva in längden på de två kortare sidorna.
Tips 1: fråga en AI om formeln Pythagoras sats. Men var noga med att inte fråga efter kod som löser uppgiften!
Tips 2: räkna ut roten med math.sqrt().

Som testdata kan du använda triangeln med sidorna 3, 4 och 5:

'''
import math

a = float(input("Ange längden på sidan a: "))
print(f"Första kateten har längden {a} cm ")

b = float(input("Ange längden på sidan b: "))
print(f"Andra kateten har längden {b} cm ")

c = math.sqrt(a ** 2 + b ** 2)
print(f"Hypotenusan längd är: {c}")