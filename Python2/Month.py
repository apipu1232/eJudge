"""Apipu"""
def main():
    """Main Function"""
    num = int(input())
    month = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec"
    month2 = month.split(" ")
    print(month2[num-1])
main()