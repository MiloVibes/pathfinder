# Caveman Survival Pathfinding Visualizer

Caveman Survival is a pathfinding visualizer built using Pygame. It visualizes the A* pathfinding algorithm, showcasing how it finds the shortest path between two points while avoiding obstacles. The theme centers around a caveman navigating through a landscape filled with dinosaurs to reach a designated safe point.

## Features

- **Visualize A* Algorithm**: See step-by-step how the A* algorithm searches for the shortest path.
- **Interactive Grid**: Create start and end points, and place barriers in the form of dinosaurs on the grid.
- **Reset and Recreate**: Easily reset the grid or start a new pathfinding visualization.

## Installation

To run Caveman Survival on your machine, follow these steps:

### Prerequisites

Ensure you have Python installed on your system. This project was developed with Python 3.8, but it should be compatible with Python 3.6+.

You'll also need Pygame installed. If you don't have Pygame, it can be installed via pip:

```bash
pip install pygame
```

### Downloading the Project

Clone the repository to your local machine:

```bash
git clone https://github.com/MiloVibes/pathfinder.git
cd pathfinder
```

### Running the Application

Navigate to the project directory and run the main script:

```bash
python main.py
```

## How to Use

1. **Set Start and End Points**: Double click on a grid square to set the start point (Cave), and double click again somewhere else on screen to set the end point (caveman).
2. **Create Barriers**: Can double click on space to put one barrier or double click and drag to place multiple barriers (Dinosaurs) on the grid. These represent obstacles the caveman must navigate around.
3. **Start Pathfinding**: Press the spacebar to begin the visualization. The algorithm will start, and the path will be displayed once found.
4. **Reset**: Right-click to remove individual barriers (does not work a the moment), start, or end points. Press `R` to reset the entire grid, or `C` to clear and start over.

## Algorithm Used

The project utilizes the **A* Pathfinding Algorithm**, renowned for its efficiency and accuracy in finding the shortest path between two points. A* combines features of Dijkstra's Algorithm (favoring vertices that are close to the starting point) and Greedy Best-First-Search (favoring vertices that are close to the goal). This makes A* both fast and guaranteed to find the shortest path if one exists.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.

---
