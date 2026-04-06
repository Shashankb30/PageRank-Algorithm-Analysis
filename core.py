import numpy as np

def build_transition_matrix(pages, links):
    n = len(pages)
    index = {p:i for i,p in enumerate(pages)}
    M = np.zeros((n,n))

    for page, outlinks in links.items():
        j = index[page]

        if len(outlinks) == 0:
            M[:, j] = 1/n
        else:
            prob = 1/len(outlinks)
            for dest in outlinks:
                i = index[dest]
                M[i][j] = prob

    return M, index


def pagerank(M, d=0.85, personalize=None, tol=1e-6, max_iter=100):
    n = M.shape[0]
    r = np.ones(n)/n

    if personalize is None:
        v = np.ones(n)/n
    else:
        v = personalize / np.sum(personalize)

    history = [r.copy()]

    for i in range(max_iter):
        r_new = d * M @ r + (1-d) * v
        history.append(r_new.copy())

        if np.linalg.norm(r_new - r) < tol:
            break

        r = r_new

    return r, np.array(history)