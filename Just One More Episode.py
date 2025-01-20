- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/ONEMORE 
- Difficulty:320

Code:
T=int(input())
for i in range(T):
    X=int(input())
    if(X>24):
        print("Yes")
    elif(X<24):
        print("No")
    elif(X==24):
        print("No")
