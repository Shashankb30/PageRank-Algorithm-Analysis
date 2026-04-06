import numpy as np

from datetime import datetime

# -----------------------------
# Generate experiment report
# -----------------------------
def generate_report(
    pages,
    base_ranks,
    damping_results,
    personalized_ranks,
    filename="pagerank_report.txt"
):
    with open(filename, "w") as f:

        # Header
        f.write("PAGE RANK ANALYSIS REPORT\n")
        f.write("="*40 + "\n")
        f.write(f"Generated on: {datetime.now()}\n\n")

        # -----------------------------
        # Base Rankings
        # -----------------------------
        f.write("1. BASE PAGE RANK RESULTS\n")
        f.write("-"*40 + "\n")

        sorted_base = sorted(zip(pages, base_ranks),
                             key=lambda x: x[1],
                             reverse=True)

        for i, (p, score) in enumerate(sorted_base, 1):
            f.write(f"{i}. {p:10} : {score:.6f}\n")

        f.write("\n")

        # -----------------------------
        # Damping Comparison
        # -----------------------------
        f.write("2. DAMPING FACTOR ANALYSIS\n")
        f.write("-"*40 + "\n")

        for d, (r, _) in damping_results.items():
            f.write(f"\nDamping = {d}\n")
            sorted_r = sorted(zip(pages, r),
                              key=lambda x: x[1],
                              reverse=True)
            for p, score in sorted_r[:3]:
                f.write(f"  {p:10} : {score:.4f}\n")

        f.write("\n")

        # -----------------------------
        # Personalized PageRank
        # -----------------------------
        f.write("3. PERSONALIZED PAGERANK\n")
        f.write("-"*40 + "\n")

        for p, base, pers in zip(pages, base_ranks, personalized_ranks):
            f.write(f"{p:10} | Base: {base:.4f} | Personal: {pers:.4f}\n")

        f.write("\n")

        # -----------------------------
        # Insights (AUTO GENERATED)
        # -----------------------------
        f.write("4. KEY INSIGHTS\n")
        f.write("-"*40 + "\n")

        top_page = sorted_base[0][0]
        f.write(f"- {top_page} is the most influential page.\n")

        f.write("- Higher damping gives more importance to link structure.\n")
        f.write("- Lower damping increases randomness.\n")
        f.write("- Personalized PageRank shifts importance toward preferred nodes.\n")

        f.write("\n")

        f.write("END OF REPORT\n")

    print(f"✅ Report saved as {filename}")

# -----------------------------
# Pretty print matrix with labels
# -----------------------------
def print_matrix(M, pages, title="Matrix"):
    print(f"\n=== {title} ===")
    header = "       " + " ".join([f"{p[:6]:>8}" for p in pages])
    print(header)

    for i, row in enumerate(M):
        row_str = " ".join([f"{val:8.3f}" for val in row])
        print(f"{pages[i][:6]:>6} {row_str}")


# -----------------------------
# Check if matrix is stochastic
# -----------------------------
def check_stochastic(M, tol=1e-6):
    col_sums = M.sum(axis=0)
    print("\nColumn sums:", col_sums)

    if np.allclose(col_sums, np.ones_like(col_sums), atol=tol):
        print("✅ Matrix is column-stochastic")
    else:
        print("❌ Matrix is NOT column-stochastic")


# -----------------------------
# Detect dangling nodes
# -----------------------------
def find_dangling_nodes(M, pages):
    dangling = []
    col_sums = M.sum(axis=0)

    for i, s in enumerate(col_sums):
        if np.isclose(s, 0):
            dangling.append(pages[i])

    return dangling


# -----------------------------
# Normalize vector (safety)
# -----------------------------
def normalize(v):
    total = np.sum(v)
    if total == 0:
        return v
    return v / total


# -----------------------------
# Compare two rank vectors
# -----------------------------
def compare_ranks(pages, r1, r2, label1="A", label2="B"):
    print(f"\n=== Rank Comparison: {label1} vs {label2} ===")
    for i, p in enumerate(pages):
        print(f"{p:10} | {label1}: {r1[i]:.4f} | {label2}: {r2[i]:.4f}")


# -----------------------------
# Sort and print rankings
# -----------------------------
def print_sorted_ranks(pages, ranks, title="Final Rankings"):
    print(f"\n=== {title} ===")
    results = list(zip(pages, ranks))
    results.sort(key=lambda x: x[1], reverse=True)

    for i, (p, score) in enumerate(results, 1):
        print(f"#{i:2d} {p:10} → {score:.6f}")


# -----------------------------
# Difference between iterations
# -----------------------------
def compute_diff(history):
    diffs = []
    for i in range(1, len(history)):
        diff = np.linalg.norm(history[i] - history[i-1], 1)
        diffs.append(diff)
    return diffs