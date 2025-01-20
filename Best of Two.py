- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BESTOFTWO 
- Difficulty: 284

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if(X>Y):
        print(X)
    elif(Y>X):
        print(Y)
    elif(X==Y):
        print(X)
