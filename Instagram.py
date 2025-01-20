- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INSTAGRAM 
- Difficulty: 408

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    Z=10*Y
    if(X>Z):
        print("YES")
    if(X<Z):
        print("NO")
    if(X==Z):
        print("NO")
