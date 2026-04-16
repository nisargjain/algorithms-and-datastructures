"""
Pocket Cube (2x2x2) BFS Solver
================================
Representation: 24 facelets (8 corners x 3 visible faces each)
Corner i has facelets at indices 3i, 3i+1, 3i+2 for (x-face, y-face, z-face).

Corner positions (x, y, z):
  0: (0,0,0) = LDB [FIXED]    4: (0,1,0) = LUB
  1: (1,0,0) = RDB             5: (1,1,0) = RUB
  2: (1,0,1) = RDF             6: (1,1,1) = RUF
  3: (0,0,1) = LDF             7: (0,1,1) = LUF

Colors: R=0, L=1, U=2, D=3, F=4, B=5

The 3 movable faces (not containing corner 0):
  R (x=1): corners 1,2,5,6
  U (y=1): corners 4,5,6,7
  F (z=1): corners 2,3,6,7
"""

import random
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ====================================================================
# 1. STATE REPRESENTATION
# ====================================================================
# Each corner's 3 facelets get the color of the face they lie on.
# 24 values total: indices 0-2 = corner 0, indices 3-5 = corner 1, etc.

SOLVED = (
    1, 3, 5,  # corner 0 (LDB): Left=1, Down=3, Back=5
    0, 3, 5,  # corner 1 (RDB): Right=0, Down=3, Back=5
    0, 3, 4,  # corner 2 (RDF): Right=0, Down=3, Front=4
    1, 3, 4,  # corner 3 (LDF): Left=1, Down=3, Front=4
    1, 2, 5,  # corner 4 (LUB): Left=1, Up=2, Back=5
    0, 2, 5,  # corner 5 (RUB): Right=0, Up=2, Back=5
    0, 2, 4,  # corner 6 (RUF): Right=0, Up=2, Front=4
    1, 2, 4,  # corner 7 (LUF): Left=1, Up=2, Front=4
)

# ====================================================================
# 2. MOVE DEFINITIONS (index permutations)
# ====================================================================
# Each move is a list of 24 indices.
# move[i] = j means: new_state[i] = old_state[j]
#
# When rotating the R face CW (looking from +x), corners cycle: 5 -> 1 -> 2 -> 6 -> 5
# The x-face sticker stays on x-face, but y and z facelets swap axes.
# Example: corner 5 (indices 15,16,17) moves to position 1 (indices 3,4,5)
#   new[3] = old[15]  (x-face stays x-face)
#   new[4] = old[17]  (z-face becomes y-face, SWAPPED)
#   new[5] = old[16]  (y-face becomes z-face, SWAPPED)

# R face (x=1) CW: cycle 5 -> 1 -> 2 -> 6 -> 5
R_CW  = [0,1,2, 15,17,16, 3,5,4, 9,10,11, 12,13,14, 18,20,19, 6,8,7, 21,22,23]
R_CCW = [0,1,2, 6,8,7, 18,20,19, 9,10,11, 12,13,14, 3,5,4, 15,17,16, 21,22,23]

# U face (y=1) CW: cycle 4 -> 5 -> 6 -> 7 -> 4
U_CW  = [0,1,2, 3,4,5, 6,7,8, 9,10,11, 23,22,21, 14,13,12, 17,16,15, 20,19,18]
U_CCW = [0,1,2, 3,4,5, 6,7,8, 9,10,11, 17,16,15, 20,19,18, 23,22,21, 14,13,12]

# F face (z=1) CW: cycle 2 -> 3 -> 7 -> 6 -> 2  (looking from +z)
F_CW  = [0,1,2, 3,4,5, 19,18,20, 7,6,8, 12,13,14, 15,16,17, 22,21,23, 10,9,11]
F_CCW = [0,1,2, 3,4,5, 10,9,11, 22,21,23, 12,13,14, 15,16,17, 7,6,8, 19,18,20]

MOVES = [R_CW, R_CCW, U_CW, U_CCW, F_CW, F_CCW]
MOVE_NAMES = ["R", "R'", "U", "U'", "F", "F'"]

# ====================================================================
# 3. HELPER: APPLY MOVE
# ====================================================================
# Uses bytes for fast hashing (3.7M entries in the visited set)

def apply_move(state, move):
    return bytes(state[m] for m in move)

# ====================================================================
# 4. SANITY CHECKS
# ====================================================================

def apply_move_tuple(state, move):
    return tuple(state[move[i]] for i in range(24))

print("Sanity check: each CW move applied 4 times should return to start...")
for name, move in zip(["R", "U", "F"], [R_CW, U_CW, F_CW]):
    s = SOLVED
    for _ in range(4):
        s = apply_move_tuple(s, move)
    assert s == SOLVED, f"{name} failed 4-fold test!"
    print(f"  {name}^4 = identity  OK")

print("Sanity check: CW then CCW should return to start...")
for name, cw, ccw in zip(["R", "U", "F"], [R_CW, U_CW, F_CW], [R_CCW, U_CCW, F_CCW]):
    s = apply_move_tuple(SOLVED, cw)
    s = apply_move_tuple(s, ccw)
    assert s == SOLVED, f"{name} CW/CCW failed!"
    print(f"  {name} * {name}' = identity  OK")

# ====================================================================
# 5. BFS FUNCTION
# ====================================================================

