"""Apipu"""
def main():
    """Main Function"""
    text = input()
    text = text.replace("1", "2")
    text = text.replace("0", "1")
    text = text.replace("2", "0")
    print(text)
main()
