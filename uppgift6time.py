# 3a Skriv ett program som talar om dagens datum.
# Resurs: Hantera datum i Python

import time
import datetime

# Dagens datum
current_date = datetime.date.today()
print(f"Dagens datum är: {current_date}")

# Ändra programmet så att det kan tala om vilket datum det är om 7 dagar.
future_date = current_date + datetime.timedelta(days=7)
print(f"Datumet om 7 dagar är: {future_date}")

#tiden
current_time = datetime.datetime.now().time()
formatted_time = current_time.strftime("%H:%M:%S")
print(f"Klockan är: {formatted_time}")

