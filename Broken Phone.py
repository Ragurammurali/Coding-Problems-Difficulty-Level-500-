- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BROKENPHONE 
- Difficulty: 451

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if(X<Y):
        print("REPAIR")
    elif(Y<X):
        print("NEW PHONE")
    elif(X==Y):
        print("ANY")
