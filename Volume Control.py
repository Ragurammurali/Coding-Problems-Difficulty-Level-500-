- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/VOLCONTROL 
- Difficulty: 409

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if(X<Y):
        print(Y-X)
    elif(X>Y):
        print(X-Y)
    elif(X==Y):
        print(0)
