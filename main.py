from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Cria 6 tartarugas, posiciona-as e adiciona-as à lista all_turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Inicia a corrida se o usuário fez uma aposta
if user_bet:
    is_race_on = True

# Loop principal da corrida
while is_race_on:
    for turtle in all_turtles:
        # Verifica se alguma tartaruga alcançou a linha de chegada
        # 230 é a coordenada X que representa a linha de chegada (250 - metade da largura da tartaruga)
        if turtle.xcor() > 230:
            is_race_on = False # A corrida termina
            winning_color = turtle.pencolor() # Obtém a cor da tartaruga vencedora
            if winning_color == user_bet:
                print(f"Você ganhou! A tartaruga {winning_color} é a vencedora!")
            else:
                print(f"Você perdeu! A tartaruga {winning_color} é a vencedora!")

        # Faz cada tartaruga se mover uma quantidade aleatória
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Mantém a janela aberta até ser clicada
screen.exitonclick()


