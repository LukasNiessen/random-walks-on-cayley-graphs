# Random Walks on Cayley Graphs

## Bachelor Thesis Lukas Nießen

This repository is part of my bachelor thesis and contains Python scripts for simulating random walks on graphs. This includes integer lattices, custom graphs, and Cayley graphs. These simulations are meant to give an intuitive understanding of the topic.

## Prerequisites

- **Python**: Python must be installed on your machine. Download it from [python.org](https://www.python.org/).
- **Dependencies**: Install the required libraries with:
  ```bash
  pip install networkx matplotlib --user
  ```
- **networkx**: For creating and manipulating graphs.
- **matplotlib**: For visualizing random walk paths.
- **Optional**: I recommend using an Integrated Development Environment (IDE) like VS Code or Spyder.

## Overview of Files

- on_integer_lattices.py: Simulates simple random walks on ℤ, ℤ², and ℤ³.
- on_some_graph.py: Allows custom graph creation for random walks. You can define your own graph by specifying nodes and edges or you can also choose a predefined graph.
- on_cayley_graph.py: Simulates random walks on the Cayley graph of the group ℤ/nℤ with the generating set {+1, -1}. You can either have a simple random walk or an "RW_lambda" random walk, which is central to the thesis's main theorem. For details please look at the comments at the top of the file.

## Usage

You can run the scripts directly from the command line or within an IDE. Command line example:

```bash
python on_integer_lattices.py
```

Please follow the comments within the scripts and modify variables as needed to customize the random walk behavior.

## Notes

Our graphs are all undirected. Although we should actually have directed graphs this is good enough for our simulation as in the thesis we assume that every edge occurrs in both directions.

# Introduction

Random walks are processes that describe objects randomly moving away from where they started. They have applications in diverse areas, such as particle diffusion in physics and modeling stock price fluctuations in finance. Mathematically, a random walk can be modeled as a sequence of steps on a predefined structure, such as the real line, a lattice, or more generally, a graph. In the context of graph theory, this corresponds to randomly moving from one node to another, following the edges of the graph. A common research question is whether a random walk is _recurrent_, meaning it returns to the starting point infinitely often, or _transient_, meaning it eventually escapes and does not return to the starting point.

One famous result in this field is [Pólya’s theorem](https://en.wikipedia.org/wiki/Random_walk#Higher_dimensions), which states that the simple random walk on Z^d is recurrent in dimensions d=1,2 and transient otherwise. In his paper from 1921 [MR1512028](https://doi.org/10.1007/BF01458701), he proved the theorem using elementary methods of probability theory and analysis. We will present a very short and elegant partial proof in Chapter 3, primarily using electrical network theory, which is a branch of mathematics inspired by physical principles. This thesis is based on the book [MR3616205](http://dx.doi.org/10.1017/9781316672815) and focuses on a certain type of random walk where the probability of moving farther from the starting point decreases exponentially with the distance. A fundamental result in this context is the existence of a _critical value_: if the probability of stepping farther decays faster than the critical value 'allows', the walk is recurrent; otherwise, it is transient.

Our interest lies in determining this critical value for random walks on Cayley graphs, which are graphs associated with groups and their generators. It turns out that this critical value is deeply connected to 'how fast the graph grows'. The main theorem of this thesis establishes that, for Cayley graphs with finite generating sets, the critical value is exactly the exponential growth rate of the graph. Here is a simplified version of the main theorem.

```
Let M_n be the number of nodes with distance n to the root. Then the 'exponential-decay random walk' described above on an infinite Cayley graph has a critical value identical to the exponential growth rate of the graph.
```

To prove this, we will analyze a subtree of the graph. Our theory primarily involves electrical network theory, focusing on concepts such as finite energy flows and admissible flows. However, we also use results from probability theory, group theory, and discrete mathematics. The main theorem is particularly interesting because it builds a bridge between group structure and probability theory. It has several applications; one example is making dimension statements in the context of derived trees (see Chapter _Derived Trees_ in [MR3616205](http://dx.doi.org/10.1017/9781316672815)).

We begin with definitions and terminology in Chapter 1. Then, in Chapter 2, we provide an overview of discrete harmonic functions, which play a key role in this thesis because many of the functions we will use, such as the _voltage function_, are harmonic. Chapter 3 is devoted to electrical network theory, presenting crucial results like Thomson's Principle, Rayleigh's Monotonicity Principle, the Nash-Williams Inequality, and the Nash-Williams Criterion. In that chapter, we also establish the connection between recurrence/transience and finite energy flows which is due to T. Lyons (1983). Finally, in Chapter 4, we prove the main theorem and also look at the 'opposite case' of random walks where the probability of moving farther from the starting point grows exponentially with the distance.

# Acknowledgments

I owe special thanks to several people who made this thesis possible. Professor Eveliina Peltola and Doctor Alexis Langlois-Rémillard have shown great support and have given amazing feedback throughout the past half-year of writing this thesis. I want to thank both of you very much for everything.

To my parents, dear Loretta and Wolfgang, your relentless drive and iron will have been the foundation on which I have built my life, and for that, I am and will remain forever grateful.
