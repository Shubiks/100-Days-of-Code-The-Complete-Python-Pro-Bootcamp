import pandas as pd

df = pd.read_csv("Squirrel_Data.csv")
# print(df.info())

grey_color = len(df[df["Primary Fur Color"]=="Gray"])
red = len(df[df["Primary Fur Color"]=="Cinnamon"])
black = len(df[df["Primary Fur Color"]=="Black"])
print(grey_color)
print(red)
print(black)

d = {
    "fur color": ["Gray","Cinnamon","Black"],
    "count":[grey_color,red,black]
}

t = pd.DataFrame(d)
print(t)

t.to_csv("Squirrel_count.csv")
