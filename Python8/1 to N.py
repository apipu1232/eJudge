""""Apipu"""
def main(num_n, num_m):
    """Main function"""
    num = 1
    while num < num_n:
        print("{0:.1f}".format(num), end=" ")
        num += num_m
main(int(input()), float(input()))
