"""Apipu"""
def main(num):
    """Main function"""
    for i in range(num):
        star = "*" * (i + 1)
        space = " " * (num - i -1)
        print(space + star)
main(int(input()))
