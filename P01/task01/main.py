from graph import *
from utils import *
from prettytable import PrettyTable





print("Breadth First Search: " + path_cost(breadth_first_search(romania, 'Bi', 'Ti'), romania).__str__())
print(breadth_first_search(romania, 'Bi', 'Ti'))
print("Depth First Search: " + path_cost(depth_first_search(romania, 'Bi', 'Ti'), romania).__str__())
print(depth_first_search(romania, 'Bi', 'Ti'))
print("Uniform Cost Search: " + path_cost(uniform_cost_search(romania, 'Bi', 'Ti'), romania).__str__())
print(uniform_cost_search(romania, 'Bi', 'Ti'))
