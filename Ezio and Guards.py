- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MANIPULATE
- Difficulty: 427

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if(X>=Y):
        print("YES")
    elif(X!=Y):
        print("NO")
    elif(X<Y):
        print("NO")
