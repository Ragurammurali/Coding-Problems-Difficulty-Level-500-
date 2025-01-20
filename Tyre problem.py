- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TYRE 
- Difficulty: 452

Code:
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    total=N*2+M*4
    print(total)
