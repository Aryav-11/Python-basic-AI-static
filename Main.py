import os
import time # Imports Time For Smooth Effect
import tkinter 
import pygame # Imports Pygame For Our Game
import sys # Imports Sys To Shut Pygame Off
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
# Must Access this to continue.
def main():
       global running
       running = True
       while running:
              global UserName
              UserName = input("Enter Your Name: ")
              PassWord = input ("Enter Password: ")
              User_displayer = "Your Name is: "+ UserName

              if UserName == "Max" and PassWord == "Max_Dom11":
                     time.sleep(1)
                     print(User_displayer)
                     logged_Max()

              elif UserName == "Zack" and PassWord == "Zack_King":
                     print(User_displayer)
                     logged_Zack()
                     
              elif UserName == "David" and PassWord == "David_Bombal":
                     print(User_displayer)
                     logged_David()
              
              elif UserName == "Head" and PassWord == "Head123":
                     print(User_displayer)
                     logged_Head()
              else:
                     try:
                        if (UserName != "Max" or "Zack" or "David" or "Head") or (PassWord != "Max_Dom11" or "Zack_King" or "David_Bombal" or "Head123"):
                            
                             raise NameError
                      
                     except NameError:
                        User_displayer = print("Username Or Password Is Not Correct")
                        exit()
def logged_Max():
    time.sleep(1)
    print ("Welcome to Syndrome " + UserName)
    print("List's Of Things To Do:\n")
    print("  1) Open Calculator")
    print("  2) Open Code Editor")
    print("  3) Exit")
    Input_from_Max = int(input("Enter Your Selection: "))
    Selec = " Your Selection Is: {}"
    print(UserName + Selec.format(Input_from_Max))
    print(Input_from_Max)
    if Input_from_Max == 1:
       cls()
       Calculator_for_Max()
       print("\n\n\n")
       logged_Max()
    elif Input_from_Max == 2:
           cls()
       #     Code_editor_for_Max()
           logged_Max()
    elif Input_from_Max == 3:
           cls()
           print("Exit Called")
           print("Exited")
           exit()
    else:
              print("\n\nInvalid Value. Please Try Again With A Suitable Value!")
              logged_Max()
              exit()
    
              


def Calculator_for_Max():
       print("Calculator Called\n\n")
       num1 = input("Enter First Number: ")
       char = input("Enter Your Operator: ")
       num2 = input("Enter Second Number: ")
       State = "Your Anwser Is: {}"
  
       if num1 == int:
         num1 == int(input("Enter First Number:"))
       elif num1 == float:
         num1 == float(input("Enter First Number"))
              
       if num2 == int:
         num2 == int(input("Enter Second Number"))
       elif num2 == float:
         num2 == float(input("Enter Second Number"))
       
       if char == '+':           
              print(State.format(num1 + num2))
       elif char == '-':
              print(State.format(num1 - num2))
       elif char == '*':
              print(State.format(num1 * num2))
       elif char == '/':
              print(State.format(num1 / num2))
       else:
              print("Invalid Operator")
              exit()

# def Code_editor_for_Max():
#      compiler = Tk() # Creates or initilises compiler
#      compiler.title('Code Editor') # Types Title
#      menu_bar = Menu(compiler)
#      editor = Text() # Make's area typable
#      editor.pack()
#      compiler.mainloop()



def logged_Zack():
    time.sleep(1)
    print ("Welcome to Syndrome " + UserName)
    print("List's Of Things To Do: ")
    print("  1) Open Game's")
    print("  2) Exit")
    Input_from_Zack = int(input("Enter Your Selection: "))
    Selec = print("Your Selection Is {}")
    print(UserName + Selec.format(Input_from_Zack))
    print(Input_from_Zack)
    if Input_from_Zack == 1:
           cls()
           print("Games Called")
           exit()
    
    exit()
    

def Games_For_Zack():
       print("List Of Games To Play: ")
       print("  1)  ")

def logged_David():
    time.sleep(1)
    print ("Welcome to Syndrome " + UserName)
    exit()
    
def logged_Head():
    time.sleep(1)
    print ("Welcome to Syndrome " + UserName)
    exit()
    
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

main()

