G = 9.8
INF = 10 ** 20
FPS = 100


class Point(object):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def copy(self):
        return Point(self.x, self.y)

    def __str__(self):
        return str(self.x) + " " + str(self.y)

    def to(self, other) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


class Vector(Point):
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __truediv__(self, const: float):
        if const == 0:
            return Vector(INF, INF)
        return Vector(self.x / const, self.y / const)

    def __mul__(self, const: float):
        return Vector(self.x * const, self.y * const)


class Body(object):
    def __init__(self, m: float):
        self.m = m
        self.a = Vector(0, 0)
        self.coords = Point(0, 0)
        self.forces = {"F тяжести": Vector(0, -G * self.m)}
        self.v = Vector(0, 0)
        self.history = {0: self.coords.copy()}
        self.update_a()
        self.flying = True
        self.cur_time = 0

    def update_a(self):
        total_f = Vector(0, 0)
        for i in self.forces.keys():
            total_f = total_f + self.forces[i]
        self.a = total_f / self.m

    def __call__(self, delta_time: float = 1 / FPS) -> Point:
        if not self.is_flying():
            return self.coords
        self.coords += self.v * delta_time
        self.v += self.a * delta_time
        self.cur_time += delta_time
        self.history[self.cur_time] = self.coords.copy()
        if self.coords.y <= 0:
            self.flying = False
        return self.coords

    def is_flying(self):
        return self.flying

    def get_history(self):
        x_coords = []
        y_coords = []
        for i in self.history.keys():
            x_coords.append(self.history[i].x)
            y_coords.append(self.history[i].y)
        return x_coords, y_coords

    def push(self, new_x, new_y):
        self.v = Vector(new_x, new_y)