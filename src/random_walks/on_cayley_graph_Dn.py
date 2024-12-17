import networkx as nx
import matplotlib.pyplot as plt
import random
from typing import List
from Node import Node

verbose = True

"""
For a simple random walk, that is, equal transition probabilites, set 'use_lambda_rw = False'.
For a RW_lambda random walk as defined in my thesis, set 'use_lambda_rw = True'.
lambd is the lambda value (lambda is a reserved name in Python).

Try setting lambd to something small like 1.000001 and then something large like 5 or 10. 
You will encounter the phenomena described in my thesis. This illustrates nicely, although 
very informally, the definition of the critical value.
"""
use_lambda_rw = True
lambd = 1.000001  # lambda > 1


class DihedralGraphWalk:
    def __init__(self, n: int):
        self.n = n
        self.nodes = self._generate_dihedral_graph_nodes()
        self.graph = nx.Graph()
        self.pos = {node.id: (node.x, node.y) for node in self.nodes}
        self._build_graph()

    def _generate_dihedral_graph_nodes(self) -> List[Node]:
        nodes = []
        angle_step = 2 * 3.14159 / self.n

        # Rotations (a)
        for i in range(self.n):
            x = 10 * round(math.cos(i * angle_step), 3)
            y = 10 * round(math.sin(i * angle_step), 3)
            neighbors = [
                (i + 1) % self.n,
                i + self.n,
            ]
            nodes.append(Node(i, x, y, neighbors))

        # Reflections (b)
        for i in range(self.n):
            x = 2 * 10 * round(math.cos(i * angle_step), 3)
            y = 2 * 10 * round(math.sin(i * angle_step), 3)
            neighbors = [
                (i + 1) % self.n + self.n,
                i,
            ]
            nodes.append(Node(i + self.n, x, y, neighbors))

        return nodes

    def _build_graph(self):
        for node in self.nodes:
            for neighbor_id in node.neighbors:
                self.graph.add_edge(node.id, neighbor_id)

    def get_distance_of_node(self, id: int) -> int:
        return min(id % self.n, self.n - (id % self.n)) if id < self.n else self.n

    def get_random_node(self, neighbors) -> int:
        if not use_lambda_rw:
            return random.choice(neighbors)
        else:
            conds = [lambd ** (-self.get_distance_of_node(v)) for v in neighbors]
            total_cond = sum(conds)
            probabilities = [c / total_cond for c in conds]
            ret = random.choices(neighbors, weights=probabilities, k=1)[0]

            if verbose:
                print("Conductances: " + str(conds))
                print("Probabilities: " + str(probabilities))
                print("Chosen next node: " + str(ret))
                print("-----------------------------")

            return ret

    def random_walk(self, start_node: int, steps: int = 10, delay: float = 0.5):
        current_node = start_node
        path = [current_node]

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

        for _ in range(steps):
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

            neighbors = self.nodes[current_node].neighbors
            next_node_id = self.get_random_node(neighbors)

            path.append(next_node_id)
            current_node = next_node_id

            ax.cla()

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


import math

graph_walk = DihedralGraphWalk(n=16)
graph_walk.random_walk(start_node=0, steps=500, delay=0.1)
