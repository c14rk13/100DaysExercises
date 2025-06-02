import requests as req

response = req.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()

data = response.json()
iss_position_lat = response.json()["iss_position"]["latitude"]
iss_position_long = response.json()["iss_position"]["longitude"]
iss_position = (iss_position_lat, iss_position_long)

print(response)                 # Output: <Response [200]>
print(response.status_code)     # Output: 200
print(data)          # {'message': 'success', 'iss_position': {'longitude': '143.0800', 'latitude': '45.7275'}, 'timestamp': 1748594369}
print(iss_position_lat, iss_position_long)
print(iss_position)

