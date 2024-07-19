import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grid Design")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)

# Grid size and block size
grid_size = 3
block_size = 30

# Define your color matrices here
rwg = ('r1', 'w7', 'g3')
rwb = ('r3', 'w9', 'b1')
owb = ('o1', 'w3', 'b3')
owg = ('o3', 'w1', 'g1')
ryg = ('r7', 'y1', 'g9')
ryb = ('r9', 'y3', 'b7')
oyb = ('o7', 'y9', 'b9')
oyg = ('o9', 'y7', 'g7')

rg = ('r4', 'g6')
ry = ('r8', 'y2')
rw = ('r2', 'w8')
rb = ('r6', 'b4')
ob = ('o4', 'b6')
og = ('o6', 'g4')
ow = ('o2', 'w2')
oy = ('o8', 'y8')
yb = ('y6', 'b8')
yg = ('y4', 'g8')
wb = ('w6', 'b2')
wg = ('w4', 'g2')


r = np.array(([rwg[0], rw[0], rwb[0]],
              [rg[0], 'r5', rb[0]],
              [ryg[0], ry[0], ryb[0]]))

w = np.array(([owg[1], ow[1], owb[1]],
              [wg[0], 'w5', wb[0]],
              [rwg[1], rw[1], rwb[1]]))

o = np.array(([oyg[0], oy[0], oyb[0]],
              [og[0], 'o5', ob[0]],
              [owg[0], ow[0], owb[0]]))

y = np.array(([ryg[1], ry[1], ryb[1]],
              [yg[0], 'y5', yb[0]],
              [oyg[1], oy[1], oyb[1]]))

g = np.array(([owg[2], wg[1], rwg[2]],
              [og[1], 'g5', rg[1]],
              [oyg[2], yg[1], ryg[2]]))

b = np.array(([rwb[2], wb[1], owb[2]],
              [rb[1], 'b5', ob[1]],
              [ryb[2], yb[1], oyb[2]]))

#    w
#  g r b   o
#    y
#                         [['w1' 'w2' 'w3']
#                          ['w4' 'w5' 'w6']
#                          ['w7' 'w8' 'w9']]
#               
# [['g1' 'g2' 'g3']       [['r1' 'r2' 'r3']       [['b1' 'b2' 'b3']         [['o9' 'o8' 'o7']
#  ['g4' 'g5' 'g6']        ['r4' 'r5' 'r6']        ['b4' 'b5' 'b6']          ['o6' 'o5' 'o4']                      
#  ['g7' 'g8' 'g9']]       ['r7' 'r8' 'r9']]       ['b7' 'b8' 'b9']]         ['o3' 'o2' 'o1']]
#
#                         [['y1' 'y2' 'y3']
#                          ['y4' 'y5' 'y6']
#                          ['y7' 'y8' 'y9']]



    

def rotate_90deg(origin_mat, left_mat, right_mat, up_mat, down_mat, no_of_rotation):
    # Check if all matrices are 3x3
    matrices = [origin_mat, left_mat, right_mat, up_mat, down_mat]
    for idx, mat in enumerate(matrices):
        if not isinstance(mat, np.ndarray):
            raise TypeError(f"Matrix at index {idx} is not a numpy array")
        if mat.shape != (3, 3):
            raise ValueError(f"Matrix at index {idx} is not a 3x3 matrix")

    # Check if no_of_rotation is a positive integer between 1 and 4
    if not isinstance(no_of_rotation, int):
        raise TypeError("Number of rotations must be an integer")
    if no_of_rotation < 1 or no_of_rotation > 4:
        raise ValueError("Number of rotations must be between 1 and 4 (inclusive)")
    
    
    if no_of_rotation == 4:
        return 
    
    for _ in range(no_of_rotation):
        origin_mat = np.rot90(origin_mat, 1)
        temp1 = up_mat[2, :][::-1].copy()
        temp2 = left_mat[:, 2].copy()
        temp3 = down_mat[0, :][::-1].copy()
        temp4 = right_mat[:, 0].copy()
        
        up_mat[:, 2] = temp1
        left_mat[0, :] = temp2
        down_mat[:, 0] = temp3
        right_mat[2, :] = temp4



# Grid positions and colors (adjusted to prevent overlap)
grids = [
    (150, 50, WHITE, w),    # Top
    (50, 150, GREEN, g),    # Left
    (150, 150, RED, r),       # Center
    (250, 150, BLUE, b),     # Right
    (150, 250, YELLOW, y), # Bottom
    (350, 150, ORANGE, o)  # Far Right
]

# Function to draw a grid
def draw_grid(x, y, color, matrix):
    for i in range(grid_size):
        for j in range(grid_size):
            rect = pygame.Rect(x + j * block_size, y + i * block_size, block_size, block_size)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)
            font = pygame.font.Font(None, 20)
            text = font.render(matrix[i, j], True, BLACK)
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)


#testing rotate fntion
rotate_90deg(origin_mat=r, up_mat=w, down_mat=y, left_mat=g, right_mat=b, no_of_rotation=1)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(GRAY)
    
    for (x, y, color, matrix) in grids:
        draw_grid(x, y, color, matrix)
    
    pygame.display.flip()

pygame.quit()
