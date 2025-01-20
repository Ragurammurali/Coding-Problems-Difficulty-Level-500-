- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BULLBEAR 
- Difficulty: 300 

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if(Y>X):
        print("PROFIT")
    elif(Y<X):
        print("LOSS")
    elif(Y==X):
        print("NEUTRAL")
