- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FEVER 
- Difficulty: 348

Code:
T=int(input())
for i in range(T):
    X=int(input())
    if(X>98):
        print("YES")
    elif(X<98):
        print("NO")
    elif(X==98):
        print("NO")
