- link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHESSTIME 
- Difficulty: 337

Code:
T=int(input())
for i in range(T):
    N=int(input())
    time=N*60
    max_no_of_complete_chess_games=time/20
    print(int(max_no_of_complete_chess_games))
