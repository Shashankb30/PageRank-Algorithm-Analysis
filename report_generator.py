from datetime import datetime

def generate_general_report(pages, links, ranks, damping=0.85):
    report = f"""
PES UNIVERSITY
Department of Computer Science and Engineering

Course: Linear Algebra and Its Applications
Mini Project Report

Title:
Enhanced PageRank Algorithm Using Linear Algebra

--------------------------------------------
PROBLEM STATEMENT
--------------------------------------------
The goal of this project is to rank webpages based on their importance
using the PageRank algorithm. Each webpage is represented as a node
in a directed graph, and hyperlinks act as edges.

The challenge is to determine importance not just by number of links,
but by the importance of linking pages.

--------------------------------------------
LINEAR ALGEBRA PIPELINE
--------------------------------------------

Step 1: Graph Representation → Matrix Form

We model the web as a directed graph with {len(pages)} pages.
This is converted into an adjacency matrix A where:

A[i][j] = 1 if page j links to page i

--------------------------------------------

Step 2: Transition Matrix Construction

The adjacency matrix is normalized to form a column-stochastic matrix M:

M[i][j] = A[i][j] / (out-degree of page j)

For pages with no outgoing links (dangling nodes),
probability is distributed uniformly.

--------------------------------------------

Step 3: Google Matrix (Damping Factor)

To ensure convergence, we introduce damping:

G = dM + (1 - d)/n

where d = {damping}

This models a "random surfer" who either follows links or jumps randomly.

--------------------------------------------

Step 4: Power Iteration (Eigenvector Computation)

We compute PageRank using iterative multiplication:

r_(k+1) = G * r_k

This converges to the dominant eigenvector of G.

--------------------------------------------

Step 5: Convergence and Stability

The algorithm converges when:

||r_(k+1) - r_k|| < tolerance

This ensures stability of ranking.

--------------------------------------------

RESULTS (FINAL RANKINGS)
--------------------------------------------
"""

    # Add rankings
    for i, (page, score) in enumerate(ranks, 1):
        report += f"{i}. {page} : {score:.6f}\n"

    report += f"""
--------------------------------------------
INTERPRETATION
--------------------------------------------

• Pages with more incoming links generally rank higher.
• Pages linked by important pages gain higher rank.
• Dangling nodes were handled to avoid rank sinks.
• The system converges due to stochastic matrix properties.

--------------------------------------------
LINEAR ALGEBRA CONCEPTS USED
--------------------------------------------

• Matrices and Matrix Multiplication
• Stochastic Matrices
• Eigenvalues and Eigenvectors
• Markov Chains
• Convergence of Iterative Methods

--------------------------------------------
CONCLUSION
--------------------------------------------

This project demonstrates how linear algebra plays a crucial role
in real-world systems like search engines. The PageRank algorithm
is fundamentally an eigenvector problem solved efficiently using
iterative methods.

--------------------------------------------
Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

    return report


def save_report(report, filename="pagerank_report.txt"):
    with open(filename, "w") as f:
        f.write(report)

    print(f"Report saved as {filename}")