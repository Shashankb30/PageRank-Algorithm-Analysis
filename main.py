from core import build_transition_matrix, pagerank
from experiments import compare_damping, personalized_case
from visualise import *
from utils import *
# from utils import generate_report
from report_generator import generate_general_report, save_report






pages = ["Google","YouTube","Instagram","Wikipedia",
         "Amazon","Twitter","LinkedIn","Reddit"]

links = {
    "Google":["YouTube","Wikipedia","Amazon"],
    "YouTube":["Google","Instagram"],
    "Instagram":["YouTube","Twitter"],
    "Wikipedia":["Google"],
    "Amazon":["Google","Reddit"],
    "Twitter":["Instagram"],
    "LinkedIn":[],
    "Reddit":["Twitter","Wikipedia"]
}

# Build matrix
M, index = build_transition_matrix(pages, links)

# Base PageRank
ranks, history = pagerank(M)

draw_graph(pages, links, ranks)
plot_convergence(history, pages)

# Damping experiment
results = compare_damping(M, [0.6, 0.85, 0.95])
plot_damping(results, pages)

# Personalized PageRank
r_personal, _ = personalized_case(M, index, ["Google","YouTube"])
compare_bars(ranks, r_personal, pages)

# Print matrices
print_matrix(M, pages, "Transition Matrix")

# Check correctness
check_stochastic(M)

# Find dead-ends
dangling = find_dangling_nodes(M, pages)
print("Dangling nodes:", dangling)

# Print rankings cleanly
print_sorted_ranks(pages, ranks)

# Compare experiments
compare_ranks(pages, ranks, r_personal, "Default", "Personalized")


generate_report(
    pages,
    ranks,
    results,          # damping experiments
    r_personal
)

# after computing results
results = list(zip(pages, ranks))
results.sort(key=lambda x: x[1], reverse=True)

report = generate_general_report(pages, links, results)
save_report(report)