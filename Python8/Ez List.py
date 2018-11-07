""""Apipu"""
def main():
    """Main function"""
    list_number = list()
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            list_number.append(num)
    print(list_number)
    list_number = sorted(list_number)
    print(list_number)
    list_number.sort()
    list_number.reverse()
    print(list_number)
    print(list_number.pop(2))
    print(list_number)
    list_number.clear()
    print(list_number)
main()
