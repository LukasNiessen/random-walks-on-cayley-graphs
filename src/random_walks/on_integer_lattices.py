import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from typing import Tuple, List


def random_walk_step_1d(position: Tuple[int, int]) -> Tuple[int, int]:
    x, y = position
    x += 1
    direction = np.random.choice(["up", "down"])
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    return x, y


def random_walk_step_2d(position: Tuple[int, int]) -> Tuple[int, int]:
    x, y = position
    direction = np.random.choice(["up", "down", "left", "right"])
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    return x, y


def random_walk_step_3d(position: Tuple[int, int, int]) -> Tuple[int, int, int]:
    x, y, z = position
    direction = np.random.choice(["x+", "x-", "y+", "y-", "z+", "z-"])
    if direction == "x+":
        x += 1
    elif direction == "x-":
        x -= 1
    elif direction == "y+":
        y += 1
    elif direction == "y-":
        y -= 1
    elif direction == "z+":
        z += 1
    elif direction == "z-":
        z -= 1
    return x, y, z


def random_walk_1d(steps: int = 100) -> List[Tuple[int, int]]:
    path = [(0, 0)]
    for _ in range(steps):
        next_position = random_walk_step_1d(path[-1])
        path.append(next_position)
    return path


def random_walk_2d(steps: int = 100) -> List[Tuple[int, int]]:
    path = [(0, 0)]
    for _ in range(steps):
        next_position = random_walk_step_2d(path[-1])
        path.append(next_position)
    return path


def random_walk_3d(steps: int = 100) -> List[Tuple[int, int, int]]:
    path = [(0, 0, 0)]
    for _ in range(steps):
        next_position = random_walk_step_3d(path[-1])
        path.append(next_position)
    return path


def animate_walk_2d(path: List[Tuple[int, int]], interval: int = 50):
    # Convert path to numpy arrays for easier handling
    path = np.array(path)
    x_coords, y_coords = path[:, 0], path[:, 1]

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 8))

    # Set the plot limits with some padding
    padding = 2
    ax.set_xlim(min(x_coords) - padding, max(x_coords) + padding)
    ax.set_ylim(min(y_coords) - padding, max(y_coords) + padding)

    # Initialize empty line and point
    (line,) = ax.plot([], [], "b-", label="Path")
    (point,) = ax.plot([], [], "ro", markersize=10, label="Current Position")

    ax.grid(True)
    ax.legend()

    def init():
        line.set_data([], [])
        point.set_data([], [])
        return line, point

    def update(frame):
        # Update line data
        line.set_data(x_coords[: frame + 1], y_coords[: frame + 1])
        # Update point data
        point.set_data([x_coords[frame]], [y_coords[frame]])
        return line, point

    anim = FuncAnimation(
        fig=fig,
        func=update,
        frames=len(path),
        init_func=init,
        blit=True,
        interval=interval,
        repeat=False,
    )

    plt.show()


def animate_walk_3d(path: List[Tuple[int, int, int]], interval: int = 50):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection="3d")
    (line,) = ax.plot([], [], [], "b-", label="Path")
    (point,) = ax.plot([], [], [], "ro", markersize=10, label="Current Position")

    # Set the plot limits with some padding
    x_coords, y_coords, z_coords = zip(*path)
    padding = 2
    ax.set_xlim(min(x_coords) - padding, max(x_coords) + padding)
    ax.set_ylim(min(y_coords) - padding, max(y_coords) + padding)
    ax.set_zlim(min(z_coords) - padding, max(z_coords) + padding)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()

    def init():
        line.set_data([], [])
        line.set_3d_properties([])
        point.set_data([], [])
        point.set_3d_properties([])
        return line, point

    def animate(frame):
        # Plot the path up to the current frame
        x_data, y_data, z_data = zip(*path[: frame + 1])
        line.set_data(x_data, y_data)
        line.set_3d_properties(z_data)

        # Plot the current position
        point.set_data([path[frame][0]], [path[frame][1]])
        point.set_3d_properties([path[frame][2]])
        return line, point

    anim = FuncAnimation(
        fig,
        animate,
        init_func=init,
        frames=len(path),
        interval=interval,
        blit=True,
        repeat=False,
    )
    plt.show()


dim = 1
steps = 1000
anim_interval = 10

if dim == 1:
    path_1d = random_walk_1d(steps)
    animate_walk_2d(path_1d, interval=anim_interval)

elif dim == 2:
    path_2d = random_walk_2d(steps)
    animate_walk_2d(path_2d, interval=anim_interval)

else:
    path_3d = random_walk_3d(steps)
    animate_walk_3d(path_3d, interval=anim_interval)
