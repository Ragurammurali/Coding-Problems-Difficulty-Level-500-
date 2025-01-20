- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/HS08TEST 
- Difficulty: 410

Code:
X, Y = map(float, input().split())

if X % 5 == 0 and X + 0.50 <= Y:
    Y -= (X + 0.50)

print(f"{Y:.2f}")
