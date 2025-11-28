# pakai number

import pygame
import sys
sys.setrecursionlimit(10**7)

pygame.init()

# =============================
# GLOBAL SETTINGS
# =============================
WIDTH, HEIGHT = 1000, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DFS Path Puzzle")

FONT = pygame.font.SysFont("arial", 24)
SMALL = pygame.font.SysFont("arial", 20)

COLOR_BG = (25, 25, 25)
COLOR_BOX = (50, 50, 50)
COLOR_ACTIVE = (80, 80, 200)
COLOR_TEXT = (240, 240, 240)

COLOR_BTN = (70, 170, 70)
COLOR_BTN2 = (170, 70, 70)
COLOR_GRID = (180, 180, 180)
COLOR_OBS = (220, 50, 50)
COLOR_START_FIN = (0, 255, 0)
COLOR_EMPTY = (200, 200, 200)
COLOR_NUM = (0, 120, 255)

# =============================
# TEXTBOX CLASS
# =============================
class TextBox:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_BOX
        self.text = ""
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = COLOR_ACTIVE if self.active else COLOR_BOX

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.unicode.isdigit():
                self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=4)
        txt_surface = FONT.render(self.text, True, COLOR_TEXT)
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))


# =============================
# MENU AWAL
# =============================
def draw_label(text, x, y):
    img = FONT.render(text, True, COLOR_TEXT)
    SCREEN.blit(img, (x, y))


