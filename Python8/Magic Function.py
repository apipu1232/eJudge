""""Apipu"""
def main(num_x):
    """Main function"""
    if num_x == 1:
        print(1)
    while num_x != 1:
        if num_x % 2 == 0:
            num_x /= 2
            print(int(num_x))
        else:
            num_x += 1
            print(int(num_x))
main(int(input()))
