for

N = int(input())
G = [[] for _ in range(N + 2)]
lst = list(map(int, input().split()))

for j in range(0, 2 * N + 2, 2):
    G[j//2].append(lst[j])
    G[j//2].append(lst[j + 1])

for line in G:
    print(* line)

bits = [0] * (N + 2)















