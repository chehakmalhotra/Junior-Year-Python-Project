import webbrowser
import time
import re
A=(input("Odd or Even")).capitalize()
from random import *
x=randint(0,6)
if A=='Odd':
    print("Your decision is Odd")
    Odd=int(input("Enter a number between 0 and 6"))
    while not -1<Odd<7:
        print("Invalid Input")
        Odd=int(input("Enter a number between 0 and 6"))
    y=Odd+x
    z=y%2
    print("Your choice is ",Odd)
    print("Computer's choice is ", x)
    if z!=0:
        print("You win!")
        Win=input("Choose to Bat or Ball").capitalize()
        Lose=1
    if z==0:
        print("You lose...")
        print("Computer chooses to Bat")
        Lose="Bat"
        Win=1
if A=='Even':
    print("Your decision is Even")
    Even=int(input("Enter a number between 0 and 6"))
    while not -1<Even<7:
        print("Invalid Input")
        Even=int(input("Enter a number between 0 and 6"))
    y=Even+x
    z=y%2
    print("Your choice is ",Even)
    print("Computer's choice is ", x)
    if z==0:
        print("You win!")
        Win=input("Choose to Bat or Ball").capitalize()
        Lose=1
    if z!=0:
        print("You lose...")
        print("Computer chooses to Ball")
        Lose="Ball"
        Win=1
runs=0
if Win=="Bat":
    print("You are Batting")
    while Win=="Bat":
        score=int(input('0 to 6'))
        while not -1<score<7:
            print("Invalid Input")
            score=int(input("Enter a number between 0 and 6"))
        comp=randint(0,6)
        if score!=comp :
          runs+=score
          print("Computer:",comp)
        else:
          print('OUT')
          print("User's runs:",runs)
          break
    Turn="Ball"
    runsuser=runs
    runscomp="A"
elif Win=="Ball":
    print("You are Balling")
    while  Win=="Ball":
        score=int(input('0 to 6'))
        while not -1<score<7:
            print("Invalid Input")
            score=int(input("Enter a number between 0 and 6"))
        comp=randint(0,6)
        if score!=comp:
          runs+=comp
          print("Computer:",runs)
        else:
          print('Computer is out')
          print("Computer's runs:",runs)
          break
    Turn="Bat"
    runscomp=runs
    runsuser="A"
elif Lose=="Ball":
    print("You are Batting")
    while  Lose=="Ball":
        score=int(input('0 to 6'))
        while not -1<score<7:
            print("Invalid Input")
            score=int(input("Enter a number between 0 and 6"))
        comp=randint(0,6)
        if score!=comp:
          runs+=score
          print("Computer:",comp)
        else:
          print('OUT')
          print("User's runs",runs)
          break
    Turn="Ball"
    runsuser=runs
    runscomp="A"
elif Lose=="Bat":
    print("You are Balling")
    while Lose=="Bat":
        comp=randint(0,6)
        score=int(input('0 to 6'))
        while not -1<score<7:
            print("Invalid Input")
            score=int(input("Enter a number between 0 and 6"))
        if comp!=score:
            runs+=comp
            print("Computer:",comp)
        else:        
            print("Computer is out")
            print("Computer's runs:",runs)
            break
    Turn="Bat"
    runscomp=runs
    runsuser="A"
runs=0
if Lose=="Bat" or Lose=="Ball":
    print("Now you are",Turn,"ing")
    if Turn=="Bat":
        while Turn=="Bat":
            score=int(input('0 to 6'))
            while not -1<score<7:
                print("Invalid Input")
                score=int(input("Enter a number between 0 and 6"))
            comp=randint(0,6)
            if score!=comp:
                runs+=score
                print("Computer:",comp)
            else:
                print('OUT')
                print("User's runs",runs)
                break
    elif Turn=="Ball":
        while Turn=="Ball":
            comp=randint(0,6)
            score=int(input('0 to 6'))
            while not -1<score<7:
                print("Invalid Input")
                score=int(input("Enter a number between 0 and 6"))
            if comp!=score:
                runs+=comp
                print("Computer:",comp)
            else:        
                print("Computer is out")
                print("Computer's runs are",runs)
                break
elif Win=="Bat" or Win=="Ball":
    print("Now you are",Turn,"ing")
    if Turn=="Bat":
        while Turn=="Bat":
            score=int(input('0 to 6'))
            while not -1<score<7:
                print("Invalid Input")
                score=int(input("Enter a number between 0 and 6"))
            comp=randint(0,6)
            if score!=comp:
                runs+=score
                print("Computer:",comp)
            else:
                print('OUT')
                print("User's runs",runs)
                break
    elif Turn=="Ball":
        while Turn=="Ball":
            comp=randint(0,6)
            score=int(input('0 to 6'))
           
            
        
            if comp!=score:
                runs+=comp
                print("Computer:",comp)
            else:        
                print("Computer is out")
                print("Computer's runs are",runs)
                break
if runscomp=="A":
    if runs>runsuser:
        print("Computer wins by",runs-runsuser,"runs")
        time.sleep(3)
        webbrowser.open("https://giphy.com/gifs/tvland-tv-land-kingofqueens-kng-of-queens-KbZEMiWBFdynuQUobJ/fullscreen")
    elif runsuser>runs:
        print("You win by",runsuser-runs,"runs")
        time.sleep(3)
        webbrowser.open('https://giphy.com/gifs/football-night-fantasy-lnlAifQdenMxW/fullscreen')
    else:
        print("Draw")
if runsuser=="A":
    if runs>runscomp:
        print("You win by",runs-runscomp,"runs")
        time.sleep(3)
        webbrowser.open('https://giphy.com/gifs/football-night-fantasy-lnlAifQdenMxW/fullscreen')
    elif runscomp>runs:
        print("Computer wins by",runscomp-runs,"runs")
        time.sleep(3)
        
        webbrowser.open("https://giphy.com/gifs/tvland-tv-land-kingofqueens-kng-of-queens-KbZEMiWBFdynuQUobJ/fullscreen")
    else:
        print("Draw")
