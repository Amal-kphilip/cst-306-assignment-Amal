import math

def build_recursion_tree(n, original_n=None):
    """Build recursion tree for T(n) = 3T(n/3) + n"""
    if original_n is None:
        original_n = n
    
    levels = []
    level = 0
    current_n = n
    
    while current_n >= 1:
        num_subproblems = 3 ** level
        subproblem_size = current_n
        cost_at_level = num_subproblems * subproblem_size  # each subproblem costs n/3^level, times 3^level subproblems = n
        levels.append((level, num_subproblems, subproblem_size, cost_at_level))
        current_n = current_n / 3
        level += 1
        if current_n < 1:
            break
    
    # Add leaf level
    num_leaves = 3 ** level
    levels.append((level, num_leaves, 1, num_leaves))  # leaves cost T(1)=1 each
    
    return levels

def compute_total(levels):
    return sum(cost for _, _, _, cost in levels)

def analyze(n):
    levels = build_recursion_tree(n)
    total = compute_total(levels)
    return levels, total

def print_table(n, levels, total):
    print(f"\n{'='*70}")
    print(f"Recursion Tree for T(n) = 3T(n/3) + n,  n = {n}")
    print(f"{'='*70}")
    print(f"{'Level':<8}{'# Subproblems':<18}{'Subproblem Size':<20}{'Cost at Level':<15}")
    print(f"{'-'*70}")
    for lvl, nsub, size, cost in levels:
        size_str = f"n/3^{lvl}" if lvl > 0 else "n"
        size_val = f"({size:.4g})"
        print(f"{lvl:<8}{nsub:<18}{size_str+' '+size_val:<20}{cost:<15.4g}")
    print(f"{'-'*70}")
    print(f"{'TOTAL T(n)':<46}{total:<15.4g}")
    print(f"{'='*70}")

output_lines = []

def log(msg=""):
    print(msg)
    output_lines.append(msg)

def analyze_and_log(n):
    levels = build_recursion_tree(n)
    total = compute_total(levels)
    
    log(f"\n{'='*70}")
    log(f"Recursion Tree for T(n) = 3T(n/3) + n,  n = {n}")
    log(f"{'='*70}")
    log(f"{'Level':<8}{'# Subproblems':<18}{'Subproblem Size':<20}{'Cost at Level':<15}")
    log(f"{'-'*70}")
    for lvl, nsub, size, cost in levels:
        size_str = f"n/3^{lvl}" if lvl > 0 else "n"
        size_val = f"({size:.4g})"
        log(f"{lvl:<8}{nsub:<18}{size_str+' '+size_val:<20}{cost:<15.4g}")
    log(f"{'-'*70}")
    log(f"{'TOTAL estimated T(n)':<46}{total:<15.4g}")
    log(f"{'='*70}")
    return total

# ── Part A: Recursion Tree ──────────────────────────────────────────────────

log("=" * 70)
log("PART A: Recursion Tree Analysis for T(n) = 3T(n/3) + n")
log("=" * 70)

log("\nRecurrence: T(n) = 3T(n/3) + n")
log("  - At each level, problem splits into 3 subproblems of size n/3")
log("  - Work done at each node of size k: k")
log("  - Number of levels: log_3(n)")
log("  - Work at level i: 3^i * (n/3^i) = n  (constant per level!)")
log("  - Total levels (including leaves): log_3(n) + 1")

test_cases = [3, 9, 27, 81, 243]
totals = {}
for n in test_cases:
    totals[n] = analyze_and_log(n)

log("\n\n" + "="*70)
log("SUMMARY: Estimated T(n) for test cases")
log("="*70)
log(f"{'n':<10}{'Estimated T(n)':<20}{'n * log3(n)':<20}{'Ratio T(n)/(n*log3n)':<20}")
log("-"*70)
for n in test_cases:
    nlogn = n * math.log(n, 3)
    ratio = totals[n] / nlogn if nlogn > 0 else 0
    log(f"{n:<10}{totals[n]:<20.4g}{nlogn:<20.4g}{ratio:<20.4f}")

log("\n")
log("="*70)
log("ASYMPTOTIC COMPLEXITY (Theta-notation)")
log("="*70)
log("""
Analysis using Master Theorem:
  T(n) = aT(n/b) + f(n)
  a = 3,  b = 3,  f(n) = n

  Compare f(n) = n  vs  n^(log_b(a)) = n^(log_3(3)) = n^1 = n

  Since f(n) = Theta(n^log_b(a))  ->  Case 2 of Master Theorem applies.

  Therefore:  T(n) = Theta(n log n)

Intuition from tree:
  - There are log_3(n) + 1 levels
  - Each level costs exactly n units of work
  - Total cost = n * (log_3(n) + 1) = Theta(n log n)
""")

# Write to file
with open("tree_results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print("\n✅ Output saved to tree_results.txt")
