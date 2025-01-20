- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/RIGHTTHERE 
- Difficulty: 299 

Code:
T=int(input())
for i in range(T):
    N,X=map(int,input().split())
    if(N<X):
        print("YES")
    elif(N==X):
        print("YES")
    elif(N>X):
        print("NO")
