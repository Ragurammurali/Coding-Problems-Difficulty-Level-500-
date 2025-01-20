- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TABLETS 
- Difficulty: 376

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    Z=X*3
    if(Z<Y):
        print("YES")
    elif(Z>Y):
        print("NO")
    elif(Z==Y):
        print("YES")
