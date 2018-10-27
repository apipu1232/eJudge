"""Apipu"""
def main(num):
    """Main Function"""
    box = []
    for _ in range(num):
        box.append(input())
    box.insert(int(input()), input())
    print(box)
main(int(input()))