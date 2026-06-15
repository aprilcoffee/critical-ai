# ===============================================================
# 2 — WEATHER  (an API has nothing to do with AI)
# ===============================================================
# Same idea as before, but this server just hands back today's
# weather. No AI, no key, no signup. It also shows the other kind
# of request: a GET, where the whole question lives IN the address
# (everything after the "?"). Open-Meteo is run on real national
# weather-service data.
#
# no key needed:  https://open-meteo.com
# docs:           https://open-meteo.com/en/docs
#
# pip install requests

import requests

# 1. the address
url = "https://api.open-meteo.com/v1/forecast"

# 2. the request: which place, and what we want to know
#    (these get stuck onto the URL after a "?")
params = {
    "latitude": 50.98,                       # Weimar
    "longitude": 11.33,
    "current": "temperature_2m,wind_speed_10m",
}

# 3. send it and wait  (GET, not POST — we are only asking, not sending)
response = requests.get(url, params=params)

# 4. read the answer
answer = response.json()
now = answer["current"]
print("temperature:", now["temperature_2m"], "°C")
print("wind:", now["wind_speed_10m"], "km/h")
