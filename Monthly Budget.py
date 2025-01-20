- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BUDGET_
- Difficulty: 456

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    dailyexpenditure=Y*30
    if(X<dailyexpenditure):
        print("NO")
    elif(X>dailyexpenditure):
        print("YES")
    elif(X==dailyexpenditure):
        print("YES")
