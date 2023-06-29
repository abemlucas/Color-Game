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


def next_color():
    global score
    global time_left

    if time_left > 0:
        # Make the text entry box active.
        entry.focus_set()

        # If the color typed is equal to the color of the text
        if entry.get().lower() == colors[1].lower():
            score += 1

        # Clear the text entry box.
        entry.delete(0, tkinter.END)

        random.shuffle(colors)

        # Change the color to type, by changing the text and the color to a random color value
        color_label.config(fg=str(colors[1]), text=str(colors[0]))

        # Update the score.
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
