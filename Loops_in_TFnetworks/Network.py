import igraph as ig
import csv

txt_file = 'network_tf_clean.txt'

def open_network(filename): 
    
    network = ig.Graph(directed=True)
    edge_names = [] 
    vertex_names = []
    num_self_edges = 0 
    
    with open(txt_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t') 
        # use dictionary and counter to convert gene names to #s
        counter = 0
        gene_dict = {}
        for row in reader :
            # [0] - TF #1, [1] - TF #2, [2] = +,-, +-, ?
            tf1 = row[0].lower()
            tf2 = row[1].lower()
            edge_type = row[2]
            tf1_idx, tf2_idx = 0, 0

            if tf1 not in gene_dict : 
                gene_dict[tf1] = counter
                network.add_vertices(1)
                vertex_names.append(tf1)
                tf1_idx = counter
                counter += 1
            else : 
                tf1_idx = gene_dict[tf1]

            if tf2 not in gene_dict : 
                gene_dict[tf2] = counter
                network.add_vertices(1)
                vertex_names.append(tf2)
                tf2_idx = counter
                counter += 1
            else :
                tf2_idx = gene_dict[tf2]

            if (tf1 == tf2) :
                num_self_edges += 1

            network.add_edge(tf1_idx, tf2_idx)
            edge_names.append(edge_type)
            if (edge_type == '+') :
                network.es[len(edge_names)-1]["color"] = 'green'
            if (edge_type == '-') :
                network.es[len(edge_names)-1]["color"] = 'red'

    return (network, vertex_names)

network, vertex_names = open_network(txt_file)

print("Number of nodes: ", len(network.vs))
print("Number of edges: ", len(network.es))
print("Number of self-loops: ", sum(ig.Graph.is_loop(network)))

ig.plot(network, vertex_label=vertex_names, vertex_label_size=8, edge_arrow_width=1, edge_arrow_size=0.5, autocurve=True, target='network.pdf')