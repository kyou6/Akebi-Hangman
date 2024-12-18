# Akebi-Hangman

Akebi-Hangman is a visually enhanced fork of the classic Hangman game from [techwithtim/Hangman](https://github.com/techwithtim/Hangman) using PyGame. 

This version incorporates a revamped UI, custom anime-inspired graphics, and enhanced audio effects for a more immersive gaming experience.

<img width=100% src="https://github.com/user-attachments/assets/0ffa3899-0eb4-44ec-8970-9400f27d634b">


## Table of Contents
- [What’s New?](#whats-new)
- [Features](#features)
- [How to Play](#how-to-play)
- [Files and Structure](#files-and-structure)
- [Preview](#preview)
- [Installation](#installation)
- [Credits](#credits)

## What's New?

- **Revamped Layout:**
  - Updated game interface with an improved design for better visual appeal.

- **Custom Anime Graphics:**
  - Replaced traditional hangman images with self-drawn anime-style characters inspired by the anime "Akebi."
  - Images dynamically change as incorrect guesses are made, progressing from `hangman1` to `hangman7`.

- **Enhanced Win and Death Screens:**
  - Added unique UI for both winning and losing scenarios.

- **Background Sound and Effects:**
  - Added a background music track (`bg.mp3`).
  - Included a click sound effect (`pop.mp3`) for button interactions.

- **Expanded Word List:**
  - The game now features an updated set of word choices located in `words.txt`.


## Features

- **Dynamic Graphics:**
  - Progressive visuals as the game unfolds.
  - Centered word display overlaying custom anime images.

- **Sound Effects:**
  - Background music loops continuously for an engaging experience.
  - Interactive button sounds for better feedback.

- **Enhanced Gameplay UI:**
  - Clearly displayed guesses.
  - Highlighted win or loss conditions with visual cues.



## How to Play

1. Start the game by running main.py.
2. Guess the word by clicking on the letters or typing them on your keyboard.
3. Each incorrect guess progresses the hangman animation closer to completion.
4. Win by guessing the word before the hangman is fully drawn.
5. Lose if the hangman animation is completed before guessing the word.


## Files and Structure

- `main.py`: The core game logic.
- `resources/`:
  - `font/`: Custom fonts used in the game.
  - `hangman/`: Anime-style hangman images (`1.png` to `7.png`).
  - `sound/`: Audio files including background music (`bg.mp3`) and click effects (`pop.mp3`).
- `words.txt`: List of words used in the game.

## Preview

### Game Screen
<img width="640" src="https://github.com/user-attachments/assets/42b6ca5e-461c-40ea-974a-fc2acc1f4471">

### Win Screen
<img width="640" src="https://github.com/user-attachments/assets/bec404bf-be02-47c0-abc5-ff15c4ba8966">

### Loss Screen
<img width="640" src="https://github.com/user-attachments/assets/9fe4311c-9042-4ac3-aca0-5b452ab265e9">

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kyou6/Akebi-Hangman.git
   cd Akebi-Hangman
2. Install dependencies: Ensure that you have Python installed. Then, install Pygame:
    ```bash
    pip install pygame
 2. Run the game:
    ```bash
    python main.py
## Credits
Original Repository: [techwithtim/Hangman](https://github.com/techwithtim/Hangman)
