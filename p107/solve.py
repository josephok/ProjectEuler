from collections import defaultdict

def build_gragh():
    graph = dict()
    with open('network.txt') as f:
        lines = f.read().splitlines()
        for vh, line in enumerate(lines, start=1):
            g = dict()
            for vs, v in enumerate(line.split(','), start=1):
                try:
                    g[str(vs)] = int(v)
                except ValueError:
                    g[str(vs)] = None
            graph[str(vh)] = g

    return graph

# test gragh
"""
graph = {
    'A': {'B': 16, 'C': 12, 'D': 21},
    'B': {'A': 16, 'D': 17, 'E': 20},
    'C': {'A': 12, 'D': 28, 'F': 31},
    'D': {'A': 21, 'B': 17, 'C': 28, 'E': 18, 'F': 19, 'G': 23},
    'E': {'B': 20, 'D': 18, 'G': 11},
    'F': {'C': 31, 'D': 19, 'G': 27},
    'G': {'D': 23, 'E': 11, 'F': 27}
}
"""

def sum_weight(graph, duplicate=True):
    sum_ = 0
    for v in graph:
        for vs in graph[v]:
            if graph[v][vs] != None:
                sum_ += graph[v][vs]

    if duplicate:
        return sum_ // 2
    else:
        return sum_

graph = build_gragh()

def prim_tree(graph):
    vertes = list(graph.keys())
    selected = set()
    selected.add(vertes[0])
    vertes.pop(0)
    
    new_graph = defaultdict(dict)
    while vertes:
        tmp = 1000
        for u in selected:
            for v in vertes:
                try:
                    if graph[u][v] != None and graph[u][v] < tmp:
                        tmp = graph[u][v]
                        choose_u = u
                        choose_v = v

                except KeyError:
                    pass

        selected.add(choose_v)
        vertes.remove(choose_v)
        new_graph[choose_u][choose_v] = tmp

    return new_graph

print("before: ")
sum1 = sum_weight(graph, duplicate=True)
print(sum1)
print("after:")
sum2 = sum_weight(prim_tree(graph), duplicate=False)
print(sum2)

print("saving: {}".format(sum1 - sum2))