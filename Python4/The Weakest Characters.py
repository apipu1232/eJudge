"""Apipu"""
def main(letter):
    """Main function"""
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    count = text.count(letter)
    if count == 0:
        print(letter)
    else:
        index = text.index(letter)
        for i in range(index + 1):
            for j in range(index - i):
                print(" ", end="")
            for j in range(i + 1):
                print(text[j], end="")
            for j in range(i-1, -1, -1):
                print(text[j], end="")
            print()
        for i in range(index-1, -1, -1):
            for j in range(index - i):
                print(" ", end="")
            for j in range(i + 1):
                print(text[j], end="")
            for j in range(i-1, -1, -1):
                print(text[j], end="")
            print()
main(input())
