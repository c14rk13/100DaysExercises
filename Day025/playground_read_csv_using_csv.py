import csv

with open("files/weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        temperature = row[1]
        if temperature.isnumeric():
            temperatures.append(int(row[1]))

    print(temperatures)