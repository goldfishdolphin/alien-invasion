# Alien Invasion 🚀👽

A classic space shooter game built with Python and Pygame where you defend Earth from waves of alien invaders!

## 🎮 Game Description

In Alien Invasion, you pilot a rocket ship positioned at the bottom of the screen. Your mission is to destroy waves of alien ships that move across and down the screen. Each wave you defeat becomes progressively faster and more challenging. Can you achieve the high score?

## 🎯 Game Rules

- **Objective**: Destroy all aliens to advance to the next level
- **Lives**: You start with 3 ships (lives)
- **Game Over**: Lose all ships when aliens hit your ship or reach the bottom
- **Scoring**: Earn points for each alien destroyed, with increasing point values per level
- **Progression**: Each new wave moves faster than the previous one

## 🎮 Controls

| Key | Action |
|-----|--------|
| `←` `→` | Move ship left/right |
| `SPACEBAR` | Fire bullets |
| `Q` | Quit game |
| `Mouse Click` | Click "Play" button to start |

## 🚀 How to Run

1. **Prerequisites**: Make sure you have Python and Pygame installed
   ```bash
   pip install pygame
   ```

2. **Run the game**:
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
alien-invasion/
├── main.py                 # Entry point to start the game
├── alien_invasion.py       # Main game class and logic
├── ship.py                 # Player ship class
├── alien.py               # Alien enemy class
├── bullet.py              # Bullet projectile class
├── button.py              # Game UI button class
├── settings.py            # Game configuration and settings
├── game_stats.py          # Game statistics tracking
├── scoreboard.py          # Score display and management
├── images/
│   ├── ship.bmp           # Player ship sprite
│   └── alien.bmp          # Alien enemy sprite
└── README.md
```

## 🎨 Game Features

- **Fullscreen gameplay** for immersive experience
- **Dynamic difficulty** - aliens move faster each level
- **Score system** with high score tracking
- **Lives display** showing remaining ships
- **Level progression** with increasing point values
- **Smooth sprite movement** and collision detection
- **Limited ammunition** system (3 bullets max on screen)

## 🛠️ Technical Details

- **Language**: Python 3.x
- **Framework**: Pygame
- **Graphics**: Bitmap sprites (.bmp format)
- **Architecture**: Object-oriented design with separate classes for each game component

## 🎵 Game Mechanics

### Ship Movement
- Continuous movement while arrow keys are held
- Ship stays within screen boundaries
- Smooth acceleration based on [`ship_speed`](settings.py) setting

### Alien Fleet
- Grid formation of aliens that move together
- Horizontal movement with direction changes at screen edges
- Vertical descent when hitting screen boundaries
- Fleet speed increases with each level

### Bullet System
- Maximum of 3 bullets on screen at once
- Bullets removed when they hit aliens or leave the screen
- Collision detection between bullets and aliens

### Scoring
- Points awarded for each alien destroyed
- Score multiplier increases with each level
- High score persistence during game session

## 🔧 Customization

Modify [`settings.py`](settings.py) to customize:
- Ship speed and bullet properties
- Screen dimensions and colors
- Alien movement patterns
- Scoring system
- Difficulty progression

## 🎮 Screenshots

<img width="1000" alt="Alien Invasion Game Screenshot" src="https://github.com/user-attachments/assets/d02193d6-7613-4a9f-ad31-dfcc53c38879" />

## 📝 License

This project is open source. Feel free to modify and distribute.

---

**Enjoy defending Earth from the alien invasion! 🌍**
