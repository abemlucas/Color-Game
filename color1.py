import tkinter
import random
import os
import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from googleapiclient.discovery import build

# List of possible colors.
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black',
          'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
time_left = 30
# Replace with the actual path to your credentials file
credentials_file = 'path/to/credentials.json'

# Load credentials from JSON file
credentials = service_account.Credentials.from_service_account_file(
    credentials_file, scopes=['https://www.googleapis.com/auth/spreadsheets'])

# Authorize the client
credentials.refresh(Request())
google.auth.default(
    scopes=['https://www.googleapis.com/auth/spreadsheets'], credentials=credentials)

# Create the Google Sheets service
service = build('sheets', 'v4', credentials=credentials)
# Replace with your actual Google Sheets spreadsheet ID
spreadsheet_id = 'your_spreadsheet_id'

# Function to update the leaderboard in the Google Sheets


def update_leaderboard():
    values = [
        ['Player', 'Score'],
        ['Player1', 10],
        ['Player2', 8],
        ['Player3', 6],
        # Add more rows as needed
    ]
    body = {
        'values': values
    }
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range='Sheet1!A1:B',
        valueInputOption='RAW',
        body=body
    ).execute()

# Function that will start the game


def start_game(event):
    global time_left
    if time_left == 30:
        # Start the countdown timer.
        countdown()

# Function to choose and display the next color.


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
        if e.get().lower() == colors[1].lower():

            score += 1

        # clear the text entry box.
        e.delete(0, tkinter.END)

        random.shuffle(colors)

        # change the colour to type, by changing the
        # text _and_ the colour to a random colour value
        time_label.config(fg=str(colors[1]), text=str(colors[0]))

        # update the score.
        score_label.config(text="Score: " + str(score))

# Countdown timer function

def countdown():
    global time_left

    if time_left > 0:
        # Decrement the timer.
        time_left -= 1

        # Update the time left label
        time_label.config(text="Time left: " + str(time_left))

        # Run the function again after 1 second.
        time_label.after(1000, countdown)


# Create a GUI window
root = tkinter.Tk()

# Set the title
root.title("Color Game")

# Set the size
root.geometry("800x500")

# Set background color
root.configure(background='blue')

# Add instructions label
instructions = tkinter.Label(
    root, text="Type in the color of the words, and not the word text!", font=('Helvetica', 20))
instructions.pack()

# Add score label
score_label = tkinter.Label(
    root, text="Press enter to start", font=('Helvetica', 20))
score_label.pack()

# Add time left label
time_label = tkinter.Label(
    root, text="Time left: " + str(time_left), font=('Helvetica', 20))
time_label.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# add a text entry box for
# typing in colours
e = tkinter.Entry(root)

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', start_game)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()