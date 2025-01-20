- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/NETFLIX
- Difficulty: 493

Code:
T=int(input())
for i in range(T):
    A,B,C,X=map(int,input().split())
    sum1=A+B  
    sum2=B+C  
    sum3=C+A
    if(sum1==X):
        print("YES")
    elif(sum2==X):
        print("YES")
    elif(sum3==X):
        print("YES")
    elif(sum1>X):
        print("YES")
    elif(sum2>X):
        print("YES")
    elif(sum3>X):
        print("YES")
    else:
        print("NO")
