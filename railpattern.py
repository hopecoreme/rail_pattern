n = 8
rail_pattern = []
rail = 0
direction = 1

for i in range(71):
    rail_pattern.append(rail)
    rail += direction
    if rail == 0 or rail == n - 1:
        direction *= -1
