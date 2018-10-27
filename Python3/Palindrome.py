"""Apipu"""
def main():
    """Main function"""
    text = input()
    if text == text[::-1]:
        print("%s is Palindrome." %text)
    else:
        print("This is not Palindrome")
main()