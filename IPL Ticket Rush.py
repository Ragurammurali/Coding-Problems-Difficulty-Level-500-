- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/IPLTRSH 
- Difficulty: 273

Code:
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    if(N>M):
        students_who_wont_be_able_to_go=N-M
        print(students_who_wont_be_able_to_go)
    else:
        print(0)
