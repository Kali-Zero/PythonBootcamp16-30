import pandas
#https://pandas.pydata.org/docs/

#Open invited_names
# with open("weather_data.csv", mode="r") as weather_file:
#     data_list = weather_file.read()

#Parse the invited names into a list.
# weather_list = data_list.splitlines()
# print(weather_list)

# import csv
# with open("weather_data.csv", mode="r") as weather_file:
#     weather_data = csv.reader(weather_file)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

#----------------------PANDA-----------------------------------------------
#weather_data = pandas.read_csv("weather_data.csv")
#print(panda_weather_data)
#print(panda_weather_data["temp"])
#print(type(panda_weather_data))
#data_dict = weather_data.to_dict()
#print(data_dict)
#temp_list = weather_data["temp"].to_list()
#print(len(temp_list))

#This...
#print(sum(temp_list) / len(temp_list))
#Is the same as this... (using PANDAS built in library)
#print(panda_weather_data["temp"].mean())

#print(panda_weather_data["temp"].max())

#Get Data in Row
#print(panda_weather_data[panda_weather_data.day == "Monday"])

#This is the same...
#print(weather_data[weather_data.temp == weather_data["temp"].max()])
#As this...
#print(weather_data[weather_data.temp == weather_data.temp.max()])

#monday = weather_data[weather_data.day == "Monday"]
#print(monday.condition)
#Get Monday's temperature converted into Fahrenheit
#print((monday.temp * 9/5) + 32)

#Create a dataframe from scratch
#Start with a dictionary...
# data_dict = {
#     "students": ["Amy", "Bob", "Cole"],
#     "scores": [96, 86, 79]
# }
# dict_data = pandas.DataFrame(data_dict)
#print(dict_data)
#Create a csv file from the data...
#dict_data.to_csv("dict_data.csv")
#----------------------------------------------------------------------------
#From the squirrel file, How many squirrels are there of each color?
#Create a csv file, with columns 'Fur Color', and 'Count'
#1 - Open the full data file
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#2 - From the 'Primary Fur Color' column, count the number of each color: (Gray, Cinnamon, Black)
grey_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
# print(grey_count)
# print(cinnamon_count)
# print(black_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, cinnamon_count, black_count]
}
count_dict_data = pandas.DataFrame(data_dict)
#print(count_dict_data)
#Will produce this:
#   Fur Color  Count
# 0      Gray   2473
# 1  Cinnamon    392
# 2     Black    103
#Create a csv file from the data...
dataframe = pandas.DataFrame(count_dict_data)
dataframe.to_csv("squirrel_count_data.csv")