def run_bfs(start_state, label):
    """
    Run BFS from start_state, exploring the full connected component.
    Returns a list where level_sizes[i] = number of configs at distance i.
    """
    visited = set()
    visited.add(start_state)
    frontier = [start_state]
    level = 0
    level_sizes = []  # <--- THIS is what gets returned as solved_levels / scrambled_levels

    t0 = time.time()
    while frontier:
        level_sizes.append(len(frontier))
        total = len(visited)
        elapsed = time.time() - t0
        print(f"  [{label}] Level {level:2d}: {len(frontier):>10,} configs | "
              f"cumulative: {total:>10,} | {elapsed:.1f}s")

        next_frontier = []
        for state in frontier:
            for move in MOVES:
                new_state = apply_move(state, move)
                if new_state not in visited:
                    visited.add(new_state)
                    next_frontier.append(new_state)

        level += 1
        frontier = next_frontier

    elapsed = time.time() - t0
    print(f"  [{label}] Done: {len(visited):,} configs, diameter = {level - 1}, "
          f"time = {elapsed:.1f}s\n")
    return level_sizes  # <--- returned here

# ====================================================================
# 6. RUN BFS FROM SOLVED STATE
# ====================================================================

print("\n" + "=" * 60)
print("BFS from SOLVED state:")
print("=" * 60)
solved_levels = run_bfs(bytes(SOLVED), "SOLVED")  # <--- assigned here

# ====================================================================
# 7. RUN BFS FROM A RANDOM SCRAMBLED STATE
# ====================================================================

# Scramble by applying 50 random moves
random.seed(42)
scrambled = bytes(SOLVED)
moves_applied = []
for _ in range(50):
    idx = random.randint(0, 5)
    scrambled = apply_move(scrambled, MOVES[idx])
    moves_applied.append(MOVE_NAMES[idx])

print("=" * 60)
print(f"Scramble: {' '.join(moves_applied)}")
print("BFS from SCRAMBLED state:")
print("=" * 60)
scrambled_levels = run_bfs(scrambled, "SCRAMBLED")  # <--- assigned here

# ====================================================================
# 8. SIDE-BY-SIDE COMPARISON TABLE
# ====================================================================

max_depth = max(len(solved_levels), len(scrambled_levels))

print("=" * 60)
print("SIDE-BY-SIDE COMPARISON")
print("=" * 60)
print(f"{'Level':>6} {'From Solved':>14} {'From Scrambled':>16} {'Difference':>12}")
print("-" * 50)
for i in range(max_depth):
    s = solved_levels[i] if i < len(solved_levels) else 0
    r = scrambled_levels[i] if i < len(scrambled_levels) else 0
    diff = r - s
    sign = "+" if diff > 0 else ""
    print(f"{i:>6} {s:>14,} {r:>16,} {sign}{diff:>11,}")

print(f"\n  Solved total:    {sum(solved_levels):,}")
print(f"  Scrambled total: {sum(scrambled_levels):,}")
print(f"  Same total? {sum(solved_levels) == sum(scrambled_levels)}")
print(f"  Solved diameter:    {len(solved_levels) - 1}")
print(f"  Scrambled diameter: {len(scrambled_levels) - 1}")
print(f"  Upper bound (7! * 3^7): {7*6*5*4*3*2*1 * 3**7:,}")
print(f"  Ratio: {7*6*5*4*3*2*1 * 3**7 / sum(solved_levels):.1f}")

# ====================================================================
# 9. PLOTTING
# ====================================================================

# Pad shorter list with zeros for aligned plotting
while len(solved_levels) < max_depth:
    solved_levels.append(0)
while len(scrambled_levels) < max_depth:
    scrambled_levels.append(0)

levels = list(range(max_depth))

fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# --- Left plot: side-by-side bars ---
ax = axes[0]
width = 0.35
ax.bar([l - width / 2 for l in levels], solved_levels, width,
       label='From Solved', color='#4C72B0', edgecolor='#2c4a7c', linewidth=0.5)
ax.bar([l + width / 2 for l in levels], scrambled_levels, width,
       label='From Scrambled', color='#DD8452', edgecolor='#9e5c35', linewidth=0.5)
ax.set_xlabel('BFS Level (distance from start)', fontsize=12)
ax.set_ylabel('Configurations at this level', fontsize=12)
ax.set_title('Configs per Level: Solved vs Scrambled Start', fontsize=13, fontweight='bold')
ax.set_xticks(levels)
ax.legend(fontsize=11)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(
    lambda x, _: f'{x/1e6:.1f}M' if x >= 1e6 else f'{x/1e3:.0f}K' if x >= 1e3 else f'{int(x)}'))

# --- Right plot: cumulative ---
ax = axes[1]
cum_solved = []
cum_scrambled = []
s, r = 0, 0
for i in range(max_depth):
    s += solved_levels[i]
    r += scrambled_levels[i]
    cum_solved.append(s)
    cum_scrambled.append(r)

ax.plot(levels, cum_solved, 'o-', color='#4C72B0', linewidth=2, markersize=5,
        label='From Solved')
ax.plot(levels, cum_scrambled, 's--', color='#DD8452', linewidth=2, markersize=5,
        label='From Scrambled')
ax.axhline(y=3674160, color='gray', linestyle=':', alpha=0.5, label='Total: 3,674,160')
ax.set_xlabel('BFS Level (distance from start)', fontsize=12)
ax.set_ylabel('Cumulative configurations', fontsize=12)
ax.set_title('Cumulative BFS: Both Start Points', fontsize=13, fontweight='bold')
ax.set_xticks(levels)
ax.legend(fontsize=10)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(
    lambda x, _: f'{x/1e6:.1f}M' if x >= 1e6 else f'{x/1e3:.0f}K' if x >= 1e3 else f'{int(x)}'))

# Key insight annotation
insight = (
    f"Same total configs: {sum(solved_levels):,}\n"
    f"Diameter (God's number): {len(solved_levels) - 1}\n"
    f"= 11,022,480 / 3"
)
ax.text(0.02, 0.55, insight, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('pocket_cube_comparison.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nPlot saved as pocket_cube_comparison.png")