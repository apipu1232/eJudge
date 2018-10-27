"""Apipu"""
def main(num):
    """Main Function"""
    position = []
    slope = []
    for i in range(num):
        text = input()
        position.append(text)
    for i in position:
        num_x = int(i.split(",")[0])
        num_y = int(i.split(",")[1])
        if num_x != 0:
            slope_1 = str(num_y / num_x)
            if num_x > 0 and num_y > 0:
                slope.append(slope_1+"++")
            elif num_x > 0 and num_y < 0:
                slope.append(slope_1+"+-")
            elif num_x < 0 and num_y > 0:
                slope.append(slope_1+"-+")
            elif num_x < 0 and num_y < 0:
                slope.append(slope_1+"--")
            elif num_x > 0 and num_y == 0:
                slope.append(slope_1+"+0")
            elif num_x < 0 and num_y == 0:
                slope.append(slope_1+"-0")
        else:
            if num_y > 0:
                slope.append("+")
            elif num_y < 0:
                slope.append("-")
    slope = list(set(slope))
    print(len(slope))
main(int(input()))
