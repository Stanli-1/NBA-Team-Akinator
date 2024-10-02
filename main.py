#-------------------------Importing libraries-----------------------
from time import sleep
import time
from colorama import *
import sys 
import os
import turtle



#----------------------------Background Functions------------------
def countdown(t):
    while t > 0:
        t -= 1
        time.sleep(1)



#-----------------------------Defining------------------------------
eastern = [
  #0
  "Philadelphia 76ers", 
  #1
  "Brooklyn Nets", 
  #2
  "Milwaukee Bucks", 
  #3
  "Boston Celtics", 
  #4
  "New york Knicks", 
  #5
  "Miami Heat", 
  #6
  "Charlotte Hornets",
  #7
  "Toronto Raptors",
  #8
  "Chicago Bulls",
  #9
  "Indiana Pacers",
  #10
  "Atlanta Hawks",
  #11
  "Washington Wizards",
  #12
  "Cleveland Cavaliers",
  #13
  "Orlando Magics",
  #14
  "Detroit Pistons",

  ]

western = [
  #0
  'Utah Jazz', 
  #1
  'Phoenix Suns',
  #2
  'Los Angeles Lakers',
  #3
  'L.A. Clippers',
  #4
  'Portland Trail Blazers',
  #5
  'Denver Nuggets',
  #6
  'San Antonio Spurs',
  #7
  'Dallas Mavericks',
  #8
  'Golden State Warriors',
  #9
  'Memphis Grizzlies',
  #10
  'New Orleans Pelicans',
  #11
  'Oklahoma City Thunder',
  #12
  'Sacramento Kings',
  #13
  'Houston Rockets',
  #14
  'Minnesota Timberwolves',
  ]

space = '-------------------------------------------------------------------'



#----------------------------Turtle Images------------------------------

screen = turtle.Screen()
screen.setup(600, 320)



#----------------------------Main Function--------------------------

def main():
  while True:



#-----------------------------Intro-------------------------------------------------------
    print( Style.BRIGHT + Fore.WHITE + "Welcome to the " + Fore.CYAN + "N" + Fore.RED + "B" + Fore.WHITE + "A Selector! Made by Jashan and Stan \nThink of your favorite NBA team and answer the following questions.")
    img = r'nba.png'
    screen.bgpic(img)

    #Prints a list or just starts asking questions
    path = input("\nFor a list of the teams this program supports, type 'l'. \nTo begin the first question, type 'c'.")
    path = path.lower()

    #if the user enters a wrong keystroke
    while path != "l" and path != 'c':
      path = input("\nPlease enter either 'l' or 'c'.")
      path = path.lower()




#--------------------------if user wants to see list------------------------------------------
    if path == 'l':
      print('\n' + space + '\n\nThe list of teams this program supports are as follows:\n')

      print(Fore.CYAN + 'Eastern Conference Teams')
      for index, item in enumerate(eastern):
        print(index + 1, item)
      print('\n')

      print(Fore.RED + 'Weastern Conference Teams')
      for index, item in enumerate(western):
        print(index + 16, item)
      print('\n' + Fore.WHITE + space)
      path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")





#----------------------------if user picks team number for info-------------------------------------------
    if path.isnumeric():
      path_num = int(path)
      path_c = ''
    else:
      path_c = path.lower()
      path_num = 100

    while path_num < 1 and path_num > 30 or path_c != 'c':
      if path.isnumeric():
        if path_num >= 1 and path_num <= 30:

#Philadelphia
          if path_num == 1:
            print(space + '\n\n' + eastern[0] + ' - \nThis team has both ' + Fore.RED + 'Red ' + Fore.WHITE + 'and ' + Fore.CYAN + 'Blue ' + Fore.WHITE + 'in their logo.')
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100



#Brooklyn
          if path_num == 2:
            print(space + '\n\n' + eastern[1] + ' - \nThis team has both White and Black in their logo. \n' + Back.MAGENTA + 'Kevin Durant also plays on this team.' + Back.RESET)
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100



#Milwaukee 
          if path_num == 3:
            print(space + '\n\n' + eastern[2] + ' - \nThis team has both ' + Fore.GREEN + 'Green ' + Fore.WHITE + 'and White in their logo. \n' + Back.MAGENTA + 'This team is also tied for 5th place in most consecutive NBA games won.' + Back.RESET)
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100



#Boston 
          if path_num == 4:
            print(space + '\n\n' + eastern[3] + ' - \nThis team has both ' + Fore.GREEN + 'Green ' + Fore.WHITE + 'and White in their logo.')
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100



#New York Knicks 
          if path_num == 5:
            print(space + '\n\n' + eastern[4] + ' - \nThis team has both ' + Fore.CYAN + 'Blue ' + Fore.WHITE + 'and ' + Fore.YELLOW + 'Orange ' + Fore.WHITE + 'in their logo. \n' + Back.MAGENTA + 'This team has also won 2 NBA championships and is a founding NBA team.' + Back.RESET)
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100



