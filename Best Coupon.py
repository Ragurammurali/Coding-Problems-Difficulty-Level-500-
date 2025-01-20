- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHEAPFOOD
- Difficulty: 496

Code:
T=int(input())
for i in range(T):
    X=int(input())
    off=(10/100)*X  
    flat=100  
    if(off>flat):
        print(int(off))
    elif(flat>off):
        print(int(flat))
    elif(off==flat):
        print(int(off))
