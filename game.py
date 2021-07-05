import pygame
import numpy as np

RES = WIDTH, HEIGHT = (2000, 1000)  # main window resolution
FPS = 60
pygame.init()
pygame.font.init()

BACKGROUND_COLOR = pygame.Color("black")
TILE = 13  # pixels per one cell
W, H = WIDTH // TILE, HEIGHT // TILE
FONT = pygame.font.SysFont('arial', TILE if TILE > 30 else 30)

# field array
current_field = np.zeros(shape=(W, H))

# randomize array
current_field = np.round(np.random.sample((W, H)))

neighbours = lambda f, x, y: [f[x - 1][y + 1], f[x][y + 1], f[x + 1][y + 1], f[x - 1][y], f[x + 1][y],
                              f[x - 1][y - 1], f[x][y - 1], f[x + 1][y - 1]]


def find_neighbours_count(field, x, y):
    """Returns the number of neighbors of a specific cell"""
    return neighbours(field, x, y).count(1)


def process_field(field):
    """Returns the next state of the field"""

    new_field = np.zeros(shape=field.shape)
    for x in range(1, W - 1):
        for y in range(1, H - 1):
            neighbour_count = find_neighbours_count(field, x, y)
            if field[x][y] == 0 and neighbour_count == 3:
                new_field[x][y] = 1
            elif field[x][y] == 1:
                if neighbour_count == 2 or neighbour_count == 3:
                    new_field[x][y] = 1
                else:
                    new_field[x][y] = 0
    return new_field


def draw_field(field):
    """Draws a field"""

    rects = []
    for x in range(W):
        for y in range(H):
            if field[x][y] == 1:
                rects.append(pygame.Rect(x * TILE, (H - y) * TILE, TILE - 3, TILE - 3))
    [pygame.draw.rect(scene, (255, 255, 255), rect) for rect in rects]


def draw_border():
    rects = []
    rects.append(pygame.Rect(0, 0, W * TILE, TILE))
    rects.append(pygame.Rect(0, H * TILE, (W + 1) * TILE, TILE))
    rects.append(pygame.Rect(W * TILE, 0, TILE, H * TILE))
    rects.append(pygame.Rect(0, 0, TILE, H * TILE))
    # rects.append(pygame.Rect(x * TILE, 0, TILE, TILE))
    [pygame.draw.rect(scene, (123, 123, 123), rect) for rect in rects]


def place_cell_in_pos(field, pos, val):
    x = pos[0]
    y = pos[1]
    x = x // TILE
    y = H - (y // TILE)
    if x != 0 and x != W and y != 0 and y != H:
        field[x][y] = val


scene = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(W) for y in range(H)]
on_pause = False

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # mouse left click to add a cell
            if event.button == 1:
                place_cell_in_pos(current_field, event.pos, 1)

            # mouse right click to remove a cell
            elif event.button == 3:
                place_cell_in_pos(current_field, event.pos, 0)

        if event.type == pygame.KEYDOWN:
            # space to pause
            if event.key == pygame.K_SPACE:
                on_pause = not on_pause

            # backspace to clear the field
            elif event.key == pygame.K_BACKSPACE:
                current_field = np.zeros(shape=(W, H))

    scene.fill(BACKGROUND_COLOR)

    # make grid
    # [pygame.draw.rect(scene, (80, 80, 80), i_rect, 1) for i_rect in grid]

    # draw
    draw_field(current_field)
    draw_border()
    if on_pause:
        pause_text = FONT.render('Paused', True, (180, 0, 0))
        scene.blit(pause_text, (TILE, 0))
    # update field
    if not on_pause:
        current_field = process_field(current_field)

    pygame.display.flip()
    clock.tick(FPS)
