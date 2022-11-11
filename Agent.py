from State import State


class Agent:

    def __init__(self, id_, init_vertex_string, world):
        self.moves = 0
        self.score = 0
        self.people_saved = 0
        self.id_ = id_
        self.terminated = False
        self.world = world
        self.current_node, self.current_state = self.build_next_state(init_vertex_string, world)

    def build_next_state(self, init_vertex_string, world):

        for vertex in self.world.graph.keys():
            if init_vertex_string == vertex.id_:
                return vertex, State(vertex, world)

    def change_current_node(self, new_node):
        self.current_node = new_node

    def change_current_state(self, ):
        pass

    def update_score(self, score):
        self.score += score

    def run(self):
        pass

    # state = [where I am, where I need to go, how many steps left to goal]
    # update action (if there was changes on the graph so the agent should know to return back)
    # if state[1]==null (thats mean that the agent standing on a vertex):
    # search
    # do_action:
    # state[2]--
    # if state[2]==0:

    # state[0]=state[1]
    # state[1]=state[0]

    def update_state(self, vertex):
        self.current_state.update_state(vertex, self.world)

    def search(self):
        pass

    #         self.current_vertex = current_vertex
    #         self.dest_vertex = None
    #         self.steps_left = 0

    def do_action(self):
        pass


class HumanAgent(Agent):

    def __init__(self, id_, init_vertex, world):
        super().__init__(id_, init_vertex, world)

    def run(self):
        while not self.terminated:
            print(self.current_state)
            wrong_choice = True
            all_neighborhood = ""
            for neighborhood in self.world.graph[self.current_node]:
                all_neighborhood += str(neighborhood[0].id_) + "   "
            while wrong_choice:
                user_input = input(f"pick a node from the following list: {all_neighborhood}")
                if self.world.list_of_only_vertices[int(user_input)].is_broken or user_input not in all_neighborhood:
                    print("please select different Node")
                else:
                    wrong_choice = False
            self.moves += 1
            self.current_node = self.world.list_of_only_vertices[int(user_input)]
            self.current_node.peoples = 0
            if self.current_node.is_brittle:
                self.current_node.is_broken = True
            self.current_state.update_state(self.current_node, self.world)
            print(self.current_state)
            if self.current_state.check_goal():
                self.terminated = True
                print ("ALL THE PEOPLES EVACUATED")
                break
            user_input_for_terminate = input("Press T if you wish to terminate")
            if user_input_for_terminate == "T":
                self.terminated = True

