#!/usr/bin/env python3   
from random import randrange

def start():
    while(True):
        try:
            usrInput = int(input("type a command (1.rock - 2.paper - 3.scissors):"))
            plays = ["-","rock", "paper", "scissors"]

            if usrInput < 1 or usrInput > 3:
                print("You have used an invalid command !")
                continue

            usrPlay = plays[usrInput]
            cpuInput = randrange(1, 4)
            cpuPlay = plays[cpuInput]

            print("You played", usrPlay, "!")
            print("The cpu has played", cpuPlay, "!")

            if usrPlay == cpuPlay:
                print("DRAW")
            else:
                if cpuPlay == plays[(usrInput % 3) + 1]:
                    print("You Lose !")
                else:
                    print("You win !")
                break

        except ValueError:
            print ("That is not a number !")
            continue

start()
