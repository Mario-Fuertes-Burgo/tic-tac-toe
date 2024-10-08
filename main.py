import customtkinter
import random



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.geometry("300x400")

# Font for buttons
buttonFont =customtkinter.CTkFont(size=28)


#Array that stores the state of the game E->empty, 
gameState = []
numberButtonsClicked = 0



# Returns the button square played by the AI
def aiButtonPlayed():
    valid = False

    while valid == False:
        randomButtonNumber = random.randint(0, 8)
        
        if gameState[randomButtonNumber].cget("state") == "normal":
            return gameState[randomButtonNumber]

        





def playerPlay(button):
    global numberButtonsClicked
    if numberButtonsClicked < 8:
        button.configure(text="X")
        button.configure(state="disabled")
        numberButtonsClicked += 1
        

        





def aiPlay(button):
    global numberButtonsClicked
    if numberButtonsClicked < 8:
        button.configure(text="O")
        button.configure(state="disabled")
        numberButtonsClicked += 1
      



def check_victory():
    # Define winning combinations (rows, columns, diagonals)
    winning_combinations = [
        [0, 1, 2],  # First row
        [3, 4, 5],  # Second row
        [6, 7, 8],  # Third row
        [0, 3, 6],  # First column
        [1, 4, 7],  # Second column
        [2, 5, 8],  # Third column
        [0, 4, 8],  # First diagonal
        [2, 4, 6],  # Second diagonal
    ]
    
    # Iterate through each possible winning combination
    for combination in winning_combinations:
        b1, b2, b3 = combination
        if gameState[b1].cget("text") == gameState[b2].cget("text") == gameState[b3].cget("text") and gameState[b1].cget("text") != "":
            return gameState[b1].cget("text")  # Return the winner ("X" or "O")
    
    # No winner found
    return None
        




# Function activated each round. A round starts when the player click the button and ends when the ai has played
def gameRound(buttonClicked):

    # The game state is changed by the PLAYER input
    playerPlay(buttonClicked)


    # The game state is changed by the AI input
    aiPlay(aiButtonPlayed())

    printGameState()

    # Victory is checked
    if check_victory() != None:
        print("The winner is: ", end="")
        print(check_victory())
        root.destroy()

    



def printGameState():
    print("\nGAME STATE")
    for i in range(9):
        if i == 3 or i == 6:
              print()
        print("[", end="", flush=True)
        print(gameState[i].cget("text"), end="]", flush=True)

    print("")




for i in range(9):
        button = customtkinter.CTkButton(master=root, text="", font=buttonFont, border_width=1, border_color="black", corner_radius=0)
        button.configure(height = 100, width=100)
        button.grid(row = i//3, column = i%3)
                    
        button.configure(command=lambda btn=button: gameRound(btn))
        
        gameState.append(button)





root.mainloop()