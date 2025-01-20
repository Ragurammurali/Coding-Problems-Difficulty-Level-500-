- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PRIZEPOOL 
- Difficulty: 296

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    total=X*10+Y*90
    print(total)
