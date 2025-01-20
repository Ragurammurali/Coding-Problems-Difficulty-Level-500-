- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MANAPTS 
- Difficulty: 327

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if(X<Y):
        print(int(Y/X))
    elif(X>Y):
        print(0)
    elif(X==Y):
        print(int(Y/X))
