- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PAR2 
- Difficulty: 295 

Code:
T=int(input())
for i in range(T):
    N=int(input())
    if(N%2==0):
        print("Yes")
    elif(N%2!=0):
        print("No")
    elif(N==2):
        print("Yes")
