"""Apipu"""
def main():
    """Main function"""
    max_p = 0
    min_p = 10000
    max_n = ""
    while True:
        printer = input()
        if printer == "END":
            break
        printer2 = printer.split(",")
        price = int(printer2[1])
        name = printer2[0]
        allin = name.count("ALL-IN-ONE")
        if allin > 0:
            if price > max_p:
                max_p = price
                max_n = name
            if price < min_p:
                min_p = price
                min_n = name
    if max_n == "":
        print("Not found")
    else:
        print(max_n)
        print(min_n)
main()
