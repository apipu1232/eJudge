"""Apipu"""
def main(num):
    """Main Function"""
    box = []
    for _ in range(num):
        box.append(int(input()))
    box.sort()
    for i in box:
        print(i)
main(int(input()))
