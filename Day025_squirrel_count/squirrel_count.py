import pandas

# Read squirrel count data
# Extract count per fur color
# Create new dataFrame of fur color counts

squirrel_data = pandas.read_csv("files/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#print(squirrel_data.groupby("Primary Fur Color").agg("count"))
fur_color_data_count = squirrel_data.groupby("Primary Fur Color").size()
fur_color_data = pandas.DataFrame(fur_color_data_count)
print(fur_color_data)
fur_color_data.to_csv("./files/squirrel_fur_color_count.csv")



# Another way to do it:
grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

fur_color_data2 = pandas.DataFrame(data_dict)
fur_color_data2.to_csv("./files/squirrel_fur_color_count2.csv")