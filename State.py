class State:
    def __init__(self, current_vertex):
        self.precept = None
        self.score = 0
        self.time = 0
        self.people_saved = 0
        self.previous_vertex = current_vertex
        self.current_vertex = current_vertex

    def __str__(self):
        return ""
