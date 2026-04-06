# 🔍 Enhanced PageRank Algorithm using Linear Algebra

## 📌 Overview

This project implements the **PageRank algorithm** using core concepts from **Linear Algebra**, including matrix operations, stochastic processes, and eigenvector computation.

It models the web as a directed graph and ranks pages based on their importance using **power iteration on the Google matrix**.

---

## 🚀 Features

* ✅ Graph-based webpage modeling using adjacency lists
* ✅ Adjacency → Transition → Google matrix pipeline
* ✅ Power Iteration method for eigenvector computation
* ✅ Handling of **dangling nodes (dead-ends)**
* ✅ Visualization of:

  * Web graph (NetworkX)
  * PageRank scores (bar chart)
  * Convergence behavior (iteration plot)
* ✅ **Advanced Extensions**:

  * Compare PageRank with/without damping
  * Analyze effect of different damping factors (0.6, 0.85, 0.95)
  * Personalized PageRank (bias vector)
* ✅ Automated **PDF report generation with embedded graphs**

---

## 🧠 Linear Algebra Concepts Used

* Matrices & Matrix Multiplication
* Stochastic (Markov) Matrices
* Eigenvalues & Eigenvectors
* Power Iteration Method
* Convergence of Iterative Systems

---

## 📊 Project Pipeline

1. **Graph Representation**

   * Webpages → Nodes
   * Hyperlinks → Directed edges

2. **Adjacency Matrix (A)**

   * A[i][j] = 1 if page *j* links to page *i*

3. **Transition Matrix (M)**

   * Normalize columns → probability distribution

4. **Google Matrix (G)**

   * G = dM + (1 - d)/n

5. **Power Iteration**

   * Compute dominant eigenvector

6. **Ranking Output**

   * Sort pages by PageRank score

---

## 📈 Sample Output

```
Final Rankings:
1. Google     : 0.2432
2. Wikipedia  : 0.1983
3. YouTube    : 0.1542
...
```

---

## 📉 Visualizations

* 📌 Graph structure of webpages
* 📊 Final PageRank distribution
* 📈 Convergence of rank values over iterations

---

## 🧪 Advanced Experiments

| Feature           | Description                             |
| ----------------- | --------------------------------------- |
| Damping Analysis  | Compare results for d = 0.6, 0.85, 0.95 |
| No Damping Case   | Shows instability without teleportation |
| Personalized PR   | Bias ranking toward specific nodes      |
| Dead-End Handling | Redistribute probability uniformly      |

---

## 📁 Project Structure

```
pagerank-project/
│
├── main.py                # Main execution script
├── utils.py               # Matrix + PageRank logic
├── report_generator.py    # PDF report + graphs
├── plots/                 # Generated images
├── reports/               # Generated PDF reports
└── README.md
```

---

## ⚙️ Installation

```bash
pip install numpy matplotlib networkx reportlab
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📄 Report Generation

The project automatically generates:

* 📊 Graph plots
* 📄 PDF report with embedded visuals

---

## 💡 Key Insights

* PageRank is fundamentally an **eigenvector problem**
* Importance depends on **quality of incoming links**
* Damping ensures **convergence and stability**
* Real-world systems rely on **sparse matrix optimization**

---

## 🏆 Why This Project Stands Out

* Combines **theory + implementation + visualization**
* Demonstrates real-world use of **Linear Algebra**
* Includes **advanced features beyond basic PageRank**
* Produces **publication-style reports**

---

## 📚 References

* PageRank Algorithm – Larry Page & Sergey Brin (1998)
* Markov Chains & Stochastic Processes
* Linear Algebra (Eigenvalues & Eigenvectors)

---

## ⭐ If you like this project, give it a star!
