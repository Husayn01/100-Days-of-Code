# with open("C:/Users/Hussaini/Desktop/100-Days-of-Code/Day 25/weather_data.csv") as data:
#     print(data.read())

# import csv
# with open("C:/Users/Hussaini/Desktop/100-Days-of-Code/Day 25/weather_data.csv") as data:
#     temperature = []
#     for temp in csv.reader(data):
#         if temp[1] != "temp":
#             temperature.append(int(temp[1]))
#     print(temperature)

# import pandas as pd

# data = pd.read_csv("C:/Users/Hussaini/Desktop/100-Days-of-Code/Day 25/weather_data.csv")
# # temp_list = data["temp"].to_list()
# # print(data["temp"].max())
# # print(data["temp"].min())
# # print(data["temp"].mean())
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# temp = monday.temp
# print(monday["temp"])

import pandas as pd

data = pd.read_csv("./Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pd.DataFrame(data_dict)
print(df)
df.to_csv("./Day 25/squirrels_count.csv")