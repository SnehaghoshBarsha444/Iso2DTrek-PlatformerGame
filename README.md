# Simple Retro Game Platformer

This is a simple platformer game built using Python and Pygame. In this game, you control a main character that can move left and right and jump across platforms. Your goal is to avoid enemies and reach the end platform to win the game.

## Features

- **Platformer gameplay:** Run, jump, and avoid enemies.
- **Simple enemy movement:** Enemies patrol on platforms and the player resets on collision.
- **End-level win condition:** Reach the last platform to win.

## Requirements

- Python 3.6+
- Pygame (installed via `requirements.txt`)

## Installation

1. Clone the repository.
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

Execute the following command from the project directory:

```bash
python main.py
```

## Controls

- **Left Arrow:** Move left.
- **Right Arrow:** Move right.
- **Space:** Jump (when on a platform).

## Notes

- The game window is 800x600 pixels.
- If the player collides with an enemy, the player respawns at the starting position.
- Reaching the end platform displays a win message!

Enjoy the game!
