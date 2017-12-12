def import_graph_from_input():
    graph = {}
    with open("input-day12.txt") as rfile:
        for line in rfile.readlines():
            node = line.split("<->")[0].strip()
            edges = [e.strip() for e in line.split("<->")[1].split(",")]
            graph[node] = edges
    return graph

def main():
    graph = import_graph_from_input()
    visited_nodes = ['0']
    nodes_to_visit = graph['0']
    nodes_in_group = 1
    while nodes_to_visit:
        if nodes_to_visit[0] not in visited_nodes:
            nodes_to_visit.extend(graph[nodes_to_visit[0]])
            visited_nodes.append(nodes_to_visit[0])
            nodes_in_group += 1
        nodes_to_visit = nodes_to_visit[1:]
    print(nodes_in_group)

if __name__ == '__main__':
    main()
