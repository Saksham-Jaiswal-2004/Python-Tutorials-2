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
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
print("Average Temperature:",sum(temp_list)/len(temp_list))

print(data["temp"].mean())

print(data["temp"].max())
print(data["temp"].min())

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# data["temp"] and data.temp both are same

# Creating a Dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("student.csv")