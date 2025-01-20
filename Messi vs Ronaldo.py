- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MVR 
- Difficulty: 316

Code:
A,B,X,Y=map(int,input().split())
m=2*A+1*B 
r=2*X+1*Y 
if(m>r):
    print("Messi")
elif(r>m):
    print("Ronaldo")
elif(m==r):
    print("Equal")
