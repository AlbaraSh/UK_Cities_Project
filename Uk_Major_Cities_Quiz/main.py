from turtle import Turtle, Screen
import pandas
from numpy.core.defchararray import lower

tim = Turtle()
screen = Screen()
screen.title('UK Cities Game')
screen.setup(width=550, height=750)
screen.bgpic('uk_map.png')

data = pandas.read_csv('uk_cities.csv')
city_list = data['city'].to_list()
answered_cities = []


def display_answer(answer, x1, y1):
    name = Turtle()
    name.penup()
    name.color('Black')
    name.speed('fastest')
    name.hideturtle()
    name.goto(x=int(x1), y=int(y1))
    name.write(f'{answer}')


game_on = True
count = 0
while game_on:
    user_answer = screen.textinput(title=f'Guess the City {count}/19', prompt="what's the names of the dotted cities")
    if user_answer in city_list:
        if user_answer in answered_cities:
            pass
        else:
            answered_cities.append(user_answer)
            city_name = data[data.city == user_answer]
            display_answer(user_answer, city_name.x, city_name.y)
            count += 1
    if count == 19 or user_answer == 'exit':
        missing_cities = [city for city in city_list if city not in answered_cities]
        pandas.DataFrame(missing_cities).to_csv('missing_cities.csv')
        pandas.DataFrame(answered_cities).to_csv('answered_cities.csv')
        break
