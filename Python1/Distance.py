"""Apipu"""
def main():
    """Main Function"""
    me_x = int(input())
    me_y = int(input())
    ta1_x = int(input())
    ta1_y = int(input())
    ta2_x = int(input())
    ta2_y = int(input())
    dist1 = ((ta1_x - me_x) ** 2 + (ta1_y - me_y) ** 2) ** 0.5
    dist2 = ((ta2_x - ta1_x) ** 2 + (ta2_y - ta1_y) ** 2) ** 0.5
    dist = dist1 + dist2
    print("%.2f" %dist)
main()
