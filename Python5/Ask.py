"""Apipu"""
def main(num):
    """Main function"""
    dic = {"Walk":0, "Car":0, "Bus":0, "Airplane":0, "Warp":0, "Paradrop":0, "Helicopter":0,\
    "Dig":0, "Jetpack":0, "Fly":0, "Jump":0, "Balloon":0, "Bird":0, "Unicorn":0, "Broom":0,\
    "Rocket":0, "Kafra":0, "Water Rocket":0, "Blink":0, "E-mail":0, "Internet":0, "Banana Boat":0,\
    "Prone":0, "Sprint":0, "Dimension Door":0, "Tamiya":0, "285":0}
    for _ in range(num):
        text = input()
        dic[text] += 1
    mode = max(dic[i] for i in dic)
    if list(dic.values()).count(mode) > 1:
        print("No.")
    else:
        for name, value in dic.items():
            if value == mode:
                print(name)
main(int(input()))
