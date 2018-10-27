"""Apipu"""
def main():
    """Main function"""
    x_1 = float(input())
    y_1 = float(input())
    r_1 = float(input())
    x_2 = float(input())
    y_2 = float(input())
    r_2 = float(input())
    dis = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5
    if r_1 + r_2 >= dis:
        print("Yes")
    else:
        print("No")
main()