#Miami heat 
          if path_num == 6:
            print(space + '\n\n' + eastern[5] + ' - \nThis team has both ' + Fore.RED + 'Red ' + Fore.WHITE + 'and ' + Fore.CYAN + 'Blue ' + Fore.WHITE + 'in their logo. \n' + Back.MAGENTA + 'Labron James has won a NBA MVP Award on this team.' + Back.RESET)
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100



#Charlotte
          if path_num == 7:
            print(space + '\n\n' + eastern[6] + ' - \nThis team has both ' + Fore.BLUE + 'Blue ' + Fore.WHITE + 'and White in their logo. \n' + Back.MAGENTA + 'This team is owned by Micheal Jordan.' + Back.RESET)
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100
 


#Raptors 
          if path_num == 8:
            print(space + '\n\n' + eastern[7] + ' - \nThis team has a ' + Fore.RED + 'Red ' + Fore.WHITE + Back.MAGENTA + 'basketball' + Back.RESET + ' in their logo. \n' + Back.MAGENTA + 'This team has also won the NBA championship in 2019.' + Back.RESET)
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100



#Bulls
          if path_num == 9:
            print(space + '\n\n' + eastern[8] + ' - \nThis team has a ' + Fore.RED + 'Red ' + Fore.WHITE + Back.MAGENTA + 'bull' + Back.RESET + ' in their logo. \n' + Back.MAGENTA + 'Micheal Jordan has also played on this team in the past.' + Back.RESET)
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100          



#Pacers 
          if path_num == 10:
            print(space + '\n\n' + eastern[9] + ' - \nThis team has both ' + Fore.BLUE + 'Blue ' + Fore.WHITE + 'and ' + Fore.YELLOW + 'Yellow ' + Fore.WHITE + 'in their logo. \n' + Back.MAGENTA + 'This team has also won 3 ABA championships.' + Back.RESET)
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100


#Hawks
          if path_num == 11:
            print(space + '\n\n' + eastern[10] + ' - \nThis team has a ' + Fore.RED + 'Red ' + Fore.WHITE + Back.MAGENTA + 'hawk' + Back.RESET + ' in their logo.')
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100



# Wizards
          if path_num == 12:
            print(space + '\n\n' + eastern[11] + " - \nThis team has both " + Fore.RED + 'Red ' + Fore.WHITE + 'and ' + Fore.CYAN + 'Blue ' + Fore.WHITE + 'in their logo. \n' + Back.MAGENTA + "This team has a basketball in their logo and is 'Magical'." + Back.RESET)
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100



#Cavaliers
          if path_num == 13:
            print(space + '\n\n' + eastern[12] + ' - \nThis team has both ' + Fore.RED + 'Red ' + Fore.WHITE + 'and ' + Fore.YELLOW + 'Gold ' + Fore.WHITE + 'in their logo.')
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100



#Orlando
          if path_num == 14:
            print(space + '\n\n' + eastern[13] + ' - \nThis team has ' + Fore.BLUE + 'Blue, ' + Fore.WHITE + 'white and black in their logo.')
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100



#Pistons 
          if path_num == 15:
            print(space + '\n\n' + eastern[14] + ' - \nThis team has both ' + Fore.RED + 'Red ' + Fore.WHITE + 'and ' + Fore.CYAN + 'Blue ' + Fore.WHITE + 'in their logo.')
            print('\n' + space)
            path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
            if path.isnumeric():
              path_num = int(path)
              path_c = 'a'
            else:
              path_c = path.lower()
              path_num = 100


#-------Western------

#Jazz

          if path_num == 16:
              print(space + '\n\n' + western[0] + ' - \nThis team has both ' + Fore.YELLOW + 'Orange ' + Fore.WHITE + 'and ' + Fore.CYAN + 'Blue ' + Fore.WHITE + 'in their logo.')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100


#Suns
          if path_num == 17:
              print(space + '\n\n' + western[1] + ' - \nThis team has both ' + Fore.YELLOW + 'Orange ' + Fore.WHITE + 'and a basketball in their logo.')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100

#Lakers                
          if path_num == 18:
              print(space + '\n\n' + western[2] + ' - \nThis team has both ' + Fore.YELLOW + 'Orange ' + Fore.WHITE + 'and' + Fore.MAGENTA + ' Purple in their logo. They have also won the N' + Fore.RED + 'B' + Fore.CYAN + 'A' + Fore.WHITE + ' Championship during a global pandemic')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100

#Clippers
          if path_num == 19:
              print(space + '\n\n' + western[3] + ' - \nThis team has both ' + Fore.WHITE + 'White ' + Fore.WHITE + 'and ' + Fore.CYAN + 'Blue ' + Fore.WHITE + 'in their logo')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100

