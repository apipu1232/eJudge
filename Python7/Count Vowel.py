"""Apipu"""
def main(text):
    """Main function"""
    count = 0
    for i in text:
        count += check(i)
    print(count)
def check(text):
    """Check vowel"""
    vowel = "aeiouAEIOU"
    if text in vowel:
        return True
    else:
        return False
main(input())
