- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/RAINFALL1 
- Difficulty: 328

Code:
T=int(input())
for i in range(T):
    X=int(input())
    if(X<3):
        print("LIGHT")
    elif(X>=3 and X<7):
        print("MODERATE")
    elif(X>=7):
        print("HEAVY")