#Nuggets
          if path_num == 20:
              print(space + '\n\n' + western[4] + ' - \nThis team has both ' + Fore.WHITE + 'Black ' + Fore.WHITE + 'and ' + Fore.YELLOW + 'Gold ' + Fore.WHITE + 'in their logo')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100

#TrailBlazers
          if path_num == 21:
              print(space + '\n\n' + western[5] + ' - \nThis team has both ' + Fore.WHITE + 'White ' + Fore.WHITE + 'and ' + Fore.RED + 'Red ' + Fore.WHITE + 'in their logo')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100

#Spurs
          if path_num == 22:
              print(space + '\n\n' + western[6] + ' - \nThis team has both ' + Fore.WHITE + 'White ' + Fore.WHITE + 'and ' + Fore.WHITE + 'Black ' + Fore.WHITE + 'in their logo')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100

#Mavericks
          if path_num == 23:
              print(space + '\n\n' + western[7] + ' - \nThis team has both ' + Fore.WHITE + 'White ' + Fore.WHITE + 'and ' + Fore.CYAN + 'Blue ' + Fore.WHITE + 'in their logo')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100

#Warriors
          if path_num == 24:
              print(space + '\n\n' + western[8] + ' - \nThis team has both ' + Fore.YELLOW + 'Gold ' + Fore.WHITE + 'and ' + Fore.CYAN + 'Blue ' + Fore.WHITE + 'in their logo')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100

#Grizzlies
          if path_num == 25:
              print(space + '\n\n' + western[9] + ' - \nThis team has both ' + Fore.WHITE + 'White ' + Fore.WHITE + 'and ' + Fore.CYAN + 'Blue ' + Fore.WHITE + 'in their logo')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100

#Pelicans
          if path_num == 26:
              print(space + '\n\n' + western[10] + ' - \nThis team has both ' + Fore.WHITE + 'White ' + Fore.WHITE + 'and ' + Fore.CYAN + 'Blue ' + Fore.WHITE + 'along with a bird, in their logo')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100

#Thunder
          if path_num == 27:
              print(space + '\n\n' + western[11] + ' - \nThis team has both ' + Fore.YELLOW + 'Orange ' + Fore.WHITE + 'and ' + Fore.CYAN + 'Blue ' + Fore.WHITE + 'along with white, in their logo')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100

#Kings
          if path_num == 28:
              print(space + '\n\n' + western[12] + ' - \nThis team has both ' + Fore.WHITE + 'White ' + Fore.WHITE + 'and ' + Fore.MAGENTA + 'Purple ' + Fore.WHITE + 'in their logo')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100

#Rockets
          if path_num == 29:
              print(space + '\n\n' + western[13] + ' - \nThis team has both ' + Fore.RED + 'Red ' + Fore.WHITE + 'and a ' + Fore.RED + 'R ' + Fore.WHITE + 'in their logo')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100

#Timberwolves
          if path_num == 30:
              print(space + '\n\n' + western[14] + ' - \nThis team has both ' + Fore.WHITE + 'Black ' + Fore.WHITE + 'and ' + Fore.CYAN + 'Blue ' + Fore.WHITE + 'along with a wolf, in their logo')
              print('\n' + space)
              path = input("\nIf you would like more information on a specific team, \nenter their coresponding digit (without period).\n\nOtherwise, type c to start the first question!\n")
              if path.isnumeric():
                path_num = int(path)
                path_c = 'a'
              else:
                path_c = path.lower()
                path_num = 100



#if not
        else:
          path = input("\nPlease enter either a teams number for more info (only digit), or 'c'.")
          if path.isnumeric():
            path_num = int(path)
            path_c = 'a'
          else:
            path_c = path.lower()
            path_num = 100





#---------------------------if user wants to start questions---------------------------------
      elif path.isnumeric() == False:
        path = path.lower()
        if path != 'c':
          path = input("\nPlease enter either a teams number for more info (only digit), or 'c'.")
          if path.isnumeric():
            path_num = int(path)
            path_c = 'a'
          else:
            path_c = path.lower()
            path_num = 100






#-----------------------------If user wants to jump right in---------------------------------------
      elif path == 'c':
        print('\n' + space + "\n\nLet's begin! \nThe screen will soon clear...")







#----------------------------clears screen after 3 seconds---------------------------------------
    print('\n' + space + "\n\nLet's begin! \nThe screen will soon clear...")
    countdown(3)
    os.system('clear')



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#------------------------Eastern or weastern-------------------------------------------------------------------------
    print ("Question 1 (Please Enter 'y' or 'n')\n")
    Q1 = input("Is the NBA team you chose part of the Eastern Conference?")
    Q1 = Q1.lower()

    while Q1 != 'y' and Q1 != 'n':
      Q1 = input("\nPlease enter either 'y' or 'n'.")
    print('Hmmm...')
    countdown(1)
    os.system('clear')





