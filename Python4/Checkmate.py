"""Apipu"""
MY_KING = input()
MY_QUEEN = input()
ENEMY_KING = input()
NUMBER_1 = int(input())
ENEMY_PIECE = []

def check():
    """Check MY_QUEEN"""
    if int(MY_QUEEN[0]) == int(ENEMY_KING[0]) or int(MY_QUEEN[1]) == int(ENEMY_KING[1]) or \
    (abs(int(MY_QUEEN[0]) - int(ENEMY_KING[0])) == (abs(int(MY_QUEEN[1]) - int(ENEMY_KING[1])))):
        for i in range(len(ENEMY_PIECE)):
            if int(MY_QUEEN[0]) == int(ENEMY_KING[0]) == int(ENEMY_PIECE[i][0]) and \
            (int(MY_QUEEN[1]) > int(ENEMY_PIECE[i][1]) > int(ENEMY_KING[1]) \
            or int(ENEMY_KING[1]) > int(ENEMY_PIECE[i][1]) > int(MY_QUEEN[1])):
                return False
            elif int(MY_QUEEN[1]) == int(ENEMY_KING[1]) == int(ENEMY_PIECE[i][1]) and \
            (int(MY_QUEEN[0]) > int(ENEMY_PIECE[i][0]) > int(ENEMY_KING[0]) \
            or int(ENEMY_KING[0]) > int(ENEMY_PIECE[i][0]) > int(MY_QUEEN[0])):
                return False
            elif abs(int(MY_QUEEN[0]) - int(ENEMY_PIECE[i][0])) == \
            abs(int(MY_QUEEN[1]) - int(ENEMY_PIECE[i][1])):
                if (MY_QUEEN[0] > ENEMY_PIECE[i][0] > ENEMY_KING[0] \
                and MY_QUEEN[1] > ENEMY_PIECE[i][1] > ENEMY_KING[1]) \
                or (MY_QUEEN[0] > ENEMY_PIECE[i][0] > ENEMY_KING[0] \
                and ENEMY_KING[1] > ENEMY_PIECE[i][1] > MY_QUEEN[1])\
                or (ENEMY_KING[0] > ENEMY_PIECE[i][0] > MY_QUEEN[0] \
                and MY_QUEEN[1] > ENEMY_PIECE[i][1] > ENEMY_KING[1])\
                or (ENEMY_KING[0] > ENEMY_PIECE[i][0] > MY_QUEEN[0] \
                and ENEMY_KING[1] > ENEMY_PIECE[i][1] > MY_QUEEN[1]):
                    return False
            elif (int(MY_QUEEN[0]) == int(ENEMY_KING[0]) == int(MY_KING[0]) and \
            (int(MY_QUEEN[1]) > int(MY_KING[1]) > int(ENEMY_KING[1]) \
            or int(ENEMY_KING[1]) > int(MY_KING[1]) > int(MY_QUEEN[1])))\
            or (int(MY_QUEEN[1]) == int(ENEMY_KING[1]) == int(MY_KING[1]) and \
            (int(MY_QUEEN[0]) > int(MY_KING[0]) > int(ENEMY_KING[0]) \
            or int(ENEMY_KING[0]) > int(MY_KING[0]) > int(MY_QUEEN[0]))):
                return False
            elif abs(int(MY_QUEEN[0]) - int(MY_KING[0])) == \
            abs(int(MY_QUEEN[1]) - int(MY_KING[1])):
                if (MY_QUEEN[0] > MY_KING[0] > ENEMY_KING[0] \
                and MY_QUEEN[1] > MY_KING[1] > ENEMY_KING[1])\
                or (MY_QUEEN[0] > MY_KING[0] > ENEMY_KING[0] \
                and ENEMY_KING[1] > MY_KING[1] > MY_QUEEN[1])\
                or (ENEMY_KING[0] > MY_KING[0] > MY_QUEEN[0] \
                and MY_QUEEN[1] > MY_KING[1] > ENEMY_KING[1])\
                or (ENEMY_KING[0] > MY_KING[0] > MY_QUEEN[0] \
                and ENEMY_KING[1] > MY_KING[1] > MY_QUEEN[1]):
                    return False
        return True
    else:
        return False
def main():
    """Main function"""
    count = NUMBER_1
    while count > 0:
        ENEMY_PIECE.append(input())
        count -= 1
    if -1 <= int(MY_KING[0]) - int(ENEMY_KING[0]) <= 1 \
    and -1 <= int(MY_KING[1]) - int(ENEMY_KING[1]) <= 1:
        print("Checkmate")
    else:
        if check() == True:
            print("Checkmate")
        else:
            print("Defeat")
main()
