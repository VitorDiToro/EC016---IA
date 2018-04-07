'''
Adaptado de:
@author: Edielson - https://github.com/edielsonpf
'''

from SearchAlgorithms.greedy_search import greedy_search
import networkx as nx


try:
    import matplotlib.pyplot as plt
except:
    raise

def printPath(path,start):
    string=(start)
    for city in path:
        if city != start:
            string=(string+' -> '+city)
    print(string)
    
def plotGraph(G,option,position=None):
    """Plot a graph G with specific position.

    Parameters
    ----------
    G : NetworkX graph
    option : if 1, edges with weight greater then 0 are enlarged. The opposite happens for option equal to 0.
    position : nodes position 
    
    Returns
    -------
    position: nodes position generated during plot (or same positions if supplied).

    """
    if option == 1:
        elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] > 0]
        esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <= 0]
    else:
        elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <= 0]
        esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] > 0]
        
    
    if position == None:
        position=nx.spring_layout(G) # positions for all nodes
    
    # nodes
    nx.draw_networkx_nodes(G,position,node_size=500)
        
    # edges
    nx.draw_networkx_edges(G,position,edgelist=elarge,width=2)
    nx.draw_networkx_edges(G,position,edgelist=esmall,width=2,alpha=0.5,edge_color='b',style='dashed')
    
    # labels
    nx.draw_networkx_labels(G,position,font_size=20,font_family='sans-serif')
    
    plt.axis('off')
    #plt.savefig("weighted_graph.png") # save as png
    plt.show() # display
    
    return position


class FindPath(object): 
    '''
    classdocs
    '''

    def __init__(self, graph):
        '''
        Constructor
        '''
        self.problem = graph
        
    def ObjectiveTest(self, current, target): 
        """
        Return ``True`` if ``current`` state corresponds to the ``target`` state 
        """ 
        solution = False 
        if current == target:
            solution = True
        return  solution
 
    def ExpandSolution(self, current): 
        """Returns all possible states from ``current`` 
        """ 
        return  self.problem.neighbors(current)
    
    def Heuristic(self, target, current): 
        """
        Returns heuristic associated to ``current`` 
        """ 
        custo_linha_reta={('Santa Rita'       , 'Campinas'): 165,
                          ('Pouso Alegre'     , 'Campinas'): 137,
                          ('Congonhal'        , 'Campinas'): 135,
                          ('Cambui'           , 'Campinas'): 108,
                          ('Itapuiuna'        , 'Campinas'): 139,
                          ('Borda da Mata'    , 'Campinas'): 117,
                          ('Andradas'         , 'Campinas'): 106,
                          ('Jacutinga'        , 'Campinas'):  84,
                          ('Camanducaia'      , 'Campinas'):  97,
                          ('Esp Santo Pinhal' , 'Campinas'):  86,
                          ('Mogi Guacu'       , 'Campinas'):  64,
                          ('Itapira'          , 'Campinas'):  58,
                          ('Braganca Paulista', 'Campinas'):  54,
                          ('Mogi Mirim'       , 'Campinas'):  54,
                          ('Atibai'           , 'Campinas'):  57,
                          ('Campinas'         , 'Campinas'):   0}

        
        
        Heuristic = custo_linha_reta.get((current, target))
        #print("Custo Heristico: %d" % Heuristic)                
        return Heuristic
    
          
    
    
