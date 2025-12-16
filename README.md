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

<img width="2047" height="1199" alt="Screenshot 2025-12-16 151149" src="https://github.com/user-attachments/assets/0c1e2a1e-f0f8-42b4-89e5-7ff68071bdfc" />

Editable Grid

<img width="2049" height="1198" alt="Screenshot 2025-12-16 151803" src="https://github.com/user-attachments/assets/2f55c27d-10ad-49db-8c53-498bdff343c4" />

Loading Screen

<img width="2049" height="1199" alt="Screenshot 2025-12-16 151248" src="https://github.com/user-attachments/assets/e1c3a224-ea60-4937-a17f-5396197dd8c1" />

Puzzle Solver

<img width="2046" height="1199" alt="image" src="https://github.com/user-attachments/assets/e7dd3232-3113-4418-89b3-470f708bc13e" />

Error Popup

<img width="2048" height="1199" alt="Screenshot 2025-12-16 152041" src="https://github.com/user-attachments/assets/a1db2efb-0870-40bb-b14f-e2bbd3707b68" />

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
- Set Start/Finish — place two green tiles that indicates start and finish
- Add Obstacle — place red tiles that indicates obstacle(s)
- Undo/Redo — revert or redo actions
- Solve — run the DFS solver
- Reset — resetting the grid to initial state

If the solver finds a valid path, it is visualized automatically.

---

## 🧩 Grid Format

Grid uses:
- Grey Square → empty
- Red Square → obstacle
- Green Square → start/finish

The solver tries to visit all Grey Square and Green Square exactly once.

---

## 👤 Author

Developed by Shab (Shabrina Amalia Safaana - 5025241157) and Neb (Nabila Shafa Rahayu - 5025241150) for the Artificial Intelligence Concepts course final project.
