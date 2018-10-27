"""Apipu"""
def main(text):
    """Main function"""
    text = text.split(".")
    print("_|_ " * len(text))
    max_len = 0
    for i in range(len(text)):
        if len(text[i]) > max_len:
            max_len = len(text[i])
    for i in range(len(text)):
        text[i] = text[i].ljust(max_len)
    for i in range(max_len):
        for j in range(len(text)):
            print("|", end="")
            print(text[j][i], end="")
            print("|", end=" ")
        print()
    print("|_| " * len(text))


main(input())
