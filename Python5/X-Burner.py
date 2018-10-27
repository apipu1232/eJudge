"""Apipu"""
def main():
    """Main Function"""
    position = []
    slope = []
    while True:
        text = input()
        if text == "Finish":
            break
        position.append(text)
    for i in position:
        num_x = int(i.split(",")[0])
        num_y = int(i.split(",")[1])
        if num_x != 0:
            slope.append(num_y/num_x)
        else:
            slope.append("vertical")
    slope = list(set(slope))
    print(len(slope))
main()
