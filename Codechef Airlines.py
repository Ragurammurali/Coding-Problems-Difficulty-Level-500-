- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AIRLINES 
- Difficulty: 475

Code:
T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    total_capacity=X*10
    if(Y<total_capacity):
        amount_made=Y*Z
        print(amount_made)
    elif(Y>total_capacity):
        amount_made=total_capacity*Z  
        print(amount_made)
    elif(Y==total_capacity):
        amount_made=Y*Z
        print(amount_made)
