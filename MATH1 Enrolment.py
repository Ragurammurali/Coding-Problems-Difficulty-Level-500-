- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/M1ENROL 
- Difficulty: 349

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if(Y>X):
        to_be_added_seats=Y-X
        print(to_be_added_seats)
    elif(X>Y):
        print(0)
    elif(Y==X):
        print(Y-X)
