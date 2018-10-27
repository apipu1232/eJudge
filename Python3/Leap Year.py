"""Apipu"""
def main():
    """Main function"""
    year = int(input())
    if year % 400 == 0:
        print("%d is a leap year." %year)
    elif year % 100 == 0:
        print("%d is not a leap year." %year)
    elif year % 4 == 0:
        print("%d is a leap year." %year)
    else:
        print("%d is not a leap year." %year)
main()