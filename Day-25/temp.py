import pandas

d = pandas.read_csv("weather_data.csv")

s = d["temp"]

max_temp = d[s == max(s)]
# print(max_temp)

monday = d[d.day == "Monday"]
celcius = monday.temp
farenheit = (celcius*(9/5))+32
print(farenheit)