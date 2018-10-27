"""Apipu"""
def main(num_a, num_b):
    """Main Function"""
    num_c = num_a
    num_d = num_b
    while num_b > 0:
        num_a, num_b = num_b, num_a % num_b
    print(num_a)
    print(int(num_c * num_d / num_a))
main(int(input()), int(input()))