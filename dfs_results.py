output_lines = []

def log(msg=""):
    print(msg)
    output_lines.append(msg)

# ── Graph Definition (from image, alphabetical neighbour ordering) ──────────
# Directed edges read from the image:
# H -> A, H -> C, H -> G
# A -> B, A -> F, A -> D
# B -> C, B -> E, B -> F
# C -> G, C -> E
# D -> F
# F -> E
# E -> C (back to C? let's check image carefully)
# G -> (none visible as outgoing)

# From image analysis (fixed neighbour ordering - alphabetical):
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'G', 'H'],
    'D': ['F'],
    'E': ['B', 'F'],
    'F': ['A'],
    'G': ['E', 'H'],
    'H': [],
}

# DFS implementation
time_counter = [0]
color = {}       # WHITE / GRAY / BLACK
discovery = {}
finish = {}
parent = {}
edge_class = []  # (u, v, type)

def dfs_visit(u):
    color[u] = 'GRAY'
    time_counter[0] += 1
    discovery[u] = time_counter[0]

    for v in graph[u]:
        if color[v] == 'WHITE':
            parent[v] = u
            edge_class.append((u, v, 'Tree edge'))
            dfs_visit(v)
        elif color[v] == 'GRAY':
            edge_class.append((u, v, 'Back edge'))
        elif color[v] == 'BLACK':
            if discovery[u] < discovery[v]:
                edge_class.append((u, v, 'Forward edge'))
            else:
                edge_class.append((u, v, 'Cross edge'))

    color[u] = 'BLACK'
    time_counter[0] += 1
    finish[u] = time_counter[0]

# Initialize all vertices
for v in graph:
    color[v] = 'WHITE'
    parent[v] = None

# Start DFS from vertex A (then continue with unvisited in alphabetical order)
visit_order = ['A'] + sorted([v for v in graph if v != 'A'])
for v in visit_order:
    if color[v] == 'WHITE':
        dfs_visit(v)

# ── Output ──────────────────────────────────────────────────────────────────

log("=" * 65)
log("PART B: Depth-First Search (DFS) — Starting from Vertex A")
log("=" * 65)
log("\nGraph adjacency list (alphabetical neighbour ordering):")
for u in sorted(graph):
    log(f"  {u} -> {graph[u]}")

log("\n")
log("=" * 65)
log("DFS Results: Discovery and Finish Times")
log("=" * 65)
log(f"{'Vertex':<10}{'Discovery':<15}{'Finish':<15}{'Parent':<10}")
log("-" * 50)
for v in sorted(graph):
    p = parent[v] if parent[v] else "None"
    log(f"{v:<10}{discovery[v]:<15}{finish[v]:<15}{p:<10}")

log("\n")
log("=" * 65)
log("Edge Classifications")
log("=" * 65)
log(f"{'Edge (u->v)':<15}{'Classification':<20}")
log("-" * 35)
for u, v, etype in edge_class:
    log(f"  {u} -> {v:<10}  {etype}")

log("\n")
log("=" * 65)
log("Summary of Edge Types")
log("=" * 65)
from collections import Counter
counts = Counter(etype for _, _, etype in edge_class)
for etype, cnt in sorted(counts.items()):
    log(f"  {etype:<20}: {cnt}")

log("\n")
log("=" * 65)
log("Edge Type Definitions")
log("=" * 65)
log("""
  Tree edge    : Edge (u,v) where v was first discovered via u.
                 v is WHITE when first explored from u.

  Back edge    : Edge (u,v) where v is an ANCESTOR of u in DFS tree.
                 v is GRAY (still being processed) when (u,v) explored.
                 Back edges indicate CYCLES in the graph.

  Forward edge : Edge (u,v) where v is a DESCENDANT of u (not tree edge).
                 v is BLACK and d[u] < d[v].

  Cross edge   : All other edges — between different DFS subtrees.
                 v is BLACK and d[u] > d[v].
""")

# Write to file
with open("dfs_results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print("\n✅ Output saved to dfs_results.txt")