if __name__ == '__main__':
    
    nodes = ['Santa Rita',
             'Pouso Alegre',
             'Congonhal',
             'Cambui',
             'Itapuiuna',
             'Borda da Mata',
             'Andradas',
             'Jacutinga',
             'Camanducaia',
             'Esp Santo Pinhal',
             'Mogi Guacu',
             'Itapira',
             'Braganca Paulista',
             'Mogi Mirim',
             'Atibai',
             'Campinas']


    edges=[('Santa Rita'       , 'Pouso Alegre'     ), ('Pouso Alegre'     , 'Santa Rita'       ),
           ('Pouso Alegre'     , 'Cambui'           ), ('Cambui'           , 'Pouso Alegre'     ),
           ('Pouso Alegre'     , 'Borda da Mata'    ), ('Borda da Mata'    , 'Pouso Alegre'     ),
           ('Pouso Alegre'     , 'Congonhal'        ), ('Congonhal'        , 'Pouso Alegre'     ),
           ('Cambui'           , 'Camanducaia'      ), ('Camanducaia'      , 'Cambui'           ),
           ('Camanducaia'      , 'Braganca Paulista'), ('Braganca Paulista', 'Camanducaia'      ),
           ('Braganca Paulista', 'Atibai'           ), ('Atibai'           , 'Braganca Paulista'),
           ('Braganca Paulista', 'Itapira'          ), ('Itapira'          , 'Braganca Paulista'),
           ('Atibai'           , 'Campinas'         ), ('Campinas'         , 'Atibai'           ),
           ('Itapira'          , 'Campinas'         ), ('Campinas'         , 'Itapira'          ),
           ('Borda da Mata'    , 'Jacutinga'        ), ('Jacutinga'        , 'Borda da Mata'    ),
           ('Jacutinga'        , 'Itapira'          ), ('Itapira'          , 'Jacutinga'        ),
           ('Congonhal'        , 'Itapuiuna'        ), ('Itapuiuna'        , 'Congonhal'        ),
           ('Itapuiuna'        , 'Andradas'         ), ('Andradas'         , 'Itapuiuna'        ),
           ('Andradas'         , 'Esp Santo Pinhal' ), ('Esp Santo Pinhal' , 'Andradas'         ),
           ('Esp Santo Pinhal' , 'Mogi Guacu'       ), ('Mogi Guacu'       , 'Esp Santo Pinhal' ),
           ('Mogi Guacu'       , 'Mogi Mirim'       ), ('Mogi Mirim'       , 'Mogi Guacu'       ),
           ('Mogi Mirim'       , 'Campinas'         ), ('Campinas'         , 'Mogi Mirim'       )]
                        

    
    cost={ ('Santa Rita'       , 'Pouso Alegre'     ): 28.9,
           ('Pouso Alegre'     , 'Cambui'           ): 49.1,
           ('Pouso Alegre'     , 'Borda da Mata'    ): 28.8,
           ('Pouso Alegre'     , 'Congonhal'        ): 24.3,
           ('Cambui'           , 'Camanducaia'      ): 24.7,
           ('Camanducaia'      , 'Braganca Paulista'): 60.4,
           ('Braganca Paulista', 'Atibai'           ): 25.2,
           ('Braganca Paulista', 'Itapira'          ): 82.4,
           ('Atibai'           , 'Campinas'         ): 65.6,
           ('Itapira'          , 'Campinas'         ): 70.7,
           ('Borda da Mata'    , 'Jacutinga'        ): 57.6,
           ('Jacutinga'        , 'Itapira'          ): 33.2,
           ('Congonhal'        , 'Itapuiuna'        ): 24.6,
           ('Itapuiuna'        , 'Andradas'         ): 67.6,
           ('Andradas'         , 'Esp Santo Pinhal' ): 28.4,
           ('Esp Santo Pinhal' , 'Mogi Guacu'       ): 37.5,
           ('Mogi Guacu'       , 'Mogi Mirim'       ): 25.0,
           ('Mogi Mirim'       , 'Campinas'         ): 60.1,
           
           ('Pouso Alegre'     , 'Santa Rita'       ): 28.9,
           ('Cambui'           , 'Pouso Alegre'     ): 49.1,
           ('Borda da Mata'    , 'Pouso Alegre'     ): 28.8,
           ('Congonhal'        , 'Pouso Alegre'     ): 24.3,
           ('Camanducaia'      , 'Cambui'           ): 24.7,
           ('Braganca Paulista', 'Camanducaia'      ): 60.4,
           ('Atibai'           , 'Braganca Paulista'): 25.2,
           ('Itapira'          , 'Braganca Paulista'): 82.4,
           ('Campinas'         , 'Atibai'           ): 65.6,
           ('Campinas'         , 'Itapira'          ): 70.7,
           ('Jacutinga'        , 'Borda da Mata'    ): 57.6,
           ('Itapira'          , 'Jacutinga'        ): 33.2,
           ('Itapuiuna'        , 'Congonhal'        ): 24.6,
           ('Andradas'         , 'Itapuiuna'        ): 67.6,
           ('Esp Santo Pinhal' , 'Andradas'         ): 28.4,
           ('Mogi Guacu'       , 'Esp Santo Pinhal' ): 37.5,
           ('Mogi Mirim'       , 'Mogi Guacu'       ): 25.0,
           ('Campinas'         , 'Mogi Mirim'       ): 60.1 }
         
    G=nx.DiGraph()
    
    G.add_nodes_from(nodes)
    
    #Adding the respective cost for each edge in the graph
    for u,v in edges:
        G.add_edge(u, v, weight=cost[u,v])
    positions = plotGraph(G, 1, None)
            
    #Creating an problem object based on FindPath class
    Problema = FindPath(G)
    
    #Creating an object for breadth first search algorithm for ``FindPath`` problem
    SearchObj = greedy_search(Problema)    
    
    
    start = 'Pouso Alegre'
    target = 'Campinas'
    print('\nSearching %s starting from %s...'%(target,start))
    solution,path,path_edges = SearchObj.search(start,target)
    print('Done!\n')
    if solution:
        print('Path found!')
        printPath(path,start)
        for u,v in edges:
            if (u,v) not in path_edges:
                G.remove_edge(u, v)
        plotGraph(G, 1, positions)        
    else:
        print('Path not found!')        