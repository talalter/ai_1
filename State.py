class State:

    def __init__(self, current_vertex, world):
        self.peoples = [vertex[1] for vertex in world.vertices]
        self.broken_vertices = [False for _ in world.vertices]
        self.current_vertex = current_vertex

    def __str__(self):
        print(self.peoples)
        print(self.broken_vertices)
        return ""

    def check_goal(self):
        return 0 not in self.peoples

    def update_state(self, current_vertex, world):
        self.peoples = [vertex[1] for vertex in world.vertices]
        self.broken_vertices = [False for _ in world.vertices]
        self.current_vertex = current_vertex
