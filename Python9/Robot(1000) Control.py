"""Apipu"""
def main(text):
    """Main function"""
    count_x = 0
    count_y = 0
    for i in text:
        if i == "N":
            count_y += 1
        if i == "E":
            count_x += 1
        if i == "S":
            count_y -= 1
        if i == "W":
            count_x -= 1
        if i == "Z":
            count_x = 0
            count_y = 0
    print("%s %s"%(count_x, count_y))
main(input())
