import matplotlib.pyplot as plt
import networkx as nx

def kruskal_visualization(graph):
    G = nx.Graph()
    for edge in graph['edges']:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    edges_sorted = sorted(graph['edges'], key=lambda x: x[2])
    
    parent = {node: node for node in graph['nodes']}
    rank = {node: 0 for node in graph['nodes']}
    
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        
        if u_root == v_root:
            return False
        
        if rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[u_root] = v_root
            if rank[u_root] == rank[v_root]:
                rank[v_root] += 1
        return True
    
    mst_edges = []
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 6))
    
    for i, edge in enumerate(edges_sorted, 1):
        u, v, w = edge
        
        if find(u) != find(v):
            if union(u, v):
                mst_edges.append((u, v, w))
            
            plt.clf()
            
            nx.draw_networkx_edges(G, pos, edgelist=G.edges(), 
                                 edge_color='lightgray', width=1, alpha=0.3)
            
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v, w in mst_edges], 
                                 edge_color='red', width=2)
            
            nx.draw_networkx_nodes(G, pos, node_color='darkgray', node_size=500)
            nx.draw_networkx_labels(G, pos)
            
            edge_labels = {(u, v): w for u, v, w in G.edges(data='weight')}
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
            
            plt.title(f"Шаг {i}: Проверяем ребро {u}-{v} (вес {w})")
            if (u, v, w) in mst_edges:
                plt.title(f"Шаг {i}: Добавляем ребро {u}-{v} (вес {w})")
            
            plt.draw()
            plt.pause(2.0)
    
    plt.title("Минимальное остовное дерево построено!")
    plt.show()
    return mst_edges

graph = {
    'nodes': ['A', 'B', 'C', 'D', 'E'],
    'edges': [
        ('A', 'B', 1), ('A', 'C', 3), ('B', 'C', 2),
        ('B', 'D', 4), ('C', 'D', 5), ('C', 'E', 6), ('D', 'E', 7)
    ]
}

mst = kruskal_visualization(graph)
print("Минимальное остовное дерево:", mst)