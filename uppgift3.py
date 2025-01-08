# Använda variabler och datatyper
# 1a Använd input för att be användaren om ett heltal. Spara värdet i en variabel. Omvandla variabelns värde till ett heltal, och skriv ut det för att testa om du har gjort rätt.
# Kodexempel med input:
user_input1 = int(input("Välj ett heltal mellan (1-10): "))

print(f"Du valde talet {user_input1}")

# 1b Fråga användaren efter ett annat heltal. Skriv ut summan av talen, alltså tal1 + tal2.
# Testa genom att hitta på två tal och räkna ut summan i huvudet. Kontrollera om programmet räknar rätt.
user_input2 = int(input("Välj ett heltal mellan (11-20): "))
print(f"Du valde talet {user_input2}")

summan = user_input1 + user_input2

print(f"Summan av dina heltal du hade valt är: {summan}")
print("***********")

# 2a Nu är det dags att köpa vinterkläder. Du ser en fin jacka som kostar 2000 kronor. Jackan är på rea, 50%. Skriv ett program som räknar ut hur mycket du behöver betala.
# Tips: räkna ut rabatten med formeln: slut_pris = pris * rea_procent / 100.

pris = 2000 # Jackans ursprungspris
rea_procent= 50 # Rea i procent

slut_pris = pris * rea_procent/100 # Beräkning av slutpris

print(f"Din jacka kostar {pris:.2f} kr, och med en rea på {rea_procent}% behöver du betala {slut_pris:.2f} kr")
print("***********")
# 2b Gör om programmet så att användaren kan skriva in en procentsats.
# Testa genom att hitta på en procentsats och räkna ut vad programmet ska svara med, innan du kör det. Till exempel 10%, som är 200 kr. Då ska jackan kosta 2000 - 200 == 1800 kr.

# 2a: Ursprungligt pris och procentsats
pris = 2000  # Jackans ursprungspris

# 2b: Be användaren ange rea-procent
rea_procent = float(input("Ange rea-procent (t.ex. 50 för 50%): "))

# Beräkning av slutpris
rabatt = pris * rea_procent / 100
slut_pris = pris - rabatt

# Utskrift av resultat
print(f"Din jacka kostar {pris:.2f} kr, och med en rea på {rea_procent}% sparar du {rabatt:.2f} kr.")
print(f"Det slutgiltiga priset du behöver betala är {slut_pris:.2f} kr.")