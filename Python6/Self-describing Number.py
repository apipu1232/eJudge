"""Apipu"""
def main():
    """Main function"""
    num = input().strip('"')
    check = ""
    for i in range(len(num)):
        if i <= 9:
            check += str(num.count(str(i)))
        if i > 9:
            check += "0"
    if check == num:
        print("YES")
    else:
        print("NO")
main()
