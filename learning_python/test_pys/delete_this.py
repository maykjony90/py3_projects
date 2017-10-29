# -----------------------------------------------------------------------------
# find_path_to_friend(network, user_A, user_B):
#   Finds a connections path from user_A to user_B. It has to be an existing
#   path but it DOES NOT have to be the shortest path.
#
# Arguments:
#   network: The network you created with create_data_structure.
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
#
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print find_path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam,
#   who is connected with Zed.
#
# NOTE:
#   You must solve this problem using recursion!
#
# Hints:
# - Be careful how you handle connection loops, for example, A is connected to B.
#   B is connected to C. C is connected to B. Make sure your code terminates in
#   that case.
# - If you are comfortable with default parameters, you might consider using one
#   in this procedure to keep track of nodes already visited in your search. You
#   may safely add default parameters since all calls used in the grading script
#   will only include the arguments network, user_A, and user_B.
def find_path_to_friend(network, user_A, user_B, nodes_visited=[]):
    if user_A not in network or user_B not in network:
        return None
    else:
        return main_path_finder(network, user_A, user_B, nodes_visited=[])

def main_path_finder(network, user_A, user_B, nodes_visited=[],
                     not_to_check=[]):

# Iki tane kosulu vardi bu gorev icin:
    # 1.
    # base case
    # aradigimiz kisiye ulastiysak kisiye giden yol geri don
    if user_A == user_B:
        nodes_visited.append(user_B)
        # Eninde sonunda yolu bulur ve bunu dunyaya haykirir
        return "PATH FOUND: \t{}\n".format(nodes_visited)

    # Kisinin arkadas listesine tek tek bakip, onlarin arkadas oldugu
    # kisileri arastirirdi
    for connection in network[user_A]['connections']:
        # Eger baktigi kisinin arkadasi yoksa, onu arama listesinden
        # oylece cikariverir, bir sonraki kisiye yonelirdi
        if network[connection]['connections'] == [] or connection in nodes_visited:
            continue
        
        # ugradigi node'larin kaydini tutardi
        nodes_visited.append(user_A)
        
        # aramaktan hic gocunmaz, teker teker butun node'lari dolasirdi
        return main_path_finder(network, connection, user_B, nodes_visited)
        
    # Aradigini bulamadiysa eger, bunu acik acik soylerdi
    print("There is no path from {} to {}".format(nodes_visited[0], user_B))
    return False 
 
