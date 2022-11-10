from Agent import HumanAgent
from Graph import Graph



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
    print(graph)
    agent = HumanAgent(1, 2, graph)
    agent.run()
