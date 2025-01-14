data = (i:=__import__)('sys').stdin.read().strip().splitlines()
graph = (n:=i('networkx')).Graph()
for line in data:
    a, b = line.split("-")
    graph.add_edge(a,b)
print(len([i for i in n.enumerate_all_cliques(graph) if len(i) == 3 and any(node.startswith('t') for node in i)]))
print(",".join(sorted(max(n.find_cliques(graph), key=len))))
