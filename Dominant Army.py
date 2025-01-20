- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DOMINANT 
- Difficulty: 488

Code:
T=int(input())
for i in range(T):
    A,B,C=map(int,input().split())
    sum1=A+B  
    sum2=B+C  
    sum3=C+A 
    if(sum1<C):
        print("YES")
    elif(sum2<A):
        print("YES")
    elif(sum3<B):
        print("YES")
    elif(sum1>C):
        print("NO")
    elif(sum2>A):
        print("NO")
    elif(sum3>B):
        print("NO")
    elif(sum1==C):
        print("NO")
    elif(sum2==A):
        print("NO")
    elif(sum3==B):
        print("NO")

