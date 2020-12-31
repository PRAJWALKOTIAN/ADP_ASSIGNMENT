from sys import maxsize 
from itertools import permutations
def travellingSalesmanProblem(graph, s): 
    vertex = [] 
    for i in range(n): 
        if i != s: 
            vertex.append(i) 
    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
        min_path = min(min_path, current_pathweight)      
    return min_path 
n=int(input("Enter the value of n ="))
print("Enter the distance between cities")
graph = [] 
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    graph.append(a)
print("The distance between cities in the form of matrix")
for i in range(n):
    for j in range(n):
        print(graph[i][j],end=" ")
    print()
s = 0
print("The minimum distance required to visit all cities is=",travellingSalesmanProblem(graph, s))
