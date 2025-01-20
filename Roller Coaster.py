- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MINHEIGHT 
- Difficulty: 285 

Code:
T=int(input())
for i in range(T):
    X,H=map(int,input().split())
    if(X<H):
        print("NO")
    elif(X>H):
        print("YES")
    elif(X==H):
        print("YES")
