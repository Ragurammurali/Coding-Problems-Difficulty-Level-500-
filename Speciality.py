- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SPECIALITY
- Difficulty: 434

Code:
T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    if(X>Y and X>Z):
        print("Setter")
    elif(Y>X and Y>Z):
        print("Tester")
    elif(Z>X and Z>Y):
        print("Editorialist")
