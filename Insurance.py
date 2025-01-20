- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INSURANCE
- Difficulty: 475

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if(Y<=X):
        print(Y)
    elif(X<=Y):
        print(X)
    elif(X==Y):
        print(X)
