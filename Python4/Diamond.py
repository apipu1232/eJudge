"""Apipu"""
def main(num):
    """Main function"""
    for i in range(num):
        print(" " * (num - i -1) + "*" * (2 * i + 1))
    for i in range(num - 2, -1, -1):
        print(" " * (num - i -1) + "*" * (2 * i + 1))
main(int(input()))
