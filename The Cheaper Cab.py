- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CABS 
- Difficulty: 399

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if(X<Y):
        print("FIRST")
    elif(Y<X):
        print("SECOND")
    elif(X==Y):
        print("ANY")
