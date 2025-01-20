- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INVESTMENT 
- Difficulty: 357

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    Z=2*Y
    if(X>=Z):
        print("YES")
    elif(X<Z):
        print("NO")
