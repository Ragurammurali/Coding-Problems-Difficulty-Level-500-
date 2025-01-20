- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TVDISC
- Difficulty: 447

Code:
T=int(input())
for i in range(T):
    A,B,C,D=map(int,input().split())
    discountfirst=A-C
    discountSecond=B-D
    if(discountfirst<discountSecond):
        print("First")
    elif(discountSecond<discountfirst):
        print("Second")
    elif(discountfirst==discountSecond):
        print("Any")
