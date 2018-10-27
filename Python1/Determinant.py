"""Apipu"""
def main():
    """Main Function"""
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    num_e = int(input())
    num_f = int(input())
    num_g = int(input())
    num_h = int(input())
    num_i = int(input())
    detplus = num_a * num_e * num_i + num_b * num_f * num_g + num_c * num_d * num_h
    detminus = - num_g * num_e * num_c - num_h * num_f * num_a - num_i * num_d * num_b
    det = detplus + detminus
    print(det)
main()
