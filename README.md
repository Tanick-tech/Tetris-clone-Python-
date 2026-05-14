# Tetris Clone in Python

Credit: Net Ninja
Tutorial Playlist: https://www.youtube.com/playlist?list=PL4cUxeGkcC9iurLoO9Mu7GqsKlxEXcf8m

Brief summary:
This repository aims to reconstruct a Tetris clone using Python as an introductory project for high-school students to become familiar with the concept of Object-Oriented Programming (OOP), one of the fundamental programming paradigms in Computer Science.

The project is designed to help beginners understand how classes and objects work together while also introducing game development concepts using pygame.


## Tech Stack
- Python
- Pygame
## Highlight Features

### 1. Object-Oriented Programming (OOP)

This game is built using classes and objects, helping students understand important OOP concepts such as:

* Encapsulation
* Inheritance
* Modular code structure

### 2. File Integration in Python

This repository demonstrates how external files such as graphics, sounds, and configurations can be integrated into a Python project while maintaining an organized project structure.

### 3. Dual Platform Experience

This project functions on two different platforms:

#### Visible Platform

A playable Tetris game window built with pygame where users can interact with blocks, scoring systems, and gameplay mechanics.

#### Invisible Platform (The Matrix)

The underlying OOP codebase that controls the game logic behind the scenes, allowing students to study how the mechanics are implemented internally.
## Directory Structure
Tetris-clone-Python-/

├── Code/

│   ├── game.py

│   ├── main.py

│   ├── preview.py

│   ├── score.py

│   ├── settings.py

│   └── timer.p

│

├── Graphics/

├── Sound/

│

├── .gitignore

├── LICENSE

└── README.md
- "main.py" starts the game
- "game.py" handles the main game logic
- "preview.py" manages upcoming tetromino previews
- "score.py" handles scoring
- "settings.py" stores game settings and constants
- "timer.py" controls timing/game speed
- "Graphics/" contains images and visual assets
- "Sound/" contains sound effects and music## Run Locally

Clone the project

```bash
git clone https://github.com/Tanick-tech/Tetris-clone-Python-.git
```

Go to the project directory

```bash
cd Tetris-clone-Python-
```

Install dependencies

```bash
pip install pygame
```

Run the game

```bash
python Code/main.py
```
## Conclusion

This project serves as both a game and a learning tool.

By exploring the code, students will:

* Understand how classes and objects work in Python
* Learn how to structure programs using OOP principles
* Explore a different perspective on game development through visible and invisible systems
* Gain confidence in building interactive applications
* Apply simple mathematical concepts in real projects
