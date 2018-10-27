"""Apipu"""
import math
def main(num_x):
    """Main Function"""
    num_y = 2 - num_x + 3 / 7 * num_x ** 2 - 5 / 11 * num_x ** 3 + math.log10(num_x)
    print(num_y)
main(float(input()))