# The COLOR Game
## Prerequistes
-pip install pillow

## Overview:

A one-player game to test users on their typing, concentration, and memory. Players are presented with a word that may or may not coordinate with the visual color font. The player must type the color of the word, rather than the color that is spelled by the word. A countdown timer will be set for each round that the player plays, limiting their time to think and forcing time optimization when typing in colors. Highscores for all game history will be stored and presented once the player types an error,

## Audience:

Keyboarding students

## User Requirements:

1. User needs to input their name
   Used to clearly indicate the winner
2. Display the name of the colors
3. Add up total points for a high score
   Used to reflect the user’s game standing
4. The user needs to answer the text box with the correct color name
   Time Display for the user each round

## Features:

- Change fonts
- Screen size
- Add a starting screen for username input
- Game over screen (saves player name)

## Technical Requirements:

### _Tools_

- Frontend: Tkinter GUI
- Backend: Python imported random
- API: N/A

# Operations:

1. startGame():

- Gets triggered when the enter key is pressed
- Checks if the game is starting for the first time @ timeleft =30s
- Starts the timer if condition is met.

2. nextColour():

- Check if there is still time left in the game.
- Make the text entry box.
- Check if the color typed by the player matches the color displayed.
- If it matches, increase the score by 1.
- Clear the text entry box and shuffle the list of colors.
- Change the color to type by updating the label's text and color.
- Update the score label with the current score.

3. countdown():

- Check if there is still time left in the game.
- Decrement the timer by 1.
- Update the time left label.
- Schedule the function to run again after 1 second.

# Algorithms:

1. Import the necessary modules, including tkinter and random.
2. Create a list of possible colors and initialize the score and the time left.
3. Create a GUI window using tkinter and set the window title and size.
4. Add labels for instructions, score, time left, and color display.
5. Add a text entry box for typing in colors.
6. Start the GUI main loop.
7. During gameplay, display a random color and wait for player input.
8. Check if the typed color matches the displayed color and update the score.
9. Repeat steps 7 and 8 until the game ends (time runs out).
10. End the game and display the final score.
