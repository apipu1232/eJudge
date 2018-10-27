"""Apipu"""
def main():
    """Main Function"""
    price_1 = input()
    price_2 = input()
    price_3 = input()
    num_1 = input()
    num_2 = input()
    money = 0
    if num_1 <= price_1 <= num_2:
        money += 10000
    money += 25 * (((int(num_2) - int(num_1)) // 100) + (int(num_1[-2:]) <= int(price_2))\
    + (int(num_2[-2:]) >= int(price_2)) - (int(num_2[-2:]) >= int(num_1[-2:])))
    money += 100 * (((int(num_2) - int(num_1)) // 1000) + (int(num_1[-3:]) <= int(price_3))\
    + (int(num_2[-3:]) >= int(price_3)) - (int(num_2[-3:]) >= int(num_1[-3:])))
    print(money)
main()
