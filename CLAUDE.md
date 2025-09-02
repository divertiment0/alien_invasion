# Claude AI Development Notes

## Project: Alien Invasion Game

### Project Goal
Let's build a game called Alien Invasion! We'll use Pygame, a collection of fun, powerful Python modules that manage graphics, animation, and even sound, making it easier for you to build sophisticated games. With Pygame handling tasks like drawing images to the screen, you can focus on the higher-level logic of game dynamics.

### Development Commands
- **Run game**: `python alien_invasion.py`
- **Install dependencies**: `pip install pygame`

### Key Files
- `alien_invasion.py` - Main game loop and event handling
- `ship.py` - Ship class with movement logic
- `settings.py` - Game configuration settings
- `bullet.py` - Bullet mechanics

### Known Issues & Fixes
1. **Diagonal Movement Prevention**: Ship movement uses `elif` statements in `ship.py:33-40`, preventing simultaneous directional movement
2. **Fullscreen Mode**: Available but commented out in `alien_invasion.py:24-27`

### GitHub Repository
- **Repo**: divertiment0/alien_invasion
- **Issues Created**: 
  - Fullscreen mode implementation
  - Diagonal movement fix

### Controls
- Arrow keys: Ship movement
- Q: Quit game
- Space: Fire bullets

### Recent Changes
- Added bullet firing functionality
- Fixed UP/DOWN key event handlers
- Resolved pygame.Q AttributeError (changed to pygame.K_q)

> Horas non numero nisi serenas
- Bash commands
- run the game : python3 alien_invasion &