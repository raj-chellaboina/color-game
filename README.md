# Color Game

A simple and fun color recognition game built with Python's Tkinter library. The game tests your ability to quickly identify the color of the text displayed, not the word itself. Audio feedback is provided for correct and incorrect answers, as well as for game events.

## Features

- Interactive GUI using Tkinter
- Randomized color challenges
- Score tracking and countdown timer
- Audio feedback for correct/wrong answers and game results (requires pygame)
- Simple rules and easy to play

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- pygame

## How to Run

1. Install the required dependencies:
    ```sh
    pip install pygame
    ```
2. Make sure you have the required sound files in the specified paths (see the code for details).
3. Run the game:
    ```sh
    python color_game.py
    ```

## How to Play

- Press the **Enter** key to start the game.
- Type the **color of the text** shown (not the word itself) and press Enter.
- Your score and time left are displayed.
- Audio cues will let you know if your answer is correct or wrong.
- Try to score as high as possible before time runs out!

## Customization

- You can change the list of colors or update the sound file paths in [`color_game.py`](color_game.py).

## License

This project is for educational purposes.
