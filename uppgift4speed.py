
# 1a Det är ca 470 km mellan Stockholm och Göteborg. Skriv ett program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg. Du behöver fråga användaren hur fort man ska köra, i km/h.
# Tips: omvandla till m/s genom att dela med 3,6. Sedan kan du använda formeln: tid = sträcka / hastighet.

sträcka = 470

while True:

    hastighet = float(input("Hur fort vill du köra, i km/h (mellan 80 och 110): "))

    if hastighet < 80:
        print("Hastigheten är för låg! Ange en högre hastighet(mellan 80 och 110): ")
    elif hastighet > 110:
        print("Hastigheten är för hög! Ange en lägre hastighet(mellan 80 och 110)")
    else:
        print("Tack!Du valde en giltig hastighet ")
        break

#kalkyl med modulo
total_tid_i_sekunder = (sträcka / hastighet) * 3600
timmar = int(total_tid_i_sekunder / 3600)
minuter = int((total_tid_i_sekunder % 3600) // 60)
sekunder = int(total_tid_i_sekunder % 60)

print(f"Det tar {timmar} timmar, {minuter} minuter och {sekunder} sekunder att köra mellan Stockholm och Göteborg.")

# User input sträcka och hastighet
user_input_distans = int(input("Ange distansen du vill resa i (km): " ))
user_input_hastighet = int(input("Ange hastigheten i (km/h): "))

tid_i_timmar = user_input_distans / user_input_hastighet

timmar = int(tid_i_timmar)
minuter = int((tid_i_timmar - timmar) * 60)
sekunder = int(((tid_i_timmar - timmar) * 60 - minuter) * 60)

formatted_time = f"{timmar:02}h:{minuter:02}m:{sekunder:02}s"

print(f"Det tar {formatted_time} for att resa {user_input_distans} km med hastigheten på {user_input_hastighet} km/h. ")

