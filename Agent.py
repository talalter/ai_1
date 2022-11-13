import sys
from State import State
from action import NoOpAction, TraverseAction, TerminateAction

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = [node for node in graph.vertices if not node.get_is_broken()]
    shortest_path = {}
    previous_nodes = {} 
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0
    
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        neighbors = graph.graph_dict[current_min_node]
        for neighbor in neighbors:
            if not neighbor[0].get_is_broken():
                tentative_value = shortest_path[current_min_node] + neighbor[1]
                if tentative_value < shortest_path[neighbor[0]]:
                    shortest_path[neighbor[0]] = tentative_value
                    previous_nodes[neighbor[0]] = current_min_node
 
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

class Agent:
    def __init__(self, id_):
        self.seq = []
        self.state = None
        self.id_ = id_

    def update_state(self, state, percept):
        raise NotImplementedError

    def search(self):
        raise NotImplementedError

    def recommendation(self, seq, state):
        raise NotImplementedError

    def remainder(self, seq, state):
        ######################### need to add brokem vertix
        if (len(seq) == 0):
            return seq 
        else:
            return seq[1:]

    def run(self, percept):
        self.state = self.update_state(self.state, percept)
        if len(self.seq) == 0:
            self.seq = self.search()
        action = self.recommendation(self.seq, self.state)
        self.seq = self.remainder(self.seq, self.state)
        return action

class HumanAgent(Agent):
    def __init__(self, id_, start_vertex):
        super().__init__(id_)
        self.state = State(start_vertex)

    def update_state(self, state, percept):
        state.percept = percept
        state.current_vertex = percept.agent_locations[self.id_]
        if state.current_vertex.first_agent_id == self.id_:
            state.people_saved += current_vertex.people_saved
        if state.current_vertex != state.previous_vertex:
            dest_arr = percept.graph_dict[state.previous_vertex]
            found_vertex = False
            for tup in dest_arr:
                if (tup[0] == state.current_vertex):
                    state.time += tup[1]
                    found_vertex = True
                    break
            assert found_vertex
        else:
            state.time += 1
        self.score = (state.people_saved * 1000) - state.time
        return state

    def search(self):
        got_vertex = False
        while not got_vertex:
            user_input = input("Agent%d: please choose destination vertex:\n" % self.id_)
            selected_vertex_id = int(user_input)
            if selected_vertex_id >= self.state.percept.num_of_vertices:
                print("illegal vertex!\n")
            else:
                got_vertex = True
        target_vertex = self.state.percept.vertices[selected_vertex_id]
        connected_target_arr = self.state.percept.graph_dict[target_vertex]
        for tup in connected_target_arr:
            if tup[0] == self.state.current_vertex:
                action = TraverseAction(self.state, self.id_, target_vertex, True)
                return [action]
        action = NoOpAction(self.state)
        return [action]

    def recommendation(self, seq, state):
        action = seq[0]
        if (type(action) == TraverseAction) and action.to_vertex.get_is_broken():
            return NoOpAction(self.state)
        return action

class StuipedGreedyAgent(Agent):
    def __init__(self, id_, start_vertex):
        super().__init__(id_)
        self.state = State(start_vertex)

    def update_state(self, state, percept):
        state.percept = percept
        state.current_vertex = percept.agent_locations[self.id_]
        if state.current_vertex.first_agent_id == self.id_:
            state.people_saved += current_vertex.people_saved
        if state.current_vertex != state.previous_vertex:
            dest_arr = percept.graph_dict[state.previous_vertex]
            found_vertex = False
            for tup in dest_arr:
                if (tup[0] == state.current_vertex):
                    state.time += tup[1]
                    found_vertex = True
                    break
            assert found_vertex
        else:
            state.time += 1
        self.score = (state.people_saved * 1000) - state.time
        return state

    def search(self):
        min_score = sys.maxsize
        target_vertex = None
        path_dict, dist_dict = dijkstra_algorithm(self.state.percept, self.state.current_vertex)
        for vertex, score in dist_dict.items():
            if (vertex.people) and (score > 0):
                if (score < min_score) or ((score == min_score) and (vertex.id_ < target_vertex.id_)):
                    min_score = score
                    target_vertex = vertex

        if target_vertex is None:
            return [TerminateAction()]

        seq = []
        next_vertex = target_vertex
        while next_vertex != self.state.current_vertex:
                next_vertex = path_dict[next_vertex]
                seq.insert(0, TraverseAction(self.state, self.id_, next_vertex, True))
        return seq

    def recommendation(self, seq, state):
        action = seq[0]
        if (type(action) == TraverseAction) and action.to_vertex.get_is_broken():
            return NoOpAction(self.state)
        return action

#    def search(self):
#        got_vertex = False
#        while not got_vertex:
#            user_input = input("Agent%d: please choose destination vertex:\n" % self.id_)
#            selected_vertex_id = int(user_input)
#            if selected_vertex_id >= self.state.percept.num_of_vertices:
#                print("illegal vertex!\n")
#            else:
#                got_vertex = True
#        path_dict, _ = dijkstra_algorithm(self.state.percept, self.state.current_vertex)
#        selected_vertex = self.state.percept.vertices[selected_vertex_id]
#        if selected_vertex not in path_dict:
#            action_params = {"state" : self.state}
#            action = NoOpAction(action_params)
#            return [action]
#        else:
#            seq = []
#            next_vertext = selected_vertex
#            while next_vertext != self.state.current_vertex:
#                next_vertext = path_dict[next_vertext]
#                seq.insert(0, TraverseAction(self.state, self.id_, next_vertext))
#            return seq