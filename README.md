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

<img width="2060" height="1208" alt="image" src="https://github.com/user-attachments/assets/99408182-afd7-4f3c-978f-64bbe6a52ee2" />

Puzzle Solver

<img width="2049" height="1198" alt="image" src="https://github.com/user-attachments/assets/d6025ce6-e48f-47a0-b230-b87245eca4da" />

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
- Number of Obstacles

2. Editor Mode
Tools available:
 
- Set Start/Finish — place two green tiles that indicates start and finish
- Add Obstacle — place red tiles that indicates obstacle(s)
- Undo/Redo — revert or redo actions
- Solve — run the DFS solver
- Reset — resetting the grid to initial state

If the solver finds a valid path, it is visualized automatically.

---

## 🧩 Grid Format

Grid uses:
- "0" → empty
- "X" → obstacle
- "A" → start/finish
The solver tries to visit all "0" and "A" exactly once.

---

## 👤 Author

Developed by Shab and Neb for the Artificial Intelligence Concepts course final project.
