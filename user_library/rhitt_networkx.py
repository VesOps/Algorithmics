import networkx as nx
import matplotlib.pyplot as plt

# pretty graph diagram
def show(G, levels, spacing):
    # position nodes rigidly - spring layout is too chaotic for this
    pos = {}
    maxl = max(levels.values())
    xdict = {level: list(levels.values()).count(level) for level in range(maxl + 1)}

    for level in range(maxl+1):
        words = [word for word, i in levels.items() if i==level]
        offset = (xdict[level]-1)/2
        for i, word in enumerate(words):
            pos[word] = ((i-offset)*spacing, maxl-level)

    # draw graph
    plt.figure(figsize=(spacing*3,spacing))
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=300, font_size=6, edge_color='gray')
    
    plt.show()
