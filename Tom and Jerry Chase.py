- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/JERRYCHASE 
- Difficulty: 298 

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if(Y>X):
        print("YES")
    elif(Y<X):
        print("NO")
    elif(Y==X):
        print("NO")
