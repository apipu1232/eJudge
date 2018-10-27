"""Apipu"""
import json
def main(set_a):
    """Main Function"""
    set_a = set_a.replace("{", "[")
    set_a = set_a.replace("}", "]")
    set_a = json.loads(set_a)
    print(2 ** len(set_a))
main(input())
