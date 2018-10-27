"""Apipu"""
def main():
    """Main Function"""
    now = input()
    dur = int(input())
    month = "JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC "
    find = month.find(now)
    trav = (find + dur * 4) % 48
    print(month[trav:trav + 3])
main()
