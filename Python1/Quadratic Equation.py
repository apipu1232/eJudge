"""Apipu"""
def main():
    """Main function"""
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_x1 = ((- num_b) + (num_b ** 2 - 4 * num_a * num_c) ** 1 / 2) / (2 * num_a)
    num_x2 = ((- num_b) - (num_b ** 2 - 4 * num_a * num_c) ** 1 / 2) / (2 * num_a)
    total = num_x1 + num_x2
    print("%.2f" %total)
main()
