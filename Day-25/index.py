import pandas

data = pandas.read_csv("Squirrel_Data.csv")

print(len(data[data["Primary Fur Color"] == "Gray"]))
print(len(data[data["Primary Fur Color"] == "Cinnamon"]))
print(len(data[data["Primary Fur Color"] == "Black"]))

squirrel_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(data[data["Primary Fur Color"] == "Gray"]), len(data[data["Primary Fur Color"] == "Cinnamon"]), len(data[data["Primary Fur Color"] == "Black"])]
}

data = pandas.DataFrame(squirrel_data)
print(data)
data.to_csv("squirrel_count.csv")