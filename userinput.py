#

name = input("Enter your name: ")

distance_km = float(input("Enter distance in km: "))

distance_mi = float(distance_km) / 1.609

print(f"Hi, {name.capitalize()} {distance_km} km is equivalent to {distance_mi:.2f} miles.")

