n = input()
fa = 0
ba = 0
for i in range(len(n)):
    if n[i] != "a":
        fa = i
        break
for i in range(len(n) - 1, -1, -1):
    if n[i] != "a":
        ba = i
        break
new_n = n[fa : ba + 1]
mean = (ba - fa + 1) // 2
back = new_n[-1 * mean:]
if new_n[:mean] != back[::-1]:
    print("No")
elif fa > (len(n) - 1) - ba:
    print("No")
else:
    print("Yes")
