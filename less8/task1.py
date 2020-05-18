# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?

def count_handshakes(graph):
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                count += 1
            else:
                break
    return int(count)


n = int(input('Введите число друзей: '))
g = [[1] * n for i in range(n)]
print('Матрица смежности: ')
for i in range(n):
    g[i][i] = 0
    print(g[i])
print(f'Количество рукопожатий: {count_handshakes(g)}')