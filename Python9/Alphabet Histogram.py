"""Apipu"""
def main(text):
    """Main function"""
    texts = ""
    maxx = 0
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        for j in text:
            if j == i and not j in texts:
                texts += i
                maxx = max(maxx, text.count(i))
    for i in range(maxx, 0, -1):
        line = "%2s"%str(i) + "  "
        for j in texts:
            line += "* " if text.count(j) >= i else "  "
        print(line)
    print("    ", end="")
    for i in texts:
        print(i + " ", end="")

main(input())