#--------------------------eastern - Red in logo?
    if Q1 == "y":
      print ("Question 2 (Please Enter 'y' or 'n')\n")
      Q2 = input("Does your team's logo have red in it?")
      Q2 = Q2.lower()

      while Q2 != 'y' and Q2 != 'n':
        Q2 = input("\nPlease enter either 'y' or 'n'.")
      print('Interesting...')
      countdown(1)
      os.system('clear')





#--------------------------Eastern - red logo - Blue in logo?
      if Q2 =="y":
        print ("Question 3 (Please Enter 'y' or 'n')\n")
        Q3 = input("Does your team's logo have blue in it?")
        Q3 = Q3.lower()

        while Q3 != 'y' and Q3 != 'n':
          Q3 = input("\nPlease enter either 'y' or 'n'.")
        print('Calculating...')
        countdown(1)
        os.system('clear')






#--------------------------Eastern - red logo - blue logo - Basketball in logo?
        if Q3 =="y":
          print ("Question 4 (Please Enter 'y' or 'n')\n")
          Q4 = input("Does your team's logo have a basketball in it?")
          Q4 = Q4.lower()

          while Q4 != 'y' and Q4 != 'n':
            Q4 = input("\nPlease enter either 'y' or 'n'.")
          print('Scanning Data Base...')
          countdown(1)
          os.system('clear')    







#----------------------------Eastern - red logo - blue logo - basketball in logo - Magic?
          if Q4 =="y":
            print ("Question 5 (Please Enter 'y' or 'n')\n")
            Q5 = input("Is your team associated with Magic?")
            Q5 = Q5.lower()

            while Q5 != 'y' and Q5 != 'n':
              Q5 = input("\nPlease enter either 'y' or 'n'.")
            print('Drum Role Please...')
            countdown(1)
            os.system('clear') 

#----------------------------Eastern - red logo - blue logo - basketball in logo - magic yes 
            if Q5 == 'y':
              #washington
              print(Fore.RED + 'Zap! ' + Fore.CYAN + 'You chose the ' + eastern[11] + '!\n' + Fore.WHITE)
              img = r'wizards.png'
              screen.bgpic(img)

#----------------------------Eastern - red logo - blue logo - basketball in logo - magic no
            else:
              #detroit
              print("You chose the " + Fore.RED + "Bad " + Fore.CYAN + "Boys " + Fore.WHITE + "(" + eastern[14] + ')!\n')
              img = r'pistons.png'
              screen.bgpic(img)






#----------------------------Eastern - red logo - blue logo - no basketball in logo
          else:
            #Philadelphia
            print('You chose the Philadelphia ' + Fore.RED + '7' + Fore.CYAN + '6' + Fore.WHITE + 'ers!\n\n' + "Did you know they used 76 because the Decloration of Independance in Philadelphia was signed in 1776?\n")

            img = r'phi.png'
            screen.bgpic(img)






#----------------------------Eastern - red logo - no blue logo - Animal in logo?
        elif Q3 == "n":
          print ("Question 4 (Please Enter 'y' or 'n')\n")
          Q4 = input("Is there an animal in your logo?")
          Q4 = Q4.lower()

          while Q4 != 'y' and Q4 != 'n':
            Q4 = input("\nPlease enter either 'y' or 'n'.")
          print('Scanning Data Base...')
          countdown(1)
          os.system('clear') 



#----------------------------Eastern - red logo - no blue logo - yes animal - MJ?
          if Q4 == "y":
            print ("Question 5 (Please Enter 'y' or 'n')\n")
            Q5 = input("Did the great Micheal Jordan play for your team?")
            Q5 = Q5.lower()

            while Q5 != 'y' and Q5 != 'n':
              Q5 = input("\nPlease enter either 'y' or 'n'.")
            print('Calculating...')
            countdown(1)
            os.system('clear') 


            if Q5 == "y":
              # bulls
              print('Home of the ' + Fore.YELLOW + 'GOAT ' + Fore.WHITE + 'himself, you picked the ' + Fore.RED + eastern[8] + Fore.WHITE + '!\n')
              img = r'bulls.png'
              screen.bgpic(img)

            else:
              # hawks
              print(Fore.RED + 'Ka' + Fore.WHITE + '-kaw! You chose the ' + Fore.RED + eastern[10] + Fore.WHITE + '!\n')
              img = r'hawks.png'
              screen.bgpic(img)





