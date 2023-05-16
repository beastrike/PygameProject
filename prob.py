map_massiv = open('map.txt').read().split('\n')
final = []
for i in map_massiv:
    print(i)
    final.append(list(map(int, list(i))))

print(final)