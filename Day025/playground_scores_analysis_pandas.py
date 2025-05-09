import pandas

data = pandas.read_csv("files/weather_data.csv")
# print(data)
# print(type(data)) # Outputs: class: pandas.core.frame.DataFrame
# print(data["temp"])
# print(type(data["temp"])) # pandas.core.series.Series

# In Pandas: a Table is a DataFrame; A Column is a Series

# Convert to a raw python data type - dictionary
data_dict = data.to_dict()
# print(data_dict)


# Convert column/series to a list
temp_list = data["temp"].to_list()
# print(temp_list)
# avg_temperature = average(temp_list)
    # OR a better way using panda's mean()
avg_temperature = data["temp"].mean()
print(f"Average Temperature is: {avg_temperature: .2f}")
print(f"Maximum Temperature is: {data["temp"].max(): .2f}")


# Get data in columns
print(data["condition"])
#OR:
print(data.condition) #Can use dot notation for column names (case-sensitive)

# Get data in a row
print(data[data.day == "Monday"])
print(data[data.condition == "Rain"])

#Get row of data that has the maximum temperature
print(data[data.temp == data.temp.max()])

#.. further refine to just getting the day
print(data[data.temp == data.temp.max()].condition)

# Get monday's temp in Fahrenheit
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_in_F = monday_temp * 9/5 + 32
print(f"Monday's temperature in Fahrenheit: {monday_temp_in_F}")


# Create dataframe from scratch:
data_dict_scores = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_scores = pandas.DataFrame(data_dict_scores)
print(data_scores)

#Convert dataframe to csv :
data_scores.to_csv("./files/scores_data.csv")