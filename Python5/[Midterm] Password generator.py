"""Apipu"""
def main():
    """Main Function"""
    text = input()
    times = len(text)
    text = text[::-1]
    print((text + "_") * (times - 1) + text)
main()
