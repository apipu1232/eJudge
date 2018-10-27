"""Apipu"""
def main(num):
    """Main Function"""
    for i in range(num):
        print((i + 1) * "*" + " " * (num - i - 1) + "*" * (num - i))
    for i in range(num):
        print(" " * (num -i -1) + "*" * (i + 1) + " " * i + "*" * (num -i))
main(int(input()))
