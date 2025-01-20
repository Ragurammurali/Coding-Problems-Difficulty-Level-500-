- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TALLER 
- Difficulty: 281

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if(X>Y):
        print("A")
    elif(Y>X):
        print("B")
