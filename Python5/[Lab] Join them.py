"""Apipu"""
def main(num):
    """Main Function"""
    box = []
    for _ in range(num):
        box.append(input())
    option = input()
    print(option.join(box))
main(int(input()))