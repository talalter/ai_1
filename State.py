class State:

    def __init__(self, current_vertex, world):
        self.peoples = [vertex[1] for vertex in world.vertices]
        self.broken_vertices = [vertex.is_broken for vertex in world.list_of_only_vertices]
        self.current_vertex = current_vertex

    def __str__(self):
        print(self.peoples)
        print(self.broken_vertices)
        return ""

    def check_goal(self):
        return 0 not in self.peoples

    def update_state(self, current_vertex, world):
        self.peoples = [vertex.peoples for vertex in world.list_of_only_vertices]
        self.broken_vertices = [vertex.is_broken for vertex in world.list_of_only_vertices]
        self.current_vertex = current_vertex

    def __str__(self):
        res = f"Current vertex: {self.current_vertex} \n"
        for index in range(len(self.peoples)):
            res += f"At vertex {index} there are {self.peoples[index]} peoples and "
            if self.broken_vertices[index]:
                res += "is broken\n"
            else:
                res += "isn't broken\n"
        return res