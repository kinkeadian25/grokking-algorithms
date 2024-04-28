from collections import deque

def generate_graph():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny "] = []

    return graph



def person_is_seller(name):
    return name[-1] == 'm'

def is_mango_seller_in_network():
    search_queue = deque()
    network_graph = {}

    network_graph = generate_graph()

    search_queue += network_graph["you"]

    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + " is a mango seller")
            return True
        else:
            search_queue += network_graph[person]

    return False

is_mango_seller_in_network()