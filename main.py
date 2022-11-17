from Agent import HumanAgent, StupidGreedyAgent, SaboteurAgent
from Graph import Graph


def ask_for_agents(graph): ############## TODO
    how_many_agents = (int(input("Insert how many agent you want\n")))
    agents_list = []
    for i in range(how_many_agents):
        agent_type = (int(input("Insert the type of the agent\n1 for human\n2 for greedy\n3 for saboteur\n\n")))
        start_vertex = (int(input("insert the starting vertex from 0-3\n\n")))
        assert agent_type == 1 or 2 or 3
        assert start_vertex == 0 or 1 or 2 or 3
        if agent_type == 1:
            agent_ = HumanAgent(i)
        elif agent_type == 2:
            agent_ = StupidGreedyAgent(i)
        else:  # agent_type == "3"
            agent_ = SaboteurAgent(i)
        agents_list.append(agent_)
        graph.agent_locations[agent_] = graph.vertices[start_vertex]
    return agents_list


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
    agents = ask_for_agents(graph)
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