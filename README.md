# The COLOR Game

## Prerequisites

pip install tkinter

## Overview:

A one-player game to test users on their typing, concentration, and memory. Players are presented with a joke that may or may not coordinate with the visual color font. The player must type the color of the word, rather than the color that is spelled by the word. A countdown timer will be set for each round that the player plays, limiting their time to think and forcing time optimization when typing in colors.

## Problem being Solved

With technology advancing at a fast pace, students are beginning to learn how to keyboard at a young age. This program will assist in enhancing their accuracy, precision and their muscle memory abilities all in a fun hands on game.

## Functionality:

### The player will be able to play this game by following these steps:

1. Display on the first screen the instructions, time left, and different color options
2. Randomizes a joke from the icanhazdadjoke API and adds a color to it
3. Time Display for the user each round decreases
4. User is able to guess the color of the joke ( adds a humurous approach)
5. The user needs to answer the text box with the correct color name in order to get a point

## Features:

- Change fonts
- Screen size
- Add a starting screen for username input
- Game over screen
- Main target audience - Students

## Technical Requirements:

### _Tools_

- Frontend: Tkinter GUI
- Backend: Python imported random, requests, tkinter
- API: "icanhazdadjoke"
- URL: https:icanhazdadjoke.com/

# Operations:

1. fetch_random_dad_joke()

2. startGame()

3. nextColour()

4. countdown()

5. openSecondScreen()

# Algorithms:

1. Import the necessary modules, including tkinter,requests and random.
2. Create a list of possible colors and initialize the score and the time left.
3. Create a GUI window using tkinter and set the window title and size.
4. Add labels for instructions, score, time left, and color display.
5. Add a text entry box for typing in colors.
6. Start the GUI main loop.
7. During gameplay, display a random color on the random dad joke and wait for player input.
8. Check if the typed color matches the displayed color and update the score.
9. Repeat steps 7 and 8 until the game ends (time runs out).
10. End the game and display the final score.
