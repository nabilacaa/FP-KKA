# =============================
# Made by Shab and Neb
# =============================

import pygame
import sys
sys.setrecursionlimit(10**7)

pygame.init()

# =============================
# GLOBAL SETTINGS
# =============================
WIDTH, HEIGHT = 1366, 768
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SINGLE-LINE FILL PUZZLE SOLVER")

FONT = pygame.font.SysFont("arial", 24)
SMALL = pygame.font.SysFont("arial", 20)

BG_HOME = pygame.image.load("image/bg_home.png")
BG_HOME = pygame.transform.scale(BG_HOME, (WIDTH, HEIGHT))

BG_GRID = pygame.image.load("image/bg_puzzle.png")
BG_GRID = pygame.transform.scale(BG_GRID, (WIDTH, HEIGHT))

IMG_BTN_CREATE = pygame.image.load("image/btn_create.png")

IMG_ROWS= pygame.image.load("image/text_rows.png")
IMG_COLS = pygame.image.load("image/text_columns.png")
IMG_OBS = pygame.image.load("image/text_obs.png")

IMG_HOME = pygame.image.load("image/btn_home.png")
IMG_SETSF = pygame.image.load("image/btn_setsf.png")
IMG_SETOBS = pygame.image.load("image/btn_setobs.png")
IMG_UNDO = pygame.image.load("image/btn_undo.png")
IMG_REDO = pygame.image.load("image/btn_redo.png")
IMG_SOLVE = pygame.image.load("image/btn_solve.png")
IMG_RESET = pygame.image.load("image/btn_reset.png")

BTN_W, BTN_H = 220, 37
def scale(img):
    return pygame.transform.scale(img, (BTN_W, BTN_H))

IMG_HOME = scale(IMG_HOME)
IMG_SETSF = scale(IMG_SETSF)
IMG_SETOBS = scale(IMG_SETOBS)
IMG_SOLVE = scale(IMG_SOLVE)
IMG_RESET = scale(IMG_RESET)

UNDO_W, UNDO_H = 106, 37
IMG_UNDO = pygame.transform.scale(IMG_UNDO, (UNDO_W, UNDO_H))
IMG_REDO = pygame.transform.scale(IMG_REDO, (UNDO_W, UNDO_H))

