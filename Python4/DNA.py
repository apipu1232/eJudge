"""Apipu"""
def main(num):
    """Main function"""
    for i in range(num):
        for j in range(i+1):
            if j == 0:
                print(" " * num + "*")
            else:
                print((" " * (num - j)) + "*" + " " * (j * 2 -1) + "*")
        for j in range(i+1, 0, -1):
            print((" " * (num - j)) + "*" + " " * (j * 2 -1) + "*")
    print(" " * num + "*")
main(int(input()))
