import tkinter
import random

# List of possible colours.
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 30

def startGame(event):
    # Function to start the game when the enter key is pressed
    if timeleft == 30:
        countdown()
    nextColour()

def nextColour():
    # Function to choose and display the next colour
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        # Check if the entered colour matches the displayed colour
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        # Change the displayed colour and update the score
        label.config(fg=str(colours[1]), text=str(colours[0]))
        score_label.config(text="Score: " + str(score))

def countdown():
    # Countdown timer function
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        time_label.config(text="Time left: " + str(timeleft))
        time_label.after(1000, countdown)
    else:
        openSecondScreen()

def openSecondScreen():
    # Function to open the second screen and display the user's score
    root.withdraw()  # Hide the main window

    # Create the second screen window
    second_screen = tkinter.Toplevel()
    second_screen.title("Second Screen")
    second_screen.geometry("1600x1600")

    #Leaderboard label
    leaderboard_label = tkinter.Label(second_screen, text="LEADERBOARD: ", font=('Helvetica', 40))
    leaderboard_label.pack(pady=10)
    # Add score label to display the user's score
    score_label = tkinter.Label(second_screen, text="Your Score: " + str(score), font=('Helvetica', 20))
    score_label.pack(pady=10)

# Create the main window
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("1600x1600")
root.configure(background='red')

blank_label=tkinter.Label(root,text="")
instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 20))
instructions.pack()

score_label = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 20))
score_label.pack()
blank_label.pack()

options_label=tkinter.Label(root, text="Choose From: " + ", ".join(colours), font=('Helvetica', 20))
options_label.pack()
blank_label.pack()
time_label = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 20))
time_label.pack()

blank_label.pack()
blank_label.pack()
blank_label.pack()
blank_label.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()



e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

root.mainloop()
