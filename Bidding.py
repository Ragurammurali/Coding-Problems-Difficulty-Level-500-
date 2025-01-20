- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AUCTION 
- Difficulty: 330

Code:
T=int(input())
for i in range(T):
    A,B,C=map(int,input().split())
    if(A>B and A>C):
        print("Alice")
    elif(B>A and B>C):
        print("Bob")
    elif(C>A and C>B):
        print("Charlie")
