- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MONOPOLY 
- Difficulty: 482

Code:
T=int(input())
for i in range(T):
    R1,R2,R3=map(int,input().split())
    sum1=R1+R2 
    sum2=R2+R3 
    sum3=R3+R1 
    if(R3>sum1):
        print("Yes")
    elif(R1>sum2):
        print("Yes")
    elif(R2>sum3):
        print("Yes")
    else:
        print("No")
