- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/READPAGES 
- Difficulty: 343

Code:
T=int(input())
for i in range(T):
    N,X,Y=map(int,input().split())
    read_pages=X*Y
    if(N<read_pages):
        print("YES")
    elif(N>read_pages):
        print("NO")
    elif(N==read_pages):
        print("YES")
