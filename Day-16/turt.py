# from turtle import Turtle,Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DeepPink1")
# timmy.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()
# print((my_screen.canvheight))
#

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.add_row(["spiderman" , "fly"])
table.align = "r"
print(table)