# with open("weather_data.csv") as file:
#     list_data = file.readlines()
#     for list_item in list_data:
#         print(list_item.strip())



# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)



import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])