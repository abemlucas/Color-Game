# import the modules
import tkinter
import random

# list of possible colour.
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

# the game time left, initially 30 seconds.
timeleft = 30

# function that will start the game.


def startGame(event):

    if timeleft == 30:
        # start the countdown timer.
        countdown()

    # choose the next colour.
    nextColour()

# Function to choose and display the next colour.


def nextColour():

    # use the globally declared 'score'
    # and 'play' variables above.
    global score
    global timeleft

    # if a game is currently in play
    if timeleft > 0:

        # make the text entry box active.
        e.focus_set()

        # if the colour typed is equal
        # to the colour of the text
        if e.get().lower() == colours[1].lower():

            score += 1

        # clear the text entry box.
        e.delete(0, tkinter.END)

        random.shuffle(colours)

        # change the colour to type, by changing the
        # text _and_ the colour to a random colour value
        label.config(fg=str(colours[1]), text=str(colours[0]))

        # update the score.
        scoreLabel.config(text="Score: " + str(score))


# Countdown timer function
def countdown():

    global timeleft

    # if a game is in play
    if timeleft > 0:

        # decrement the timer.
        timeleft -= 1

        # update the time left label
        timeLabel.config(text="Time left: "
                         + str(timeleft))

        # run the function again after 1 second.
        timeLabel.after(1000, countdown)


def openSecondScreen():
    root.withdraw()  # Hide the main window

    second_screen = tkinter.Toplevel()  # Create the second screen
    second_screen.title("Second Screen")

    # Add widgets and customize the second screen
    second_label = tkinter.Label(
        second_screen, text="This is the second screen")
    second_label.pack()

    # Add a button to go back to the main screen
    back_button = tkinter.Button(second_screen, text="Go Back", command=goBack)
    back_button.pack()


def goBack():
    root.deiconify()  # Show the main window
    second_screen.destroy()  # Destroy the second screen


# Driver Code

# create a GUI window
root = tkinter.Tk()

# set the title
root.title("COLORGAME")

# set the size
root.geometry("800x500")

# set background color
root.configure(background='blue')


# add an instructions label
instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!",
                             font=('Helvetica', 20))
instructions.pack()

# add a score label
scoreLabel = tkinter.Label(root, text="Press enter to start",
                           font=('Helvetica', 20))
scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text="Time left: " +
                          str(timeleft), font=('Helvetica', 20))

timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# add a text entry box for
# typing in colours
e = tkinter.Entry(root)

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()
