"""Apipu"""
def main():
    """Main function"""
    num = int(input())
    print("0" * (0 <= num <= 49) + "1" * (50 <= num <= 54) + "1.5" * (55 <= num <= 59)\
        + "2" * (60 <= num <= 64) + "2.5" * (65 <= num <= 69) + "3" * (70 <= num <= 74)\
        + "3.5" * (75 <= num <= 79) + "4" * (80 <= num <= 100) \
        + "Invalid" * (num < 0 or num > 100))
main()