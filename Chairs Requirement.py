- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHAIRS_ 
- Difficulty: 305

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if(X>Y):
        print(X-Y)
    elif(Y>X):
        print(0)
    elif(Y==X):
        print(0)
