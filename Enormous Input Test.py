- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INTEST
- Difficulty: 464

Code:
(n, k) = map(int, input().split())

ans = 0

for i in range(n):
	x = int(input())
	if x % k == 0:
		ans += 1

print(ans)
