import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def draw_graph(pages, links, ranks=None):
    G = nx.DiGraph()

    for p in pages:
        G.add_node(p)

    for src, dsts in links.items():
        for d in dsts:
            G.add_edge(src, d)

    sizes = None
    if ranks is not None:
        sizes = [5000 * r for r in ranks]

    plt.figure(figsize=(8,6))
    nx.draw(G, with_labels=True, node_size=sizes)
    plt.title("Web Graph (Node size = Rank)")
    plt.show()


def plot_convergence(history, pages):
    plt.figure(figsize=(8,5))
    for i, p in enumerate(pages):
        plt.plot(history[:, i], label=p)

    plt.title("PageRank Convergence")
    plt.xlabel("Iteration")
    plt.ylabel("Score")
    plt.legend()
    plt.grid()
    plt.show()


def plot_damping(results, pages):
    plt.figure(figsize=(8,5))

    for d, (_, hist) in results.items():
        plt.plot(hist[:,0], label=f"d={d}")

    plt.title("Damping Effect (Google Page)")
    plt.legend()
    plt.grid()
    plt.show()


def compare_bars(default, personalized, pages):
    x = np.arange(len(pages))

    plt.figure(figsize=(8,5))
    plt.bar(x-0.2, default, width=0.4, label="Default")
    plt.bar(x+0.2, personalized, width=0.4, label="Personalized")

    plt.xticks(x, pages, rotation=45)
    plt.legend()
    plt.title("Default vs Personalized PageRank")
    plt.show()