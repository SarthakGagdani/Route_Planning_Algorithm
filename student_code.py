import math
from queue import PriorityQueue

def shortest_path(graph, start, goal):
    
    frontier= PriorityQueue()      #frontier is a priority queue.
    frontier.put(start, 0)
    
    previous = {start: None}
    g= {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            path(previous, start, goal)

        for neighbor in graph.roads[current]:
            tempg = g[current] + h(graph.intersections[current], graph.intersections[neighbor])
            
            if neighbor not in g or tempg < g[neighbor]:
                g[neighbor] = tempg
                totalScore = tempg + h(graph.intersections[current], graph.intersections[neighbor])
                frontier.put(neighbor, totalScore)
                previous[neighbor] = current

    return path(previous, start, goal)


#Distance formula in maths,returning distance from start to goal
def h(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))      

def path(previous, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = previous[current]
        path.append(current)
    path.reverse()
    return path