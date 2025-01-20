- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PARLIAMENT
- Difficulty: 419

Code:
T=int(input())
for i in range(T):
    N,X=map(int,input().split())
    if(X>=N/2):
        print("YES")
    elif(X<N/2):
        print("NO")
