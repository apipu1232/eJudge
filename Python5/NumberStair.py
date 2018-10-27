"""Apipu"""
def main(num):
    """Main function"""
    num_2 = 1
    count = 0
    for i in range(1, num + 1):
        print(i, end=" ")
        count += 1
        if count == num_2:
            count = 0
            num_2 += 1
            print()
main(int(input()))
