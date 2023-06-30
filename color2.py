import tkinter
import random
import requests

def fetch_random_dad_joke():
    url = 'https://icanhazdadjoke.com/'
    
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Your User Agent'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        joke = data['joke']
        return joke


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
        dad_joke = fetch_random_dad_joke()
        label.config(fg=str(colours[1]), text=dad_joke)
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
    second_screen.configure(background='#ADD8E6')

    #Leaderboard label
    leaderboard_label = tkinter.Label(second_screen, text="CONGRATULATION!", font=('Helvetica', 40))
    leaderboard_label.pack(pady=30)
    # Add score label to display the user's score
    score_label = tkinter.Label(second_screen, text="Total Score: " + str(score), font=('Helvetica', 20))
    score_label.pack(pady=10)

# Create the main window
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("1600x1600")
root.configure(background='#ADD8E6')

welcome = tkinter.Label(root, text="WELCOME TO THE COLOR GAME!", font=('Helvetica', 40))
welcome.pack()

instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 20))
instructions.pack()


options_label=tkinter.Label(root, text="Choose From: " + ", ".join(colours), font=('Helvetica', 20))
options_label.pack()

score_label = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 20))
score_label.pack()

time_label = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 20))
time_label.pack()

label = tkinter.Label(root, font=('Helvetica', 20))
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()

e.focus_set()

root.mainloop()