""""Apipu"""
def main(num_n, num_m):
    """Main function"""
    for i in range(num_n):
        print("Line {0}: ".format(i+1), end="")
        for j in range(num_m):
            print((j+1)%10, end="")
        print()
main(int(input()), int(input()))