"""Apipu"""
def main():
    """Main Function"""
    day = int(input())
    money = int(day / 2 * (2 * 3 + (day - 1) * 7))
    print(money)
main()
