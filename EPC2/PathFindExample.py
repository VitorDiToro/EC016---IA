'''
@author: Edielson - https://github.com/edielsonpf
'''
from SearchAlgorithms.breadth_first_search import breadth_first_search
import networkx as nx  # https://networkx.github.io/"
import matplotlib.pyplot as plt


def printPath(path, start):
    string = (start)
    for city in path:
        if city != start:
            string = (string+' -> '+city)
    print(string)


def plotGraph(G, option, position=None):
    """Plot a graph G with specific position.

    Parameters
    ----------
    G : NetworkX graph
    option : if 1, edges with weight greater then 0 are enlarged. The opposite
             happens for option equal to 0.
    position : nodes position

    Returns
    -------
    position: nodes position generated during plot (or same positions if supplied).
    """

    if option == 1:
        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0]
        esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0]
    else:
        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0]
        esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0]

    if position is None:
        position = nx.spring_layout(G)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, position, node_size=500)

    # edges
    nx.draw_networkx_edges(G, position, edgelist=elarge, width=2)
    nx.draw_networkx_edges(G, position, edgelist=esmall, width=2,
                           alpha=0.5, edge_color='b', style='dashed')

    # labels
    nx.draw_networkx_labels(G, position, font_size=20, font_family='sans-serif')

    plt.axis('off')
    # plt.savefig("weighted_graph.png") # save as png
    plt.show()  # display

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
        return solution

    def ExpandSolution(self, current):
        """
        Returns all possible states from ``current``
        """
        return self.problem.neighbors(current)


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
                

    G = nx.DiGraph()

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # You must change here if there is a different cost per edge
    CostperEdge = [1 for i in range(len(edges))]

    # Adding the respective cost for each edge in the graph
    for u, v in edges:
        G.add_weighted_edges_from([(u, v, CostperEdge[edges.index((u, v))])])

    positions = plotGraph(G, 1, None)

    # Creating an problem object based on FindPath class
    Problema = FindPath(G)

    # Creating an object for breadth first search algorithm for ``FindPath`` problem
    SearchObj = breadth_first_search(Problema)

    start = 'Pouso Alegre'
    target = 'Campinas'
    print('\nSearching %s starting from %s...' % (target, start))
    solution, path, path_edges = SearchObj.search(start, target)
    print('Done!\n')
    if solution:
        print('Path found!')
        printPath(path, start)
        for u, v in edges:
            if (u, v) not in path_edges:
                G.remove_edge(u, v)
        plotGraph(G, 1, positions)
    else:
        print('Path not found!')
