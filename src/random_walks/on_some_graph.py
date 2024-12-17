import networkx as nx
import matplotlib.pyplot as plt
import random
from typing import List
from Node import Node


class GraphWalk:
    def __init__(self, nodes: List[Node]):
        self.nodes = {node.id: node for node in nodes}
        self.graph = nx.Graph()
        self.pos = {node.id: (node.x, node.y) for node in nodes}
        self._build_graph()

    def _build_graph(self):
        for node in self.nodes.values():
            for neighbor_id in node.neighbors:
                self.graph.add_edge(node.id, neighbor_id)

    def random_walk(self, start_node: int, steps: int = 10, delay: float = 0.5):
        current_node = start_node
        path = [current_node]

        # Initialize plot
        plt.ion()
        fig, ax = plt.subplots()
        nx.draw(
            self.graph,
            pos=self.pos,
            ax=ax,
            with_labels=True,
            node_color="lightblue",
            node_size=500,
        )

        # Perform the random walk
        for step in range(steps):
            # Highlight the current node
            nx.draw(
                self.graph,
                pos=self.pos,
                ax=ax,
                with_labels=True,
                node_color="lightblue",
                node_size=500,
            )
            nx.draw_networkx_nodes(
                self.graph,
                pos=self.pos,
                nodelist=[current_node],
                node_color="red",
                node_size=700,
            )
            plt.draw()
            plt.pause(delay)

            # Choose the next node randomly based on neighbors
            neighbors = self.nodes[current_node].neighbors
            if not neighbors:
                print("No more neighbors to walk to.")
                break
            next_node = random.choice(neighbors)
            path.append(next_node)
            current_node = next_node

            # Clear the plot for the next step
            ax.cla()

        # Show final path
        plt.ioff()
        nx.draw(
            self.graph,
            pos=self.pos,
            ax=ax,
            with_labels=True,
            node_color="lightblue",
            node_size=500,
        )
        nx.draw_networkx_nodes(
            self.graph, pos=self.pos, nodelist=path, node_color="orange", node_size=700
        )
        plt.show()


nodes_data_1 = [
    Node(0, 2, 0, [1, 5]),
    Node(1, 0, 2, [0, 2, 3, 4]),
    Node(2, 0, 4, [1, 3]),
    Node(3, 2, 2, [1, 2, 6]),
    Node(4, 2, 4, [1, 6]),
    Node(5, 4, 0, [0]),
    Node(6, 4, 2, [3, 4]),
]

nodes_data_2 = [
    Node(0, 0, 0, [6, 1]),
    Node(1, 0, 1, [6, 0, 2]),
    Node(2, 0, 2, [6, 1, 3]),
    Node(3, 0, 3, [6, 2, 4]),
    Node(4, 0, 4, [6, 3, 5]),
    Node(5, 0, 5, [6, 4]),
    Node(6, 4, 2.5, [0, 1, 2, 3, 4, 5]),
]

use_data_x = 1

if use_data_x == 1:
    graph_walk = GraphWalk(nodes=nodes_data_1)
elif use_data_x == 2:
    graph_walk = GraphWalk(nodes=nodes_data_2)

graph_walk.random_walk(start_node=0, steps=200, delay=0.3)
