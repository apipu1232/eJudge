"""Apipu"""
import math
def main():
    """Main Function"""
    d_1 = int(input())
    d_2 = int(input())
    r_1 = d_1 / 2
    r_2 = d_2 / 2
    area = int((math.pi * r_1 ** 2) - (math.pi * r_2 ** 2))
    cir = int(math.pi * d_1 + math.pi * d_2)
    print(area)
    print(cir)
main()
