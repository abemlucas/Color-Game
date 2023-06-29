import tkinter
import random
import os
import os
import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account


CLIENT_ID = "155346813761-q9bgi1t1n8v5h4liam00h32h52ffnu56.apps.googleusercontent.com"
CLIENT_SECRET = "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"

# list of possible colours.
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 30


def startGame(event):
    if timeleft == 30:
        countdown()
    nextColour()


def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
    else:
        openSecondScreen()


def openSecondScreen():
    root.withdraw()  # Hide the main window

    second_screen = tkinter.Toplevel()  # Create the second screen
    second_screen.title("Second Screen")
    second_screen.geometry("400x300")

    # Add score label to display the user's score
    score_label = tkinter.Label(
        second_screen, text="Your Score: " + str(score), font=('Helvetica', 20))
    score_label.pack(pady=50)


root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("800x500")
root.configure(background='blue')

instructions = tkinter.Label(
    root, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 20))
instructions.pack()

scoreLabel = tkinter.Label(
    root, text="Press enter to start", font=('Helvetica', 20))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: " +
                          str(timeleft), font=('Helvetica', 20))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

# save client ID and client secret in the code
# authenticate and authorize access to Google API

# Set up credentials
credentials = None
token_path = 'token.pickle'
scopes = ['https://www.googleapis.com/auth/spreadsheets']

if os.path.exists(token_path):
    with open(token_path, 'rb') as token:
        credentials = pickle.load(token)

if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', scopes)
        credentials = flow.run_local_server(port=0)

    with open(token_path, 'wb') as token:
        pickle.dump(credentials, token)

# Build the service
service = build('sheets', 'v4', credentials=credentials)


# reading a data from a sheet
def read_sheet(spreadsheet_id, range_name):
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=range_name
    ).execute()
    values = result.get('values', [])
    return values


# writing data to a sheet
def write_sheet(spreadsheet_id, range_name, values):
    body = {
        'values': values
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()
    return result


root.mainloop()
