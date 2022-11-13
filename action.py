
class Action:
    def __call__(self):
        raise NotImplementedError

    def __repr__(self):
        return self.__class__.__name__

class TraverseAction(Action):
    def __init__(self, state, agent_id, to_vertex, pickup):
        self.state = state
        self.to_vertex = to_vertex
        self.agent_id = agent_id
        self.pickup = pickup

    def __call__(self):
        percept = self.state.percept
        if self.to_vertex.get_is_broken():
            state.time += 1
        else:
            if self.to_vertex.people and self.pickup:
                self.to_vertex.people_saved = self.to_vertex.people
                self.to_vertex.people = 0
            if (self.to_vertex.first_agent_id is None) and self.pickup:
                self.to_vertex.first_agent_id = self.agent_id
            if self.to_vertex.get_is_brittle():
                self.to_vertex.is_broken = True

        return False

class NoOpAction(Action):
    def __init__(self, state):
        self.state= state

    def __call__(self):
        self.state.time += 1
        return False

class TerminateAction(Action):
    def __call__(self):
        return True
    