"""Apipu"""
def main():
    """Main function"""
    num = int(input())
    if 0 <= num <= 49:
        print("0")
    elif 50 <= num <= 54:
        print("1")
    elif 55 <= num <= 59:
        print("1.5")
    elif 60 <= num <= 64:
        print("2")
    elif 65 <= num <= 69:
        print("2.5")
    elif 70 <= num <= 74:
        print("3")
    elif 75 <= num <= 79:
        print("3.5")
    elif 80 <= num <= 100:
        print("4")
    else:
        print("Invalid")
main()