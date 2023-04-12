from bishop import Bishop
from king import King
from knight import Knight
from pawn import Pawn
from queen import Queen
from rook import Rook
import stockfish as st 

stc = st.Stockfish(path="/usr/bin/stockfish")
stc.update_engine_parameters({"Hash": 1024, "UCI_Chess960": "true"})
# elo_rat = int(input("Enter The ELO Rating You Find Yourself Comfortable With : "))
stc.set_elo_rating(1000)
stc.set_depth(15)



compelete_pos_map = {}
pos_letters = ['a','b','c','d','e','f','g','h']

def print_board() :
    for i in range(8):
        print(f"{i}  ",end=" ") 
        for j in range(8):
            if compelete_pos_map[f"{pos_letters[j]}"][i] == None:
                print(" ", end="")
            else:
                print(compelete_pos_map[f"{pos_letters[j]}"][i], end=" ")
        print("\n", end=" ")
    print("\n", end="     ")
    for i in pos_letters:
        print(f"{i.upper()}",end=" ")

def change_pos(s, d):
    ch = d[0]
    num = abs(int(d[1])-1-7)

    cur_piece = compelete_pos_map[s[0]][abs(int(s[1])-1-7)]
    if cur_piece is not None:
        cur_piece.position = f"{ch}{d[1]}"
        compelete_pos_map[s[0]][abs(int(s[1])-1-7)] = None
        compelete_pos_map[ch][num] = cur_piece
        print_board()
    else:
        print("There is no piece at the starting position")

matrix = [
    [Rook("b", "a8"), Knight("b", "b8"), Bishop("b", "c8"), Queen("b", "d8"), King("b", "e8"), Bishop("b", "f8"), Knight("b", "g8"), Rook("b", "h8")],
    [Pawn("b", "a7"), Pawn("b", "b7"), Pawn("b", "c7"), Pawn("b", "d7"), Pawn("b", "e7"), Pawn("b", "f7"), Pawn("b", "g7"), Pawn("b", "h7")],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Pawn("w", "a2"), Pawn("w", "b2"), Pawn("w", "c2"), Pawn("w", "d2"), Pawn("w", "e2"), Pawn("w", "f2"), Pawn("w", "g2"), Pawn("w", "h2")],
    [Rook("w", "a1"), Knight("w", "b1"), Bishop("w", "c1"), Queen("w", "d1"), King("w", "e1"), Bishop("w", "f1"), Knight("w", "g1"), Rook("w", "h1")]
]

for i in range(8): #char
    compelete_pos_map[f"{pos_letters[i]}"] = []
    for j in range(8): #number
        compelete_pos_map[f"{pos_letters[i]}"].append(matrix[j][i])

print_board()
turn = "white"
while True :
    cur = input("Enter Your position Before change 2chars like -- >[d2] : ")
    sug_pei = compelete_pos_map[cur[0]][abs(int(cur[1])-1-7)]
    valid = []
    for i in sug_pei.move(sug_pei.position):
        if stc.is_move_correct(f"{cur}{i}"):
            valid.append(i)
        else :
            continue
    print(valid)
    dis = input("Enter Distenation : ")

    if not stc.is_move_correct(f"{cur}{dis}") :
        print("not a valid move")
        continue
    stc.make_moves_from_current_position([f"{cur}{dis}"])
    change_pos(cur,dis)