#----------------------------Eastern - red logo - no blue logo - no animal - 2019 champ?
          if Q4 == "n":
            print ("Question 5 (Please Enter 'y' or 'n')\n")
            Q5 = input("Did your team win the 2019 NBA Championship?")
            Q5 = Q5.lower()

            while Q5 != 'y' and Q5 != 'n':
              Q5 = input("\nPlease enter either 'y' or 'n'.")
            print('Calculating...')
            countdown(1)
            os.system('clear') 



#----------------------------Eastern - red logo - no blue logo - no animal - yes 2019
            if Q5 == "y":
              # raptors
              print('WOW did this team step up to the game and take home the ' + Fore.YELLOW + 'crown ' + Fore.WHITE + 'from the two-time defending championship!\nYou picked the ' + Fore.RED + eastern[7] + Fore.WHITE + '!\n')
              img = r'raptors.png'
              screen.bgpic(img)



#----------------------------Eastern - red logo - no blue logo - no animal - no 2019 - james mvp?
            if Q5 == 'n':
              print ("Question 6 (Please Enter 'y' or 'n')\n")
              Q6 = input("Has Labron James won the NBA MVP Award while playing for your team?")
              Q6 = Q6.lower()

              while Q6 != 'y' and Q6 != 'n':
                Q6 = input("\nPlease enter either 'y' or 'n'.")
              print('Calculating...')
              countdown(1)
              os.system('clear') 


              if Q6 == "y":
                # Miami
                print(Fore.RED + 'Sizzzle ' + Fore.WHITE + 'You chose the ' + Fore.YELLOW + 'Miami ' + Fore.RED + 'Heat' + Fore.WHITE + '!\n')
                img = r'miami.png'
                screen.bgpic(img)

              else:
                # calvaliers
                print('You chose the ' + Fore.YELLOW + 'Cleveland ' + Fore.RED + 'Cavaliers' + Fore.WHITE + '!\nDid you know the Cavaliers were the first team in NBA history \nto come back from a ' + Fore.YELLOW + '3' + Fore.WHITE + '-' + Fore.RED + '1' + Fore.WHITE + ' deficit in the finals?\n')
                img = r'cava.png'
                screen.bgpic(img)





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#--------------------------Eastern - no red logo - b in name?
      if Q2 == "n":
        print ("Question 3 (Please Enter 'y' or 'n')\n")
        Q3 = input("Does your team have the letter 'B' in their name?")
        Q3 = Q3.lower()

        while Q3 != 'y' and Q3 != 'n':
          Q3 = input("\nPlease enter either 'y' or 'n'.")
        print('Calculating...')
        countdown(1)
        os.system('clear')






#--------------------------Eastern - no red logo - b - 5th?
        if Q3 =="y":
          print ("Question 4 (Please Enter 'y' or 'n')\n")
          Q4 = input("Is your team tied for 5th place in the most consecutive NBA games won?")
          Q4 = Q4.lower()

          while Q4 != 'y' and Q4 != 'n':
            Q4 = input("\nPlease enter either 'y' or 'n'.")
          print('Scanning Data Base...')
          countdown(1)
          os.system('clear')    

          if Q4 == 'y':
            #bucks
            print(Fore.GREEN + 'Fast ' + Fore.WHITE + 'and ' + Fore.GREEN + 'agile ' + Fore.WHITE + 'just like a buck, the team you picked was ' + eastern[2] + '!\n')
            img = r'bucks.png'
            screen.bgpic(img)







#--------------------------Eastern - no red logo - b - not 5th - KD?
          elif Q4 =="n":
            print ("Question 5 (Please Enter 'y' or 'n')\n")
            Q5 = input("Does Kevin Durant currently play on your team?")
            Q5 = Q5.lower()

            while Q5 != 'y' and Q5 != 'n':
              Q5 = input("\nPlease enter either 'y' or 'n'.")
            print('Drum Role Please...')
            countdown(1)
            os.system('clear') 

#--------------------------Eastern - no red logo - b - not 5th - KD yes           
            if Q5 == 'y':
              #Brooklyn
              print('You chose the ' + eastern[1] + '!\nDid you know ' + Fore.MAGENTA + 'Jay Z ' + Fore.WHITE + 'previously owned a portion of this NBA team?\n')
              img = r'brook.png'
              screen.bgpic(img)

#----------------------------Eastern - no red - b - not 5th - no kd
            else:
              #Boston
              print("You chose the " + Fore.GREEN + eastern[3] + Fore.WHITE + '!\n\nDid you know the ' + Fore.GREEN + 'Celtics' + Fore.WHITE + ' hold the record for longest NBA win streak of all time? \nThey won ' + Fore.GREEN + '8 championships ' + Fore.WHITE + 'in a row!\n')
              img = r'boston.png'
              screen.bgpic(img)






