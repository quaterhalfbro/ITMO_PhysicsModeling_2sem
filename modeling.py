import matplotlib.pyplot as plt
from objects import Body
from matplotlib.animation import FuncAnimation


def frame(time):
    ax.clear()
    for body in bodies:
        body()
    return [ax.plot(*body.get_history()) for body in bodies]


if __name__ == "__main__":
    fig, ax = plt.subplots()
    bodies = [Body(1, 0.1) for i in range(3)]
    bodies[0].push(10, 10)
    bodies[1].push(13.25, 5)
    bodies[2].push(5, 13.25)
    anime = FuncAnimation(fig, frame, frames=100, interval=10, repeat=True)
    plt.show()
