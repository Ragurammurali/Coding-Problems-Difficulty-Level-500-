- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/WAITTIME 
- Difficulty: 319

Code:
T=int(input())
for i in range(T):
    K,X=map(int,input().split())
    week=K*7
    remaining_days=week-X
    print(remaining_days)