#----------------------------Eastern - no red logo - no b - won nba/aba?
        elif Q3 == "n":
          print ("Question 4 (Please Enter 'y' or 'n')\n")
          Q4 = input("Has your team won an NBA/ABA championship?")
          Q4 = Q4.lower()

          while Q4 != 'y' and Q4 != 'n':
            Q4 = input("\nPlease enter either 'y' or 'n'.")
          print('Scanning Data Base...')
          countdown(1)
          os.system('clear') 




#----------------------------Eastern - no red logo - no b - won nba/aba - founding team?          
          if Q4 == "y":
            print ("Question 5 (Please Enter 'y' or 'n')\n")
            Q5 = input("Is your team one of the founding NBA teams?")
            Q5 = Q5.lower()

            while Q5 != 'y' and Q5 != 'n':
              Q5 = input("\nPlease enter either 'y' or 'n'.")
            print('Calculating...')
            countdown(1)
            os.system('clear') 


            if Q5 == "y":
              # Knicks
              print('You picked the ' + Fore.YELLOW + 'New York ' + Fore.CYAN + 'Nicks' + Fore.WHITE + "!\nDid you know the knicks is short for " + Fore.YELLOW + "Knicker" + Fore.CYAN + "bocker " + Fore.WHITE + "\nwhich is named after the symbol of New York's Father?\n")
              img = r'knicks.png'
              screen.bgpic(img)

            else:
              # Pacers
              print('You chose the ' + Fore.YELLOW + 'Indiana ' + Fore.CYAN + 'Pacers' + Fore.WHITE + '!\nDid you know the Pacers have 2 mascots? \nOne is a cat named ' + Fore.YELLOW + 'Boomer' + Fore.WHITE + ', and the other is ' + Fore.CYAN + 'Bowser ' + Fore.WHITE + 'which is a dog.\n')
              img = r'pacers.png'
              screen.bgpic(img)






#----------------------------Eastern - no red logo - no b - no win nba/aba - owned by MJ?
          if Q4 == "n":
            print ("Question 5 (Please Enter 'y' or 'n')\n")
            Q5 = input("Is your team owned by Micheal Jordan?")
            Q5 = Q5.lower()

            while Q5 != 'y' and Q5 != 'n':
              Q5 = input("\nPlease enter either 'y' or 'n'.")
            print('Calculating...')
            countdown(1)
            os.system('clear') 

            if Q5 == "y":
              # Hornets
              print(Fore.CYAN + 'Buzz, ' + Fore.BLUE + 'Buzz, ' + Fore.WHITE + 'you picked the ' + Fore.CYAN + 'Charlotte ' + Fore.BLUE + 'Hornets' + Fore.WHITE + "!\n")
              img = r'hornets.png'
              screen.bgpic(img)

            else:
              # Orlando Magic
              print('You chose the ' + Fore.CYAN + 'Orlando ' + Fore.BLUE + 'Magics' + Fore.WHITE + "!\nDid you know the Magic in their name comes from " + Fore.CYAN + "Walt Dinsey's " + Fore.BLUE + "Magic Kingdom?.\n" + Fore.WHITE)
              img = r'magics.png'
              screen.bgpic(img)






#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






#------------------------------Weastern teams - blue?
    elif Q1 == "n":
      print ("Question 2 (Please Enter 'y' or 'n')\n")
      Q2A = input("Is the NBA team you chose have any bit of blue in their logo?")
      Q2A = Q2A.lower()

      while Q2A != 'y' and Q2A != 'n':
        Q2A = input("\nPlease enter either 'y' or 'n'.")
      print('Hmmm...')
      countdown(1)
      os.system('clear')





#----------------------------weastern - blue - animal?
      if Q2A =="y":
        print("Question 3 (Please Enter 'y' or 'n')\n")
        Q3A1 = input("Does your NBA team's name have an animal in it?")
        Q3A1 = Q3A1.lower()

        while Q3A1 != 'y' and Q3A1 != 'n':
          Q3A1 = input("\nPlease enter either 'y' or 'n'.")
        print('Interesting...')
        countdown(1)
        os.system('clear')




#-----------------------------weastern - blue - animal - land?
        if Q3A1 =="y":
          print("Question 4 (Please Enter 'y' or 'n')\n")
          Q4A1 = input("Is your team's animal a land animal?")
          Q4A1 = Q4A1.lower()

          while Q4A1 != 'y' and Q4A1 != 'n':
            Q4A1 = input("\nPlease enter either 'y' or 'n'.")
          print('Calculating...')
          countdown(1)
          os.system('clear')




#----------------------------weastern - blue - animal - land - Texas?
          if Q4A1 =="y":
            print("Question 5 (Please Enter 'y' or 'n')\n")
            Q5A1 = input("Is your team from Texas?")
            Q5A1 = Q5A1.lower()

            while Q5A1 != 'y' and Q5A1 != 'n':
              Q5A1 = input("\nPlease enter either 'y' or 'n'.")
            print('Scanning Data Base...')
            countdown(1)
            os.system('clear')

