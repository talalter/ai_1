from Agent import HumanAgent, StupidGreedyAgent, SaboteurAgent
from Graph import Graph
from action import *


def ask_for_agents(graph):
    how_many_agents = (int(input("Insert how many agent you want\n")))
    for i in range(how_many_agents):
        agent_type, = (int(input(f"Insert the type of the {i+1} agent\n1 for human\n2 for greedy\n3 for saboteur\n\n")))
        start_vertex = (int(input("insert the starting vertex from 0-4\n\n")))
        if agent_type == "1":
            agents.append(HumanAgent(i))
        if agent_type == "2":
            agents.append(StupidGreedyAgent(i))
        if agent_type == "3":
            agents.append(SaboteurAgent(i))
    return agents


if __name__ == "__main__":
    config_ = '''
#N 4      
#V1                  
#V2 P1 B             
#V3 B                
#V4 P2               

#E1 1 2 W1                 
#E2 3 4 W1                 
#E3 2 3 W1                 
#E4 1 3 W4                 
#E5 2 4 W5                 
'''
    graph = Graph(config_)
    agents = [HumanAgent(0), StupidGreedyAgent(1)]
    for agent in agents:
        graph.agent_locations[agent] = graph.vertices[0]
    #agents = ask_for_agents(agents,graph)
    print(graph.agent_locations)
    i = 0
    while agents:
        for agent in agents:
            print("its "+type(agent).__name__+" %d turn %d\n" % (agent.id_, i))
            action = agent(graph)
            if action():
                agents.remove(agent)
                print(type(agent).__name__ +" %d has been removed\n" % agent.id_)
        i+=1
    print("simulation over\n")