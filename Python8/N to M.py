""""Apipu"""
def main():
    """Main function"""
    num_n = int(input())
    num_m = int(input())
    for i in range(num_n, num_m+1):
        print(i, end=" ")
    for i in range(num_n, num_m-1, -1):
        print(i, end=" ")
main()
