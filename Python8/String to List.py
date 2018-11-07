""""Apipu"""
def main(lis_x):
    """Main function"""
    lis_x = lis_x[1:-1].replace(" ", "")
    text = ""
    lis_y = []
    for i in lis_x:
        if i != ",":
            text += i
        else:
            lis_y.append(text)
            text = ""
    if text != "":
        lis_y.append(text)
    lis_y = [int(i) for i in lis_y]
    lis_z = []
    for i in range(len(lis_y)):
        if i % 2 != 0:
            lis_z.append(lis_y[i])
    if len(lis_z) % 2 != 0:
        lis_z.pop(len(lis_z) // 2)
    print(lis_z)
main(input())