#Mavericks
            if Q5A1 == 'y':
              print("Your team is the wild chargers of the league...the " + Fore.CYAN + western[7] + Fore.WHITE + '!\n')
              img = r'mavericks.png'
              screen.bgpic(img)   




#----------------------------weastern - blue - animal - land - no texas - hibernate?
            if Q5A1 =="n":
              print("Question 6 (Please Enter 'y' or 'n')\n")
              Q6A1 = input("Does your team's animal hibernate during the winter months?")
              Q6A1 = Q6A1.lower()

              while Q6A1 != 'y' and Q6A1 != 'n':
                Q6A1 = input("\nPlease enter either 'y' or 'n'.")
              print('Drum Roll Please...')
              countdown(1)
              os.system('clear')

#yes hibernate - Grizzlies
              if Q6A1 == 'y':
                print("Your team are the hibernating bears of the western conference... the " + Fore.CYAN + western[9] + Fore.WHITE + '!\n')
                img = r'grizzlies.png'
                screen.bgpic(img)        

#no hibernate - Timberwolves
              if Q6A1 == 'n':
                print("Your team is the wolf pack of the western conference... the " + Fore.CYAN + western[14] + Fore.WHITE + '!\n')
                img = r'timberwolves.png'
                screen.bgpic(img)  





#----------------------------weastern - blue - animal - notland
#Pelicans
          elif Q4A1 == 'n':
            print("Your team is the big beaks of the western conference... \nthe " + Fore.CYAN + western[10] + Fore.WHITE + '!\n')
            img = r'pelicans.png'
            screen.bgpic(img)





#----------------------------weastern - blue - no animal - cali?
        elif Q3A1 == 'n':
          print("Question 4 (Please Enter 'y' or 'n')\n")
          Q4B1 = input("Is your team from beautiful sunny California?")
          Q4B1 = Q4B1.lower()

          while Q4B1 != 'y' and Q4B1 != 'n':
            Q4B1 = input("\nPlease enter either 'y' or 'n'.")
          print('Scanning Data Base...')
          countdown(1)
          os.system('clear')




#----------------------------weastern - blue - no animal - yes cali - gold? 
          if Q4B1 == 'y':
            print("Question 5 (Please Enter 'y' or 'n')\n")
            Q7A1 = input("Is your team 24K Gold (sometimes)?")
            Q7A1 = Q7A1.lower()

            while Q7A1 != 'y' and Q7A1 != 'n':
              Q7A1 = input("\nPlease enter either 'y' or 'n'.")
            print('Drum Role PLease...')
            countdown(1)
            os.system('clear')





#----------------------------weastern - blue - no animal - yes cali - yes gold 
#warriors
            if Q7A1 == 'y':
              print("Your team is the gold encrusted team of the western conference... \nthe " + Fore.YELLOW +   western[8] + Fore.WHITE + '!\n')
              img = r'warriors.png'
              screen.bgpic(img)  


#clippers  
            elif Q7A1 =="n":
              print("Your team is the team that stole Kawhi Leonard from us Raptors fans and I will not forgive you... the " + Fore.BLUE + western[3] + Fore.WHITE + '!\n' )
              img = r'clippers.png'
              screen.bgpic(img)





              
#----------------------------weastern - blue - no animal - no cali - music? 
          if Q4B1 == 'n':
            print("Question 5 (Please Enter 'y' or 'n')\n")
            Q7B1 = input("Does your team make music?")
            Q7B1 = Q7B1.lower()

            while Q7B1 != 'y' and Q7B1 != 'n':
              Q7B1 = input("\nPlease enter either 'y' or 'n'.")
            print('Drum Role PLease...')
            countdown(1)
            os.system('clear')





#----------------------------weastern - blue - no animal - no cali - yes music 
#jazz
            if Q7B1 == 'y':
              print("Your team are the slow jazz team of the western conference... \nthe " + Fore.RED +   western[0] + Fore.WHITE + '!\n')  
              img = r'jazz.png'
              screen.bgpic(img)
              

              
#----------------------------weastern - blue - no animal - no cali - no music - thunder?
            if Q7B1 == 'n':
              print("Question 6 (Please Enter 'y' or 'n')\n")
              Q8B1 = input("Does your team bring the rumble of the thunder?")
              Q8B1 = Q8B1.lower()

              while Q8B1 != 'y' and Q8B1 != 'n':
                Q8B1 = input("\nPlease enter either 'y' or 'n'.")
              print('A-Ha!')
              countdown(1)
              os.system('clear')

                
