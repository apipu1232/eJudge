"""Apipu"""
def main(set_a):
    """Main Function"""
    if set_a == "{}":
        print(1)
    else:
        set_a = len(set_a.replace("{", "").replace("}", "").split(","))
        print(2 ** set_a)
main(input())
