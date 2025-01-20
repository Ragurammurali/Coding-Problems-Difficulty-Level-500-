- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TOP10 
- Difficulty: 255 

Code:
T=int(input())
top=10
for i in range(T):
    X=int(input())
    if(X>top):
        print("NO")
    elif(X<=top):
        print("YES")
    
