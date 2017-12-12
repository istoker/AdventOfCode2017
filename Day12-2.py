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
    number_of_groups = 0
    visited_nodes = []
    for key in graph:
        if key not in visited_nodes:
            number_of_groups += 1
            visited_nodes.append(key)
            nodes_to_visit = graph[key]
            while nodes_to_visit:
                if nodes_to_visit[0] not in visited_nodes:
                    nodes_to_visit.extend(graph[nodes_to_visit[0]])
                    visited_nodes.append(nodes_to_visit[0])
                nodes_to_visit = nodes_to_visit[1:]
    print(number_of_groups)

if __name__ == '__main__':
    main()
