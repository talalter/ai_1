from Agent import HumanAgent, StupidGreedyAgent, SaboteurAgent, AStarAgent, GreedyAStarAgent, RealTimeAStarAgent
from Graph import Graph


def ask_for_agents(graph):
    how_many_agents = (int(input("Insert how many agent you want\n")))
    agents_list = []
    for i in range(how_many_agents):
        agent_type = (int(input(
            "Insert the type of the agent\n1 for human\n2 for greedy\n3 for saboteur\n4 for greedyAStar\n5 for AStar\n6 for RealTimeAStar\n\n")))
        start_vertex = (int(input("insert the starting vertex from 0-5\n\n")))
        assert agent_type == 1 or 2 or 3 or 4 or 5 or 6
        assert graph.num_of_vertices > start_vertex >= 0
        if agent_type == 1:
            agent = HumanAgent(i)
        elif agent_type == 2:
            agent = StupidGreedyAgent(i)
        elif agent_type == 3:
            agent = SaboteurAgent(i)
        elif agent_type == 4:
            agent = GreedyAStarAgent(i, (int(input("insert T for agent\n\n"))), (int(input("insert L for agent\n\n"))))
        elif agent_type == 5:
            agent = AStarAgent(i, (int(input("insert T for agent\n\n"))))
        elif agent_type == 6:
            agent = RealTimeAStarAgent(i, (int(input("insert T for agent\n\n"))), (int(input("insert L for agent\n\n"))))
        else:
            print("agent Type not recognized")
            continue
        agents_list.append(agent)
        graph.agent_locations[agent] = graph.vertices[start_vertex]
    return agents_list


def run_agents(graph, agents):
    i = 0
    while agents:
        for agent in agents:
            print("its " + type(agent).__name__ + " %d turn %d" % (agent.id_, i))
            action = agent(graph)
            if action():
                agents.remove(agent)
                print(type(
                    agent).__name__ + " %d has been removed with a score of %f saved %d with the time of %d\n" % (
                          agent.id_, ((agent.state.people_saved * 1000) - agent.state.time), agent.state.people_saved,
                          agent.state.time))
        i += 1
    print("simulation over\n")


if __name__ == "__main__":
    with open('input_graph.txt') as f:
        input_txt = f.read()
    graph = Graph(input_txt)
    agents = ask_for_agents(graph)
    run_agents(graph, agents)

    # graph = Graph(input_txt)
    # agent = AStarAgent(0)
    # graph.agent_locations[agent] = graph.vertices[0]
    # agents = [agent]
    # run_agents(graph, agents)
    #
    # graph = Graph(input_txt)
    # agent = AStarAgent(1, 0.000001)
    # graph.agent_locations[agent] = graph.vertices[0]
    # agents = [agent]
    # run_agents(graph, agents)
    #
    # graph = Graph(input_txt)
    # agent = AStarAgent(2, 0.01)
    # graph.agent_locations[agent] = graph.vertices[0]
    # agents = [agent]
    # run_agents(graph, agents)
    #
    # graph = Graph(input_txt)
    # agent = GreedyAStarAgent(0)
    # graph.agent_locations[agent] = graph.vertices[0]
    # agents = [agent]
    # run_agents(graph, agents)
    #
    # graph = Graph(input_txt)
    # agent = GreedyAStarAgent(1, 0.000001)
    # graph.agent_locations[agent] = graph.vertices[0]
    # agents = [agent]
    # run_agents(graph, agents)
    #
    # graph = Graph(input_txt)
    # agent = GreedyAStarAgent(2, 0.01)
    # graph.agent_locations[agent] = graph.vertices[0]
    # agents = [agent]
    # run_agents(graph, agents)
    #
    # graph = Graph(input_txt)
    # agent = RealTimeAStarAgent(0)
    # graph.agent_locations[agent] = graph.vertices[0]
    # agents = [agent]
    # run_agents(graph, agents)
    #
    # graph = Graph(input_txt)
    # agent = RealTimeAStarAgent(1, 0.000001)
    # graph.agent_locations[agent] = graph.vertices[0]
    # agents = [agent]
    # run_agents(graph, agents)
    #
    # graph = Graph(input_txt)
    # agent = RealTimeAStarAgent(2, 0.01)
    # graph.agent_locations[agent] = graph.vertices[0]
    # agents = [agent]
    # run_agents(graph, agents)
