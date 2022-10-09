import itertools

s, k = input().split()
k = int(k)
ans = list(set(itertools.permutations(s)))
ans.sort()
print("".join(ans[k - 1]))
