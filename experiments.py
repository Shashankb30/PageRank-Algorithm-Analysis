import numpy as np
from core import pagerank

def compare_damping(M, d_values):
    results = {}
    for d in d_values:
        r, hist = pagerank(M, d=d)
        results[d] = (r, hist)
    return results


def personalized_case(M, index, focus_pages):
    v = np.zeros(len(index))
    for p in focus_pages:
        v[index[p]] = 1

    return pagerank(M, d=0.85, personalize=v)