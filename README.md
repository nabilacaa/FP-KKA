  # FP-KKA

## CONNECT THE DOTS PUZZLE SOLVER  
A path-finding puzzle solver built with **Python + Pygame**, implementing **uninformed search (DFS)** with a **degree heuristic** to efficiently find a single continuous path connecting two points without revisiting any cell.

---

## 📌 Project Description
This project is developed as the final assignment for the **Artificial Intelligence Concepts** course.  
It simulates a grid-based puzzle where the goal is to connect **Start** and **Finish** in *one continuous line* that visits every free cell exactly once while avoiding obstacles.

The program includes:
- Interactive grid editor  
- Start/Finish placement  
- Obstacle placement  
- Undo/Redo  
- Solver using DFS  
- Visual path rendering with Pygame  

---

## 🧠 Algorithm Used
This application uses **Depth-First Search (DFS)** as its primary search algorithm.

### Why DFS?
- Effective for exploring large search spaces  
- Ideal for Hamiltonian-path-like puzzles  
- Simple recursive implementation  

### Optimizations Included
- **Degree Heuristic**  
  Expands nodes with the fewest available moves first to reduce backtracking.

- **Pruning**  
  Stops as soon as a valid solution is discovered.

- **State Snapshots (Undo/Redo)**  
  The app stores complete grid states to allow safe undo/redo actions.

---

## 🎮 Features
- 🧱 **Interactive Grid Editor**
  - Set number of rows, columns, and obstacles  
  - Click to place Start/Finish  
  - Click to place obstacles  

- ↩️ **Undo, Redo, & Reset Functionality**

- 🧠 **Automatic Solver**
  - DFS with heuristics  
  - Visualized path drawing  

- ⚠️ **Error Popup**
  - Displays a message when no solution exists  

- 🎨 **Pygame-based UI**

---

## 📸 Preview

Home

<img width="2045" height="1195" alt="Screenshot 2025-12-16 164108" src="https://github.com/user-attachments/assets/755fd014-945d-4c3b-9360-7196f4f6d404" />

Editable Grid

<img width="2047" height="1196" alt="Screenshot 2025-12-16 164209" src="https://github.com/user-attachments/assets/88050704-f5e5-444d-b346-756784a2ba9f" />

Loading Screen

<img width="2046" height="1197" alt="Screenshot 2025-12-16 164232" src="https://github.com/user-attachments/assets/aa0df1a7-7b31-4048-974d-4c8ebaff4cc4" />

Puzzle Solver

<img width="2046" height="1198" alt="Screenshot 2025-12-16 164305" src="https://github.com/user-attachments/assets/aa3f514a-b2fd-4f88-904c-cd21fdc2c9b9" />

Error Popup

<img width="2045" height="1192" alt="Screenshot 2025-12-16 164249" src="https://github.com/user-attachments/assets/deb77619-460f-45c9-bacb-90968f49a024" />

---

## 🛠️ Installation

Clone the repository:

```
git clone https://github.com/Shabrinashsf/single-line-fill-puzzle-solver
cd single-line-fill-puzzle-solver
```

Install dependencies:

```
pip install pygame
```

Run the program:

```
python main.py
```

---

## 📌 How to Use

1. Start Menu
Enter:
- Number of Rows
- Number of Columns

2. Editor Mode
Tools available:

- Home — back to start menu
- Set Start/Finish — place two dots tiles that indicates start and finish
- Add Obstacle — place stone(s) that indicates obstacle(s)
- Undo/Redo — revert or redo actions
- Solve — run the DFS solver
- Reset — resetting the grid to initial state

If the solver finds a valid path, it is visualized automatically.

---

## 🧩 Grid Format

Grid uses:
- Plain Green Square → empty
- Square with Stone(s) → obstacle
- Square with Blue Dot → start/finish

The solver tries to visit all Grey Square and Green Square exactly once.

---

## 👤 Author

Developed by Shab (Shabrina Amalia Safaana - 5025241157) and Neb (Nabila Shafa Rahayu - 5025241150) for the Artificial Intelligence Concepts course final project.
