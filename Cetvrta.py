axes = []
verticals = []
final_x = 0
final_y = 0
for i in range(3):
    x, y = map(int, input().split())
    axes.append(x)
    verticals.append(y)
for i in range(len(axes)):
    if axes.count(axes[i]) % 2 != 0:
        final_x = axes[i]
        break

for j in range(len(verticals)):
    if verticals.count(verticals[j]) % 2 != 0:
        final_y = verticals[j]
        break
print(f"{final_x} {final_y}")