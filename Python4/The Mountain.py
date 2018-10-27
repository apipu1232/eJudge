"""Apipu"""
def main(num):
    """Main function"""
    first = "  O  "
    second = " OOO "
    third = "OOOOO"
    star = "  O *"
    for i in range(num):
        if (i + 1) % 3 == 0:
            print(star, end="")
        else:
            print(first, end="")
    print("")
    for _ in range(num):
        print(second, end="")
    print("")
    for _ in range(num):
        print(third, end="")
    print("")
main(int(input()))