#-------------yes thunder
  #thunder
              if Q8B1 == 'y':
                print("Your team are the thunderstorm of the western conference... \nthe " + Fore.YELLOW +   western[11] + Fore.WHITE + '!\n')
                img = r'thunder.png'
                screen.bgpic(img)  


 #-------------no thunder
 #nuggets
              elif Q8B1 =="n":
                print('Your team is the... ' + Fore.RED + western[5] + Fore.WHITE + '!\n' )
                img = r'nuggets.png'
                screen.bgpic(img)





#---------------------------weastern - no blue - in tex or cali?
      elif Q2A == "n":
        print("Question 3 (Please Enter 'y' or 'n')\n")
        Q3B2 = input("Is your NBA team from a city in Texas or California? ")
        Q3B2 = Q3B2.lower()

        while Q3B2 != 'y' and Q3B2 != 'n':
          Q3B2 = input("\nPlease enter either 'y' or 'n'.")
        print('Interesting...')
        countdown(1)
        os.system('clear')




#---------------------------weastern - no blue - in tex or cali - Cali?
        if Q3B2 == "y":
          print("Question 4 (Please Enter 'y' or 'n')\n")
          Q4A2 = input("Is your team from sunny and bright California?")
          Q4A2 = Q4A2.lower()

          while Q4A2 != 'y' and Q4A2 != 'n':
            Q4A2 = input("\nPlease enter either 'y' or 'n'.")
          print('Calculating...')
          countdown(1)
          os.system('clear')



#---------------------------weastern - no blue - in tex or cali - yes Cali - pandemic win?
          if Q4A2 == "y":
            print("Question 5 (Please Enter 'y' or 'n')\n")
            Q5A2 = input("Did your team win the NBA championship during a global pandemic?")
            Q5A2 = Q5A2.lower()

            while Q5A2 != 'y' and Q5A2 != 'n':
              Q5A2 = input("\nPlease enter either 'y' or 'n'.")
            print('Scanning Data Base...')
            countdown(1)
            os.system('clear')


#-------------yes pandemic win
#lakers
            if Q5A2 == 'y':
              print('Your team is the great ' + Fore.YELLOW +   western[2] + Fore.WHITE + '!\n')
              img = r'lakers.png'
              screen.bgpic(img)  


 #-------------no pandemic win
 #kings
            elif Q5A2 =="n":
              print('Your team are the often forgotten team of California... \nthe ' + western[12] + '!\n' )
              img = r'kings.png'
              screen.bgpic(img)



#---------------------------weastern - no blue - in tex or cali - not Cali - space?
          if Q4A2 == "n":
            print("Question 5 (Please Enter 'y' or 'n')\n")
            Q5B2 = input("Does your team like space travel?")
            Q5B2 = Q5B2.lower()

            while Q5B2 != 'y' and Q5B2 != 'n':
              Q5B2 = input("\nPlease enter either 'y' or 'n'.")
            print('Interesting...')
            countdown(1)
            os.system('clear')


#-------------yes space
#rockets
            if Q5B2 == 'y':
              print("Your team are the rocketeers of the league... \nthe " + Fore.RED +   western[13] + Fore.WHITE + '!\n')
              img = r'rockets.png'
              screen.bgpic(img)  


 #-------------no space
 #spurs
            elif Q5B2 =="n":
              print("That means your team is the... " + Fore.CYAN + western[6] + '!\n' )
              img = r'spurs.png'
              screen.bgpic(img)





#---------------------------weastern - no blue - not in tex or cali - Arizona?
        if Q3B2 == "n":
          print("Question 4 (Please Enter 'y' or 'n')\n")
          Q4B2 = input("Is your team from hot and dry Arizona?")
          Q4B2 = Q4B2.lower()

          while Q4B2 != 'y' and Q4B2 != 'n':
            Q4B2 = input("\nPlease enter either 'y' or 'n'.")
          print('Calculating...')
          countdown(1)
          os.system('clear')


#-------------yes Arizona
#Suns
          if Q4B2 == 'y':
            print("Your team are the firebirds of the league... \nthe " + Fore.RED +   western[1] + Fore.WHITE + '!\n')
            img = r'suns.png'
            screen.bgpic(img)  


 #-------------no Arizona
 #blazers
          elif Q4B2 =="n":
            print("Your team are the trailblazers of the league... \nthe " + Fore.RED + western[4] + Fore.WHITE + '!\n' )
            img = r'trailblazers.png'
            screen.bgpic(img)









#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------









#---------------------------------Play again-----------------------
    print(space)
    again = input("\nWould you like to play again? ('y' or 'n')")
    again = again.lower()

    #if the user enters a wrong keystroke
    while again != "y" and again != 'n':
      again = input("\nPlease enter either 'y' or 'n'.")
      again = again.lower()

    if again == "n":
      print ("Thanks for playing! :)")
      break

    if again == "y":
      print('\nThe screen will soon clear...')
      countdown(3)
      os.system('clear')
 
main()

#Stan did the eastern conference teams (and did the picture software)
#Jashan did the western conference