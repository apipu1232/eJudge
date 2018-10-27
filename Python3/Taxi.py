"""Apipu"""
def main():
    """Main function"""
    dis = int(input())
    time = int(input())
    if dis > 65:
        price = 682.5 + (dis - 65) * 15
    elif 41 <= dis <= 65:
        price = 370 + (dis - 40) * 12.5
    elif 21 <= dis <= 40:
        price = 170 + (dis - 20) * 10
    elif 11 <= dis <= 20:
        price = 95 + (dis - 10) * 7.5
    elif  2 <= dis <= 10:
        price = 50 + (dis - 1) * 5
    elif 0 <= dis <= 1:
        price = 50
    price += (time // 60 + (time % 60 != 0)) * 1.5
    print(int(price) + (price % 1 != 0))
main()