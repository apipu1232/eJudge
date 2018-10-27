"""Apipu"""
def main(set_a, set_b):
    """Main Function"""
    if set_a != "{}":
        set_a = set_a[1:-1].split(",")
    else:
        set_a = []
    if set_b != "{}":
        set_b = set_b[1:-1].split(",")
    else:
        set_b = []
    set_a = [int(i) for i in set_a]
    set_b = [int(i) for i in set_b]
    set_a = set(set_a)
    set_b = set(set_b)
    union = set_a.union(set_b)
    intersect = set_a.intersection(set_b)
    print(union)
    print(intersect)
main(input(), input())