"""Apipu"""
def main():
    """Main function"""
    print("Welcome to OX!\n")
    lis = ["+-+-+-+", "|1|2|3|", "+-+-+-+", "|4|5|6|", "+-+-+-+", "|7|8|9|", "+-+-+-+"]
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    position_x = list()
    position_o = list()
    for i in lis:
        print(i)
    print()
    for i in range(10):
        if i == 9:
            print("Draw!!")
            break
        if i % 2 == 0:
            print("It's X's turn!")
            turn = "X"
        else:
            print("It's O's turn!")
            turn = "O"
        while True:
            inp = input("Please enter cell number (1-9) --> ")
            if inp in num:
                num.remove(inp)
                replace(lis, inp, turn)
                if turn == "X":
                    position_x.append(inp)
                else:
                    position_o.append(inp)
                break
        for i in lis:
            print(i)
        print()
        if win(position_x):
            print("The winner is X!!")
            break
        if win(position_o):
            print("The winner is O!!")
            break
def replace(lis, text, turn):
    """Replace X O"""
    if text == "1" or text == "2" or text == "3":
        lis[1] = lis[1].replace(text, turn)
    elif text == "4" or text == "5" or text == "6":
        lis[3] = lis[3].replace(text, turn)
    elif text == "7" or text == "8" or text == "9":
        lis[5] = lis[5].replace(text, turn)
def win(lis):
    """Win condition"""
    if ("1" in lis and "2" in lis and "3" in lis) or \
    ("4" in lis and "5" in lis and "6" in lis) or\
    ("7" in lis and "8" in lis and "9" in lis):
        return True
    if "1" in lis and "4" in lis and "7" in lis:
        return True
    if "2" in lis and "5" in lis and "8" in lis:
        return True
    if "3" in lis and "6" in lis and "9" in lis:
        return True
    if "1" in lis and "5" in lis and "9" in lis:
        return True
    if "3" in lis and "5" in lis and "7" in lis:
        return True
    else:
        return False
main()
