- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/KITCHENSPICE 
- Difficulty: 390

Code:
T=int(input())
for i in range(T):
    X=int(input())
    if(X<4):
        print("MILD")
    elif(X>=4 and X<7):
        print("MEDIUM")
    elif(X>=7):
        print("HOT")
