import heapq
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = float("inf")
    # def update(self,state,parent,action,cost):
    #     if(cost < self.cost):
    #         self.state = state
    #         self.parent = parent
    #         self.action = action
    #         self.cost = cost

class Frontier():
    def __init__(self):
        self.frontier = []
        heapq.heapify(self.frontier)

    def add(self, node):
        heapq.heappush(self.frontier,(A_star_F(node),node))

    def contains_state(self, state):
        return any(element[1].state == state for element in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = A_star()
            self.frontier = self.frontier[:-1]
            return node