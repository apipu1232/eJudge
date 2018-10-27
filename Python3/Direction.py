"""Apipu"""
def main():
    """Main function"""
    num_x = int(input())
    num_y = int(input())
    if num_x == 0 and num_y == 0:
        print("Origin")
    elif num_x == 0 and num_y > 0:
        print("North")
    elif num_x == 0 and num_y < 0:
        print("South")
    elif num_x > 0 and num_y == 0:
        print("East")
    elif num_x < 0 and num_y == 0:
        print("West")
    elif num_x > 0 and num_y > 0:
        print("Northeast")
    elif num_x > 0 and num_y < 0:
        print("Southeast")
    elif num_x < 0 and num_y > 0:
        print("Northwest")
    elif num_x < 0 and num_y < 0:
        print("Southwest")
main()