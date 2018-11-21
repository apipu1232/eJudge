"""Apipu"""
def main(text):
    """Main function"""
    num = list()
    text = text.split(",")
    for i in range(int(text[1])):
        inp = input()
        if "." in inp:
            num.append(float(inp))
        else:
            num.append(int(inp))
    new_num = list()
    for i in range(len(num)):
        minumum = num[0]
        for j in num:
            if j < minumum:
                minumum = j
        new_num.append(minumum)
        num.remove(minumum)
    if text[0] == "desc":
        new_num.reverse()
    for i in new_num:
        print(i, end=" ")
main(input())
