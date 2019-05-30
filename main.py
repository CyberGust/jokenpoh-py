# Coding: utf-8
# Author: Gustavo Ilha Morais
# Python_version: 3.x

from random import randint
import time

history = []
rock = 1
paper = 2
scissors = 3

def bar(n, res):
    """
    This functions intends to help writing a shorter and cleaner code.
    n: width of the '-=-=' before and after the result;
    result: win, lose or draw
    """
    print("-="*n)
    print("Você" + " " + res)
    print("-="*n)



class ValidateAs():
    """
    Validate user as winner, looser or unlucky(draw matches) and
    save it on history to create game statistics.
    """
    def winner():
        history.append("won")
    def looser():
        history.append("lost")
    def unlucky():
        history.append("draw")


class Game():
    """
    Invoke 'menu' to show a menu and wait for user input.
    Call 'result' to validate which is the match's winner.
    Call 'rating' to get percentage of winning, loosing and drawing.
    """

    def menu():
        """
        Wait for the user input, validate it and invoke
        """
        print("-"*11)
        print("|1-Pedra  |\n|2-Papel  |\n|3-Tesoura|")
        print("-"*11)

        player = int(input("Qual a sua jogada?\n"))

        if player <= 3 & player >=1:
            Game.result(player)
        else:
            return False


    def result(human):
        """
        Creates computer's play and compares to the user input
        validating who's the winner.
        """
        computer = randint(1, 3)
        if (human == computer):
            ValidateAs.unlucky()
            bar(10, "empatou")
        elif (human == rock and computer == paper):
            ValidateAs.looser()
            print("Você: Pedra")
            print("Computador: Papel\n")
            bar(10, "perdeu")
        elif (human == rock and computer == scissors):
            ValidateAs.winner()
            print("Você: Pedra")
            print("Computador: Tesoura\n")
            bar(10, "ganhou")
        elif (human == paper and computer == scissors):
            ValidateAs.looser()
            print("Você: Papel")
            print("Computador: Tesoura\n")
            bar(10, "perdeu")
        elif (human == paper and computer == rock):
            ValidateAs.winner()
            print("Você: Papel")
            print("Computador: Pedra\n")
            bar(10, "ganhou")
        elif (human == scissors and computer == rock):
            ValidateAs.looser()
            print("Você: Tesoura")
            print("Computador: Pedra\n")
            bar(10, "perdeu")
        elif (human == scissors and computer == paper):
            ValidateAs.winner()
            print("Você: Tesoura")
            print("Computador: Papel\n")
            bar(10, "ganhou")


    def rating(history):
        w = 0
        l = 0
        d = 0
        for i in history:
            if i == "won":
                w += 1
            elif i == "lost":
                l += 1
            elif i == "draw":
                d += 1

        playedMatches = w + l + d
        if w > 0:
            winRating = round((w / playedMatches) * 100)
            print("Venceu " + " " + str(winRating) + "%")
        if l > 0:
            lostRating = round((l / playedMatches) * 100)
            print("Perdeu " + " " + str(lostRating) + "%")
        if d > 0:
            drawRating = round((d / playedMatches) * 100)
            print("Empatou " + " " + str(drawRating) + "%")


while True:
    a = Game.menu()
    if a == False:
        print("-=" * 6)
        Game.rating(history)
        print("-=" * 6)
        time.sleep(5)

        print("\n\n\n")

        print("-=" * 6)
        print("...Saindo...")
        print("-=" * 6)
        time.sleep(2)
        break
