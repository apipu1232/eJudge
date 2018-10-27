"""Apipu"""
def main():
    """Main Function"""
    num = int(input())
    month = "1 January2 February3 March4 April5 May6 June7 July8 August9 September\
    10October11November12December "
    find = month.find(str(num))
    find2 = month.find(str(num + 1))
    print(month[find + 2 : find2])
main()