COLOR_BOX = (255, 255, 255)
COLOR_ACTIVE = (180, 220, 255)
COLOR_TEXT = (0, 0, 0)

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
# CREATE MENU
# =============================
def start_menu():
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    row_box = TextBox(center_x - 100, center_y - 50, 200, 40)
    col_box = TextBox(center_x - 100, center_y + 50, 200, 40)
    obs_box = TextBox(center_x - 100, center_y + 150, 200, 40)

    create_button_rect = pygame.Rect(center_x - 55, center_y + 220, 200, 60)

    while True:
        SCREEN.blit(BG_HOME, (0, 0))

        row_box.draw(SCREEN)
        col_box.draw(SCREEN)
        obs_box.draw(SCREEN)

        SCREEN.blit(IMG_ROWS, (center_x - IMG_ROWS.get_width() // 2, 310))
        SCREEN.blit(IMG_COLS, (center_x - IMG_COLS.get_width() // 2, 410))
        SCREEN.blit(IMG_OBS, (center_x - IMG_OBS.get_width() // 2, 510))

        SCREEN.blit(IMG_BTN_CREATE, (create_button_rect.x, create_button_rect.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            row_box.handle_event(event)
            col_box.handle_event(event)
            obs_box.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button_rect.collidepoint(event.pos):
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
def draw_grid(rows, cols, cs, grid, ox, oy):
    for r in range(rows):
        for c in range(cols):
            rect = pygame.Rect(c*cs + ox, r*cs + oy, cs, cs)

            if grid[r][c] == "X":
                pygame.draw.rect(SCREEN, COLOR_OBS, rect)
            elif grid[r][c] == "A":
                pygame.draw.rect(SCREEN, COLOR_START_FIN, rect)
            else:
                pygame.draw.rect(SCREEN, COLOR_EMPTY, rect)

            pygame.draw.rect(SCREEN, COLOR_GRID, rect, 1)


# =============================
# DRAW PATH
# =============================
def draw_path(path, cs, ox, oy):
    if not path or len(path) < 2:
        return

    points = []

    (r0, c0) = path[0]
    (r1, c1) = path[1]

    x0 = c0 * cs + cs // 2 + ox
    y0 = r0 * cs + cs // 2 + oy

    dx = c1 - c0
    dy = r1 - r0

    x0 += dx * (cs // 2 - 2)
    y0 += dy * (cs // 2 - 2)

    points.append((x0, y0))

    for (r, c) in path[1:-1]:
        cx = c * cs + cs // 2 + ox
        cy = r * cs + cs // 2 + oy
        points.append((cx, cy))

    (rf, cf) = path[-1]
    (r_prev, c_prev) = path[-2]

    xf = cf * cs + cs // 2 + ox
    yf = rf * cs + cs // 2 + oy

    dx = c_prev - cf
    dy = r_prev - rf

    xf += dx * (cs // 2 - 2)
    yf += dy * (cs // 2 - 2)

    points.append((xf, yf))

    # Finally draw the path
    pygame.draw.lines(SCREEN, (0, 70, 255), False, points, 10)


# =============================
# ALERT IF NO SOLUTION
# =============================
def show_alert(message):
    popup_width, popup_height = 400, 200
    popup = pygame.Surface((popup_width, popup_height))

    ok_rect = pygame.Rect(
        popup_width//2 - 50,
        120,
        100,
        40
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos

                rel_x = mx - (WIDTH//2 - popup_width//2)
                rel_y = my - (HEIGHT//2 - popup_height//2)

                if ok_rect.collidepoint((rel_x, rel_y)):
                    running = False 

        popup.fill((40, 40, 40))
        pygame.draw.rect(popup, (200, 50, 50), (0, 0, popup_width, popup_height), 4)

        txt = FONT.render(message, True, (255,255,255))
        popup.blit(txt, (popup_width//2 - txt.get_width()//2, 50))

        pygame.draw.rect(popup, (100,200,100), ok_rect, border_radius=8)
        popup.blit(FONT.render("OK", True, (0,0,0)),
                   (ok_rect.x + 30, ok_rect.y + 5))

        SCREEN.blit(
            popup,
            (WIDTH//2 - popup_width//2,
             HEIGHT//2 - popup_height//2)
        )

        pygame.display.update()


# -----------------------
# HISTORY STATE HELPER (UNDO/REDO)
# -----------------------
def copy_grid(g):
    return [row[:] for row in g]

def make_snapshot(grid, start, finish, obs_count):
    return {
        "grid": copy_grid(grid),
        "start": None if start is None else (start[0], start[1]),
        "finish": None if finish is None else (finish[0], finish[1]),
        "obs": obs_count
    }

def restore_snapshot(snap):
    g = copy_grid(snap["grid"])
    s = None if snap["start"] is None else (snap["start"][0], snap["start"][1])
    f = None if snap["finish"] is None else (snap["finish"][0], snap["finish"][1])
    return g, s, f, snap["obs"]

# =============================
# MAIN GRID EDITOR
# =============================
def main_editor(rows, cols, max_obs):
    grid = [["0" for _ in range(cols)] for _ in range(rows)]

    MAX_GRID_W = 800
    cs = min(HEIGHT // rows, MAX_GRID_W // cols)

    grid_w = cols * cs
    grid_h = rows * cs

    grid_offset_x = 0
    grid_offset_y = (HEIGHT - grid_h) // 2    

    mode = "none"
    obs_count = 0
    start = None
    finish = None

    undo = []
    redo = []

    BTN_X = WIDTH - BTN_W - 100
    UNDO_X = WIDTH - (UNDO_W * 2) - 110  
    REDO_X = WIDTH - UNDO_W - 100

    buttons = {
        "home": pygame.Rect(BTN_X, 100, BTN_W, BTN_H),
        "set_sf": pygame.Rect(BTN_X, 240, BTN_W, BTN_H),
        "set_obs": pygame.Rect(BTN_X, 300, BTN_W, BTN_H),
        "undo": pygame.Rect(UNDO_X, 360, UNDO_W, UNDO_H),
        "redo": pygame.Rect(REDO_X, 360, UNDO_W, UNDO_H),
        "solve": pygame.Rect(BTN_X, 500, BTN_W, BTN_H),
        "reset": pygame.Rect(BTN_X, 560, BTN_W, BTN_H),
    }

    path = None
    solved = False

    while True:
        SCREEN.blit(BG_GRID, (0,0))

        draw_grid(rows, cols, cs, grid, grid_offset_x, grid_offset_y)

        SCREEN.blit(IMG_HOME, buttons["home"].topleft)
        SCREEN.blit(IMG_SETSF, buttons["set_sf"].topleft)
        SCREEN.blit(IMG_SETOBS, buttons["set_obs"].topleft)
        SCREEN.blit(IMG_UNDO, buttons["undo"].topleft)
        SCREEN.blit(IMG_REDO, buttons["redo"].topleft)
        SCREEN.blit(IMG_SOLVE, buttons["solve"].topleft)
        SCREEN.blit(IMG_RESET, buttons["reset"].topleft)

        if solved and path:
            draw_path(path, cs, grid_offset_x, grid_offset_y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos

                if (grid_offset_x <= x < grid_offset_x + grid_w and
                    grid_offset_y <= y < grid_offset_y + grid_h):
                    # compute r,c relative to grid
                    r = (y - grid_offset_y) // cs
                    c = (x - grid_offset_x) // cs

                    undo.append(make_snapshot(grid, start, finish, obs_count))
                    redo.clear()

                    if mode == "set_sf":
                        if not start and grid[r][c] == "0":
                            start = (r,c)
                            grid[r][c] = "A"
                        elif not finish and (r,c) != start and grid[r][c] == "0":
                            finish = (r,c)
                            grid[r][c] = "A"

                    elif mode == "set_obs":
                        if grid[r][c] == "0" and obs_count < max_obs:
                            grid[r][c] = "X"
                            obs_count += 1

                else:
                    for name, rect in buttons.items():
                        if rect.collidepoint(event.pos):
                            if name == "home":
                                return
                            elif name == "set_sf":
                                mode = "set_sf"
                            elif name == "set_obs":
                                mode = "set_obs"
                            elif name == "undo":
                                if undo:
                                    # push current state to redo, then restore last undo
                                    redo.append(make_snapshot(grid, start, finish, obs_count))
                                    snap = undo.pop()
                                    grid, start, finish, obs_count = restore_snapshot(snap)
                            elif name == "redo":
                                if redo:
                                    # push current state to undo, then restore next redo
                                    undo.append(make_snapshot(grid, start, finish, obs_count))
                                    snap = redo.pop()
                                    grid, start, finish, obs_count = restore_snapshot(snap)
                            elif name == "solve":
                                if start and finish:
                                    path = dfs_solver(grid)
                                    if path is None:
                                        show_alert("No solution found!")
                                    else:
                                        solved = True
                            elif name == "reset":
                                grid = [["0" for _ in range(cols)] for _ in range(rows)]
                                obs_count = 0
                                start = None
                                finish = None
                                path = None
                                solved = False
                                undo.clear()
                                redo.clear()

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
