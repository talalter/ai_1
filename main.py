from Agent import HumanAgent
from Graph import Graph



def ask_for_agents():

    agents = []
    how_many_agents = (int(input("Insert how many agent you want")))
    for i in range(how_many_agents):
        agent_type, start_vertex = input(f"Insert the type of the {i+1} agent\n1 for human\n2 for greedy\n\nInsert the starting vertex")
        if(agent_type=="1"):
            agents.append(HumanAgent(i), start_vertex, )

class Environment:

    def __init__ (self, world):
        self.world = world






if __name__ == "__main__":
    config_ = '''
#N 4      
#V1                  
#V2 P12 B             
#V3 B                
#V4 P2               

#E1 1 2 W1                 
#E2 3 4 W1                 
#E3 2 3 W1                 
#E4 1 3 W4                 
#E5 2 4 W5                 
'''
    graph = Graph(config_)
    print(graph, "\n\n\n")
    agent = HumanAgent(1, 2, graph)
    agent.run()
