- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BATTERYLOW 
- Difficulty: 479

Code:
T=int(input())
for i in range(T):
    X=int(input())
    if(X<15):
        print("Yes")
    elif(X==15):
        print("Yes")
    elif(X>15):
        print("No")
