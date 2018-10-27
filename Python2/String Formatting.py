"""Apipu"""
def main():
    """Main Function"""
    product = input()
    price = int(input())
    weight = int(input())
    code = input()
    date = int(input())
    month = int(input())
    year = int(input())
    year_1 = int(input())
    year_2 = year + year_1
    print("Name:\t%s" %product)
    print("Price:\t%d" %price)
    print("Weight:\t%d" %weight)
    print("ID:\t%s" %code)
    print("EXP:\t%02d/%02d/%04d" %(date, month, year_2))
main()