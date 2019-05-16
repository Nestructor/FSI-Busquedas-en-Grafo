# Search methods

import search

#Oradea -> Giurgiu
og = search.GPSProblem('O', 'G', search.romania)

#Arad -> Bucharest
ab = search.GPSProblem('A', 'B', search.romania)

#Craiova -> Fagaras
cf = search.GPSProblem('C', 'F', search.romania)

problem = ab

print("PRIMERO EN ANCHURA")
print(search.breadth_first_graph_search(problem).path())
print()
print("PRIMERO EN PROFUNDIDAD")
print(search.depth_first_graph_search(problem).path())
print()
print("RAMIFICACIÓN Y ACOTACIÓN")
print(search.branchAndBound(problem).path())
print()
print("RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACIÓN")
print(search.branchAndBoundSubestimation(problem).path())

""" Result:
 [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
 [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450 """