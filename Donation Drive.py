- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DONDRIVE 
- Difficulty: 272 

Code:
T=int(input())
for i in range(T):
    N,X=map(int,input().split())
    remaining_donations=N-X
    print(remaining_donations)
