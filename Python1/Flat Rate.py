"""Apipu"""
def main():
    """Main Function"""
    car = int(input())
    down = int(input())
    year = int(input())
    interest = int((car - down) * 0.0325 * year)
    pay = int(((car - down) + interest) / (year * 12))
    print(interest)
    print(pay)
main()
