# CST-306 Assignment — Amal K Philip

## Part A: Recursion Tree Analysis — T(n) = 3T(n/3) + n

### Recurrence Properties
- At each level, the problem splits into **3 subproblems** of size n/3
- Work done at each node of size k: **k**
- Work at level i: 3^i × (n/3^i) = **n** (constant per level)
- Total levels (including leaves): log₃(n) + 1

---

### Recursion Tree Tables

#### n = 3
| Level | # Subproblems | Subproblem Size | Cost at Level |
|-------|--------------|----------------|---------------|
| 0 | 1 | n (3) | 3 |
| 1 | 3 | n/3^1 (1) | 3 |
| 2 | 9 | n/3^2 (1) | 9 |
| **TOTAL** | | | **15** |

#### n = 9
| Level | # Subproblems | Subproblem Size | Cost at Level |
|-------|--------------|----------------|---------------|
| 0 | 1 | n (9) | 9 |
| 1 | 3 | n/3^1 (3) | 9 |
| 2 | 9 | n/3^2 (1) | 9 |
| 3 | 27 | n/3^3 (1) | 27 |
| **TOTAL** | | | **54** |

#### n = 27
| Level | # Subproblems | Subproblem Size | Cost at Level |
|-------|--------------|----------------|---------------|
| 0 | 1 | n (27) | 27 |
| 1 | 3 | n/3^1 (9) | 27 |
| 2 | 9 | n/3^2 (3) | 27 |
| 3 | 27 | n/3^3 (1) | 27 |
| 4 | 81 | n/3^4 (1) | 81 |
| **TOTAL** | | | **189** |

#### n = 81
| Level | # Subproblems | Subproblem Size | Cost at Level |
|-------|--------------|----------------|---------------|
| 0 | 1 | n (81) | 81 |
| 1 | 3 | n/3^1 (27) | 81 |
| 2 | 9 | n/3^2 (9) | 81 |
| 3 | 27 | n/3^3 (3) | 81 |
| 4 | 81 | n/3^4 (1) | 81 |
| 5 | 243 | n/3^5 (1) | 243 |
| **TOTAL** | | | **648** |

#### n = 243
| Level | # Subproblems | Subproblem Size | Cost at Level |
|-------|--------------|----------------|---------------|
| 0 | 1 | n (243) | 243 |
| 1 | 3 | n/3^1 (81) | 243 |
| 2 | 9 | n/3^2 (27) | 243 |
| 3 | 27 | n/3^3 (9) | 243 |
| 4 | 81 | n/3^4 (3) | 243 |
| 5 | 243 | n/3^5 (1) | 243 |
| 6 | 729 | n/3^6 (1) | 729 |
| **TOTAL** | | | **2187** |

---

### Summary of Estimated T(n)

| n | Estimated T(n) | n × log₃(n) | Ratio T(n)/(n·log₃n) |
|-----|---------------|-------------|----------------------|
| 3 | 15 | 3 | 5.0000 |
| 9 | 54 | 18 | 3.0000 |
| 27 | 189 | 81 | 2.3333 |
| 81 | 648 | 324 | 2.0000 |
| 243 | 2187 | 1215 | 1.8000 |

---

### Asymptotic Complexity (Theta-notation)

Using the **Master Theorem**: T(n) = aT(n/b) + f(n)

- a = 3, b = 3, f(n) = n
- Compare f(n) = n vs n^(log_b(a)) = n^(log₃3) = n^1 = n
- Since f(n) = Theta(n^log_b(a)) → **Case 2** of Master Theorem applies

> **T(n) = Theta(n log n)**

**Intuition from tree:**
- There are log₃(n) + 1 levels
- Each level costs exactly n units of work
- Total cost = n × (log₃(n) + 1) = Theta(n log n)

---

## Part B: Depth-First Search (DFS)

### Graph Definition (Alphabetical Neighbour Ordering)

| Vertex | Neighbours |
|--------|-----------|
| A | B, D |
| B | C, F |
| C | E, G, H |
| D | F |
| E | B, F |
| F | A |
| G | E, H |
| H | — |

---

### DFS Results — Discovery and Finish Times

Starting vertex: **A** | Neighbour order: **Alphabetical**

| Vertex | Discovery | Finish | Parent |
|--------|-----------|--------|--------|
| A | 1 | 16 | None |
| B | 2 | 13 | A |
| C | 3 | 12 | B |
| D | 14 | 15 | A |
| E | 4 | 7 | C |
| F | 5 | 6 | E |
| G | 8 | 11 | C |
| H | 9 | 10 | G |

---

### Edge Classifications

| Edge (u -> v) | Classification |
|---------------|---------------|
| A -> B | Tree edge |
| B -> C | Tree edge |
| C -> E | Tree edge |
| E -> B | Back edge |
| E -> F | Tree edge |
| F -> A | Back edge |
| C -> G | Tree edge |
| G -> E | Cross edge |
| G -> H | Tree edge |
| C -> H | Forward edge |
| B -> F | Forward edge |
| A -> D | Tree edge |
| D -> F | Cross edge |

### Edge Type Summary

| Type | Count |
|------|-------|
| Tree edge | 7 |
| Back edge | 2 |
| Forward edge | 2 |
| Cross edge | 2 |

> **Note:** 2 back edges (E->B, F->A) indicate the graph contains **cycles**.

---

### Edge Type Definitions

- **Tree edge**: Edge (u,v) where v was first discovered via u (v is WHITE when explored).
- **Back edge**: Edge (u,v) where v is an ancestor of u in the DFS tree (v is GRAY). Indicates a cycle.
- **Forward edge**: Edge (u,v) where v is a descendant of u but not a tree edge (v is BLACK, d[u] < d[v]).
- **Cross edge**: All other edges between different DFS subtrees (v is BLACK, d[u] > d[v]).

---

## Files

| File | Description |
|------|-------------|
| `tree_results.py` | Python program for recursion tree analysis |
| `tree_results.txt` | Output of recursion tree program |
| `dfs_results.py` | Python program for DFS traversal |
| `dfs_results.txt` | Output of DFS program |
