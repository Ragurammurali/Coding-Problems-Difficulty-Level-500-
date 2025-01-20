- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/POPULATION 
- Difficulty: 358

Code:
T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    total_population=(X-Y)+Z
    print(total_population)
