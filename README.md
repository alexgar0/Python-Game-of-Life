# Python Game of Life
This is the simple implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) in Python3

## Required libs:
* [Numpy](https://github.com/numpy/numpy)
* [pygame](https://github.com/pygame)

## Run the game:
`python game.py`

## Change the resolution:
To change the main window resolution and cell size, simply edit the values in the following lines:
```python
 RES = WIDTH, HEIGHT = (2000, 1000)
 TILE = 13
```

***Warning: A large field may cause the game to crash or slow down.***

You can change the game speed by editing the FPS value: 
```python
        FPS = 60
```

# In-game controls:
`spacebar` - to pause/unpause

`Left mouse button` - to place a cell

`Right mouse button` - to remove a cell

## TODO:

- [x] Main logic
- [x] Main window
- [ ] Make the game work faster
- [ ] Make it easy to change resolution and field size
- [ ] Make the field infinite
- [ ] Make free camera view
