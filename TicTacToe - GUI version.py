from tkinter import *
import random

def next_turn(row, column): # checks the next turn of the grid 
   
    global player # makes the variable accessible throught the entire program
    
    if buttons[row][column]['text'] == "" and check_winner() is False: # check if thee button clicked is empty (There is no winner)
        
        if player == players[0]: # this signifies the player at index 0 which is "o"
             
            buttons[row][column]['text'] = player
            
            if check_winner() is False:
                player = players[1] # this swaps the player
                label.config(text=(players[1] + " turn"))
                
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
                
            elif check_winner() == 'Tie':
                label.config(text=("Tie!"))
        
        else: # nthis signifies the plater at index 1 which is "x"
            
            buttons[row][column]['text'] = player
            
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
                
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
                
            elif check_winner() == 'Tie':
                label.config(text=("Tie!"))
    
def check_winner(): # checks winnig conditions of the game
    
    for row in range(3): # to loop through the row to check for winning
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg='green')
            buttons[row][1].config(bg='green')
            buttons[row][2].config(bg='green')
            return True
   
    for column in range(3): 
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg='green')
            buttons[1][column].config(bg='green')
            buttons[2][column].config(bg='green')
            return True
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True
    
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='yellow')
        return "Tie"
    
    else:
        return False

def empty_spaces(): # checks for empty spaces in the grid
    spaces = 9 # creating a local variables - this is number of spaces in the grid
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1
                
    if spaces == 0:
        return False
    else:
        return True
        

def new_game():

    global player 
    
    player = random.choice(players)
    
    label.config(text=player + " Turn")
    
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")
    
    


window = Tk()

icon = PhotoImage(file='Capture001.png')
window.iconphoto(True, icon)

window.title("Tic Tac Toe")
players = ['x', 'o']
player = random.choice(players)
buttons = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    ]

label = Label(window, text= player + ' Turn', font=('consolas', 20))
label.pack(side='top')

reset_button = Button(window, text='Restart', font=('consolas', 10), command=new_game)
reset_button.pack(side='top')

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2, command= lambda row=row, column=column: next_turn(row, column))
        
        buttons[row][column].grid(row=row, column=column)

window.mainloop()