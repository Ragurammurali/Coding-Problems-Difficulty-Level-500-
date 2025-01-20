- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FLOW006 
- Difficulty: 455

Code:
T=int(input())
for i in range(T):
    N=int(input())
    sum=0
    while(N!=0):
        digit=(N%10)
        sum+=digit
        N//=10
    print(sum)
