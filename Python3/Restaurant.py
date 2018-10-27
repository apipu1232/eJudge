"""Apipu"""
def main():
    """Main function"""
    menu = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    order = int(input())
    menu[order] = menu.get(order, 0) + 1
    order = int(input())
    menu[order] = menu.get(order, 0) + 1
    order = int(input())
    menu[order] = menu.get(order, 0) + 1
    order = int(input())
    menu[order] = menu.get(order, 0) + 1
    order = int(input())
    menu[order] = menu.get(order, 0) + 1
    order = int(input())
    menu[order] = menu.get(order, 0) + 1
    order = int(input())
    menu[order] = menu.get(order, 0) + 1
    order = int(input())
    menu[order] = menu.get(order, 0) + 1
    price1 = menu[1] * 69
    price2 = menu[2] * 79
    price3 = menu[3] * 85
    price4 = menu[4] * 70
    price5 = menu[5] * 80
    price6 = menu[6] * 40
    price7 = menu[7] * 15
    price8 = menu[8] * 3
    subtotal = price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8
    total = subtotal * 1.07
    subtotal = int(subtotal) + (subtotal % 1 != 0)
    total = int(total) + (total % 1 != 0)
    if menu[1] > 0:
        print("Fish and Chips (%d)  %d" %(menu[1], price1))
    if menu[2] > 0:
        print("Hamburger (%d)  %d" %(menu[2], price2))
    if menu[3] > 0:
        print("Spaghetti Carbonara (%d)  %d" %(menu[3], price3))
    if menu[4] > 0:
        print("Spaghetti Meatball (%d)  %d" %(menu[4], price4))
    if menu[5] > 0:
        print("Lasagna (%d)  %d" %(menu[5], price5))
    if menu[6] > 0:
        print("Garlic Bread (%d)  %d" %(menu[6], price6))
    if menu[7] > 0:
        print("Water (%d)  %d" %(menu[7], price7))
    if menu[8] > 0:
        print("Ice (%d)  %d" %(menu[8], price8))
    print("Subtotal %d" %subtotal)
    print("Total (VAT 7%%) %d" %total)
main()
