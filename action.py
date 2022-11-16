class Action:
    def __init__(self, agent):
        self.target_vertex = agent.state.current_vertex
        self.agent = agent
        self.graph = agent.state.percept

    def __call__(self):
        raise NotImplementedError

    def __repr__(self):
        return self.__class__.__name__

    def the_move(self):
        self.graph.change_agent_location(self.agent, self.target_vertex)
        if type(self.agent).__name__ != "SaboteurAgent":  ###isinstance(self.agent, SaboteurAgent)
            self.agent.state.people_saved += self.target_vertex.people
            self.target_vertex.people = 0
        if self.target_vertex.is_brittle:
            self.target_vertex.is_broken = True


class TraverseAction(Action):
    def __init__(self, agent, target_vertex):
        self.target_vertex = target_vertex
        self.agent = agent
        self.graph = agent.state.percept

    def __call__(self):
        if self.graph.agent_locations[self.agent] == self.target_vertex:
            raise Exception("this is is traverse action why is it moving to itself?")
        linked_vertexes = [x for x in self.graph.graph_dict[self.agent.state.current_vertex] if x[0] == self.target_vertex]
        assert len(linked_vertexes) == 1
        self.agent.state.time += linked_vertexes[0][1]
        self.the_move()
        return False

class NoOpAction(Action):
    def __init__(self, agent):
        super().__init__(agent)

    def __call__(self):
        self.agent.state.time += 1
        self.the_move()
        return False

class TerminateAction(Action):
    def __init__(self, agent):
        super().__init__(agent)

    def __call__(self):
        return True
    