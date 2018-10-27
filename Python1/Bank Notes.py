"""Apipu"""
def main():
    """Main Function"""
    money = int(input())
    bank800 = money // 800
    bank200 = (money % 800) // 200
    bank150 = (money % 200) // 150
    bank60 = (money % 200 % 150) // 60
    bank10 = (money % 200 % 150 % 60) // 10
    print(bank800)
    print(bank200)
    print(bank150)
    print(bank60)
    print(bank10)
main()
