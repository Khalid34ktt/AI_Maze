import random

class Player:
  def __init__(self):
    self.search_tree = []
    pass

  def reset(self):
      #Initialize entrance for first node
    self.search_tree = []
    
    

    pass

  def set_maze(self, maze, entrance, exits):
    # sample code
    self.maze = {
      "n_row": maze["n_row"],
      "n_col": maze["n_col"]
    }
    self.entrance = {
      "position": entrance["position"],
      "actions": entrance["actions"],
      "entrance": entrance["entrance"],
      "exit": entrance["exit"]
    }
    self.exits = exits
    
#    set initial node
    actions = []
    if "n" in entrance["actions"]:
        actions.append("n")
    if "s" in entrance["actions"]:
        actions.append("s")
    if "e" in entrance["actions"]:
        actions.append('e')
    if "w" in entrance["actions"]:
        actions.append('w')
    
    self.search_tree.append({
            'id': 1,
            'state': entrance["position"],
            'children': [],
            'actions': actions,
            'removed': False,
            'parent': None
            })

    pass

  def next_node(self):
    # your code
    next_node_to_expand = []
    #Make sure lowest_cost is the highest value for cost possible in maze
    lowest_cost = self.maze["n_col"]*self.maze["n_col"] + self.maze["n_row"]*self.maze["n_row"]
    #Search every unsearched node to find the one with the lowest cost
    #Using A* search
    for node in self.search_tree:
        if node["removed"] == False:
            #Search in each direction from current node
            for direction in node["actions"]:
                #Lazy if statements
                #position node is going to move to
                node_position = node["state"]
                
                if direction == "n":
                    node_position[1]+=1
                elif direction == "s":
                    node_position[1]-=1
                elif direction == "e":
                    node_position[0]+=1
                elif direction == "w":
                    node_position[0]-=1
                #Calculate distance from entrance
                distance_from_entrance = abs(node_position[0]-self.entrance["position"][0]) + abs(node_position[1]-self.entrance["position"][1]) 
                #Calculate distance from every exit (square x and y distances)
                    #Making sure initial closest exit is always larger than possible
                closest_exit = self.maze["n_col"]*self.maze["n_col"] + self.maze["n_row"]*self.maze["n_row"]
                for individual_exit in self.exits:
                    #Determine distance from current point to the exit
                    distance_from_exit = (abs(node_position[0]-individual_exit[0])*abs(node_position[0]-individual_exit[0])) + (abs(node_position[1]-individual_exit[1])*abs(node_position[1]-individual_exit[1]))
                    #Determine if exit is the closest exit from current location
                    if distance_from_exit < closest_exit:
                        closest_exit = distance_from_exit
                #Determine if node has the lowest cost to explore, if so, assign it as the lowest cost and continue the search for the lowest cost
                if lowest_cost > distance_from_entrance + closest_exit:
                    lowest_cost = distance_from_entrance + closest_exit
                    next_node_to_expand = node_position
                    #node of parent
                    parent_node = node["state"]
    
    #Change searched node to false to prevent future searching
    for node in self.search_tree:
        if node["state"] == parent_node:
            node["removed"] = True
        
    print(self.search_tree)
    return next_node_to_expand

  def set_node_state(self, state):
#     sample code
#    new_node = {
#      "position": state["position"],
#      "actions": state["actions"],
#      "entrance": state["entrance"],
#      "exit": state["exit"]
#    }
#    if random.random() < 0.2:
#      sol = [self.entrance["position"]]
#      n_step = random.randrange(5,10)
#      for n in range(n_step):
#        next_step = [sol[-1][0], sol[-1][1]]
#        options = [[], []]
#        if next_step[0] > 0: options[0].append(-1)
#        if next_step[0] < self.maze["n_col"] - 1: options[0].append(1)
#        if next_step[1] > 0: options[1].append(-1)
#        if next_step[1] < self.maze["n_row"] - 1: options[1].append(1)
#        h_or_v = random.choice([0,1])
#        next_step[h_or_v] += random.choice(options[h_or_v])
#        sol.append(next_step)
#      solution = {
#        "found": True,
#        "solution": sol
#      }
#    else:
#      solution = {
#        "found": False,
#        "solution": []
#      }
    
#    Find all actions for node
    actions = []
    if "n" in state["actions"]:
        actions.append("n")
    if "s" in state["actions"]:
        actions.append("s")
    if "e" in state["actions"]:
        actions.append('e')
    if "w" in state["actions"]:
        actions.append('w')
    
    #Append all information on node to search tree
    self.search_tree.append({
            'id': len(self.search_tree),
            'state': state["position"],
            'children': [],
            'actions': actions,
            'removed': False,
            'parent': []
            })
        
    #Return solution
    if state["exit"] == True:
        solution = {
          "found": True,
          "solution": ["Lul"]
        }
    else:
        solution = {
          "found": False,
          "solution": []
        }
#
    return solution

  def get_search_tree(self):
   #'id': 1,
#  'state': [1,1],
#  'children': [2,3,4],
#  'actions': ['n','s','e'],
#  'removed': False,
#  'parent': None
    return self.search_tree