def start_menu():
    row_box = TextBox(350, 180, 200, 40)
    col_box = TextBox(350, 260, 200, 40)
    obs_box = TextBox(350, 340, 200, 40)

    start_button = pygame.Rect(350, 440, 200, 50)

    while True:
        SCREEN.fill(COLOR_BG)

        draw_label("Rows:", 250, 185)
        draw_label("Columns:", 250, 265)
        draw_label("Obstacles:", 250, 345)

        row_box.draw(SCREEN)
        col_box.draw(SCREEN)
        obs_box.draw(SCREEN)

        pygame.draw.rect(SCREEN, COLOR_BTN, start_button, border_radius=6)
        SCREEN.blit(FONT.render("START", True, (255,255,255)),
                    (start_button.x+60, start_button.y+10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            row_box.handle_event(event)
            col_box.handle_event(event)
            obs_box.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    if row_box.text and col_box.text and obs_box.text:
                        return int(row_box.text), int(col_box.text), int(obs_box.text)

        pygame.display.update()


# =============================
# DFS SOLVER
# =============================
def find_points(g):
    pts = []
    R, C = len(g), len(g[0])
    for r in range(R):
        for c in range(C):
            if g[r][c] == "A":
                pts.append((r,c))
    if len(pts) != 2:
        return None, None
    return pts[0], pts[1]


def dfs_solver(grid):
    R, C = len(grid), len(grid[0])
    start, finish = find_points(grid)
    if not start or not finish:
        return None

    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    target_cells = [(r,c) for r in range(R) for c in range(C)
                    if grid[r][c] in ("0","A")]
    need = len(target_cells)

    visited = set()
    path = []
    solution = None

    def degree(r,c):
        cnt = 0
        for dr,dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C:
                if grid[nr][nc] != "X" and (nr,nc) not in visited:
                    cnt += 1
        return cnt

    def dfs(r,c):
        nonlocal solution
        if solution is not None:
            return

        if (r,c) == finish and len(path) == need:
            solution = path[:]
            return

        moves = []
        for dr,dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C:
                if grid[nr][nc] != "X" and (nr,nc) not in visited:
                    moves.append((degree(nr,nc), nr, nc))

        moves.sort()

        for _, nr, nc in moves:
            visited.add((nr,nc))
            path.append((nr,nc))

            dfs(nr,nc)

            path.pop()
            visited.remove((nr,nc))

    visited.add(start)
    path.append(start)
    dfs(*start)

    return solution


# =============================
# DRAWING
# =============================
def draw_grid(rows, cols, cs, grid):
    for r in range(rows):
        for c in range(cols):
            rect = pygame.Rect(c*cs, r*cs, cs, cs)

            if grid[r][c] == "X":
                pygame.draw.rect(SCREEN, COLOR_OBS, rect)
            elif grid[r][c] == "A":
                pygame.draw.rect(SCREEN, COLOR_START_FIN, rect)
            else:
                pygame.draw.rect(SCREEN, COLOR_EMPTY, rect)

            pygame.draw.rect(SCREEN, COLOR_GRID, rect, 1)


# =============================
#  🔥 NEW: DRAW NUMBERS 🔥
# =============================
def draw_numbers(path, cs):
    num = 1
    for (r, c) in path:
        # skip A (start / finish)
        rect_x = c * cs
        rect_y = r * cs

        img = SMALL.render(str(num), True, COLOR_NUM)
        SCREEN.blit(img, (rect_x + cs//2 - img.get_width()//2,
                          rect_y + cs//2 - img.get_height()//2))
        num += 1


# =============================
# MAIN GRID EDITOR
# =============================
def main_editor(rows, cols, max_obs):
    grid = [["0" for _ in range(cols)] for _ in range(rows)]
    cs = min(600//rows, 600//cols)

    mode = "none"
    obs_count = 0
    start = None
    finish = None

    undo = []
    redo = []

    buttons = {
        "set_sf": pygame.Rect(650, 50, 200, 45),
        "set_obs": pygame.Rect(650, 110, 200, 45),
        "undo": pygame.Rect(650, 170, 95, 45),
        "redo": pygame.Rect(755, 170, 95, 45),
        "solve": pygame.Rect(650, 230, 200, 45)
    }

    home_btn = pygame.Rect(650, 50, 200, 45)
    path = None
    solved = False

    while True:
        SCREEN.fill(COLOR_BG)

        draw_grid(rows, cols, cs, grid)

        if solved and path:
            draw_numbers(path, cs)

        if solved:
            pygame.draw.rect(SCREEN, COLOR_BTN2, home_btn, border_radius=8)
            SCREEN.blit(FONT.render("HOME", True, (255,255,255)),
                        (home_btn.x+70, home_btn.y+10))

        else:
            for name, rect in buttons.items():
                pygame.draw.rect(SCREEN, COLOR_BTN, rect, border_radius=6)
                SCREEN.blit(FONT.render(name.replace("_"," ").upper(),
                        True,(255,255,255)), (rect.x+10, rect.y+10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if solved:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if home_btn.collidepoint(event.pos):
                        return
                continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos

                if x < cols*cs and y < rows*cs:
                    r = y // cs
                    c = x // cs

                    prev = [row[:] for row in grid]
                    undo.append(prev)
                    redo.clear()

                    if mode == "set_sf":
                        if not start:
                            start = (r,c)
                            grid[r][c] = "A"
                        elif not finish and (r,c) != start:
                            finish = (r,c)
                            grid[r][c] = "A"

                    elif mode == "set_obs":
                        if grid[r][c] == "0" and obs_count < max_obs:
                            grid[r][c] = "X"
                            obs_count += 1

                else:
                    for name, rect in buttons.items():
                        if rect.collidepoint(event.pos):
                            if name == "set_sf":
                                mode = "set_sf"
                            elif name == "set_obs":
                                mode = "set_obs"
                            elif name == "undo":
                                if undo:
                                    redo.append([row[:] for row in grid])
                                    grid = undo.pop()
                            elif name == "redo":
                                if redo:
                                    undo.append([row[:] for row in grid])
                                    grid = redo.pop()
                            elif name == "solve":
                                if start and finish:
                                    path = dfs_solver(grid)
                                    solved = True

        pygame.display.update()


# =============================
# MAIN
# =============================
def main():
    while True:
        r, c, o = start_menu()
        main_editor(r, c, o)


if __name__ == "__main__":
    main()
