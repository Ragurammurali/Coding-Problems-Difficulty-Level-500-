- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DOREWARD 
- Difficulty: 395

Code:
T=int(input())
for i in range(T):
    X=int(input())
    if(X<=3):
        print("BRONZE")
    elif(X>3 and X<=6):
        print("SILVER")
    elif(X>6):
        print("GOLD")
