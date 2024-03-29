import heapq
from copy import copy, deepcopy
from sys import stdin, stdout

class Node():
    def __init__(self, state, parent, action , cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
    # def update(self,state,parent,action,cost):
    #     if(cost < self.cost):
    #         self.state = state
    #         self.parent = parent
    #         self.action = action
    #         self.cost = cost

def heuristic(state,target_place):
    n = len(state)
    h = 0
    for i in range(n):
        for j in range(n):
            x_dif = abs(j - target_place[state[i][j]][1])
            y_dif = abs(i - target_place[state[i][j]][0])
            if (x_dif > n//2 ): 
                x_dif = n - x_dif
            if (y_dif > n//2):
                y_dif = n - y_dif
            h = h +  x_dif * 5  + y_dif * 5
    return h

def A_star_F(node,target_place):
    return node.cost + heuristic(node.state,target_place)

def find_target_places(target):
    target_places = {}
    for i in range(len(target)):
        for j in range(len(target)):
            target_places[target[i][j]] =  (i,j)
    return target_places 

class Frontier():
    def __init__(self,target_place):
        self.states = set()
        self.A_star = []
        self.target_place = target_place
        self.dic = {}
        heapq.heapify(self.A_star)

    def add(self, node):
        try:
            self.states.add(node.state)
            A_star_score = A_star_F(node,self.target_place)
            if A_star_score in self.dic.keys() :
                self.dic[A_star_score].append(node) 
            else:
                self.dic[A_star_score] = [node]
            heapq.heappush(self.A_star,A_star_score)
        except:
            pass
        

    def contains_state(self, state):
        return state in self.states

    def empty(self):
        return len(self.A_star) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node_score  = heapq.heappop(self.A_star)
            node = self.dic[node_score].pop()
            return node

def find_adjacent_nodes(node):
    adjacent_nodes = []
    current = list(map(list,node.state))
    # right moves 
    adjacent = []
    for i in range(len(current)):
         adjacent = deepcopy(current)
         adjacent[i][1:] = current[i][0:-1]
         adjacent[i][0] = current[i][-1]
         adjacent = tuple(map(tuple,adjacent))
         adjacent_nodes.append(("right "+str(i+1),adjacent))
    # left moves 
    adjacent = []
    for i in range(len(current)):
         adjacent = deepcopy(current) 
         adjacent[i][0:-1] = current[i][1:]
         adjacent[i][-1] = current[i][0]
         adjacent = tuple(map(tuple,adjacent))
         adjacent_nodes.append(("left "+str(i+1),adjacent))
    # down moves 
    adjacent = []
    for i in range(len(current)):
         adjacent = deepcopy(current)
         adjacent[0][i] = current[-1][i]
         for j in range(1,len(current)):
            adjacent[j][i] = current[j-1][i]
         adjacent = tuple(map(tuple,adjacent))
         adjacent_nodes.append(("down "+str(i+1),adjacent))
    # up moves 
    adjacent = []
    for i in range(len(current)):
         adjacent = deepcopy(current)
         adjacent[-1][i] = current[0][i]
         for j in range(0,len(current)-1):
            adjacent[j][i] = current[j+1][i]
        
         adjacent = tuple(map(tuple,adjacent))
         adjacent_nodes.append(("up "+str(i+1),adjacent))
    return adjacent_nodes
    





def path(source , target):

    source_node = Node(source,None,None,0)
    target_place = find_target_places(target)
    frontier = Frontier(target_place)
    frontier.add(source_node)

    # explored = set()
    
    targetNode = Node(None,None,None,None)

    while(True):
        if frontier.empty():
            return None
        nextNode = frontier.remove()
        # if(len(frontier.frontier )> 5500):
        #     print("..")
        # explored.add(nextNode.state)

        if nextNode.state == target :
            targetNode = nextNode
            break
        adjacent_nodes  = find_adjacent_nodes(nextNode)
        for adjacent in adjacent_nodes :
            if not frontier.contains_state(adjacent[1]) :
                frontier.add(Node(adjacent[1],nextNode,adjacent[0],nextNode.cost + 1))
    
    # put the shortest path in the list 
    shortest_path_list = []
    while(True):
        if targetNode.state == source :
            break
        else:
            shortest_path_list.append((targetNode.action,targetNode.state))
        targetNode = targetNode.parent

    shortest_path_list.reverse()


    return shortest_path_list

# def fast_input():
#     input = io.BytesIO(os.read(0, \
#             os.fstat(0).st_size)).readline
        
#         # Taking input as string 
#     s = input().decode()
#     return s

X_star = []
X_0 = []    
n = int(stdin.readline())
for i in range(n):
    X_star.append(tuple(list(map(lambda x : int(x) ,stdin.readline().split()))))
for i in range(n):
    X_0.append(tuple(list(map(lambda x : int(x) ,stdin.readline().split()))))

X_0 = tuple(X_0)
X_star = tuple(X_star)

path_to_X_star = path(X_0,X_star)
print(len(path_to_X_star))
for i in range(len(path_to_X_star)):
    print(path_to_X_star[i][0])



