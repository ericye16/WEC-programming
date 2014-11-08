from dijkstra import Graph, dijkstra
from file_read import read_map

transitions = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
)


def between(x, min, max):
    return x >= min and x < max


def is_street(ch):
    return ch == 'H' or ch == ' '


def make_transition(y, x, transition):
    return y + transition[0], x + transition[1]


# def construct_graph(mapp):
#     g = Graph()
#     for y in range(len(mapp)):
#         for x in range(len(mapp[y])):
#             if isStreet(mapp[y][x]):
#                 g.add_node((y, x))
#                 if (y, x) not in g.edges:
#                     for transition in transitions:
#                         yNew = y + transition[0]
#                         xNew = x + transition[1]
#                         if (between(yNew, 0, len(mapp))
#                             and between(xNew, 0, len(mapp[y]))):
#                             if isStreet(mapp[yNew][xNew]):
#                                 g.add_edge((y, x), (yNew, xNew), 1)
#     return g


def dist(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)


def shortest_path(mapp, y1, x1, y2, x2):
    '''Finds the shortest path between two points on the map.

    Returns a tuple of pathlength and path. None if no path exists
    or either point is not on a street
    '''
    # for example:
    # mapp = ["XXX",
    #         "X X",
    #         "XHX"]
    # x1, x2 = 1, 1
    # y1, y2 = 1, 1
    #
    # greedy alg
    yCurrent, xCurrent = y1, x1

    path = []

    feasible = True

    visited = set()
    while yCurrent != y2 and xCurrent != x2 and feasible:
        dists = [float('inf')] * 4
        for i, transition in enumerate(transitions):
            yNew, xNew = make_transition(yCurrent, xCurrent, transition)
            if between(yNew, 0, len(mapp)) and between(xNew, 0, len(mapp[0])):
                if (yNew, xNew) not in visited and is_street(mapp[yNew, xNew]):
                    dists[i] = dist(yNew, xNew, y2, x2)
        if dists == [float('inf')] * 4:
            feasible = False
        bestTransition = transitions[dists.index(min(dists))]
        yNew, xNew = make_transition(yCurrent, xCurrent, bestTransition)
        visited.add((yCurrent, xCurrent))
        path.append((yCurrent, xCurrent))
        yCurrent, xCurrent = yNew, xNew
    if  yCurrent == y2 and xCurrent == x2:
        return len(path), path
    else:
        return None

if __name__ == "__main__":
    pass
