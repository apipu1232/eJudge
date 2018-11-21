"""Apipu"""
def main(text):
    """Main function"""
    text = text.upper()
    for i in range(len(text) - 1):
        text1 = ("  " * i + text[-i-1] + " " * ((len(text) - i - 2) * 2 + 1))
        text2 = (text[-i-1] + " " * ((len(text) - i - 2) * 2 + 1))
        print(text1, end="")
        for _ in range(2):
            print(text2, end="")
        print()
    for i in range(len(text) - 1):
        print(text[-i-1], end=" ")
    for i in range(len(text)):
        print(text[i], end=" ")
    print()
    for i in range(len(text) - 1):
        text1 = ("  " * (len(text) - i - 2) + text[i+1] + " " * (i * 2 + 1))
        text2 = (text[i+1] + " " * (i * 2 + 1))
        print(text1, end="")
        for _ in range(2):
            print(text2, end="")
        print()
main(input())
