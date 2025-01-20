- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CWIREFRAME 
- Difficulty: 383

Code:
T=int(input())
for i in range(T):
    N,M,X=map(int,input().split())
    perimeter=2*(N+M)
    total_cost=perimeter*X
    print(total_cost)
