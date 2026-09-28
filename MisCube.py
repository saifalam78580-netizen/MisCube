from collections import Counter

# Read 24 cube colors
colors = input().split()

# 2x2 cube:
# Top    -> 0 to 3
# Front  -> 4 to 7
# Down   -> 8 to 11
# Back   -> 12 to 15
# Left   -> 16 to 19
# Right  -> 20 to 23

# Eight corner positions
corners = [
    (0, 4, 17),    # Top-Front-Left
    (1, 5, 20),    # Top-Front-Right
    (2, 13, 16),   # Top-Back-Left
    (3, 12, 21),   # Top-Back-Right

    (8, 6, 19),    # Down-Front-Left
    (9, 7, 22),    # Down-Front-Right
    (10, 15, 18),  # Down-Back-Left
    (11, 14, 23)   # Down-Back-Right
]

# Get the three colors of every corner
corner_colors = []

for corner in corners:
    a = colors[corner[0]]
    b = colors[corner[1]]
    c = colors[corner[2]]

    # Alphabetical order
    combo = tuple(sorted([a, b, c]))
    corner_colors.append(combo)

# Count repeated corner combinations
count = Counter(corner_colors)

# Find the unusual corner combination
answer = None

for combo in corner_colors:
    if count[combo] % 2 == 1:
        answer = combo
        break

# Fallback
if answer is None:
    answer = min(count, key=count.get)

print("".join(answer))