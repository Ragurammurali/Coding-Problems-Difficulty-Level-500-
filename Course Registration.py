- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/COURSEREG
- Difficulty: 470

Code:
T=int(input())
for i in range(T):
    N,M,K=map(int,input().split())
    left=M-K
    if(N>left):
        print("No")
    elif(N<left):
        print("Yes")
    elif(N==left):
        print("Yes")
