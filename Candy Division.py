- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CANDIVIDE 
- Difficulty: 289

Code:
T=int(input())
for i in range(T):
    N=int(input())
    if(N%3==0):
        print("YES")
    elif(N%3!=0):
        print("NO")
    elif(N==3):
        print("YES")
