"""Apipu"""
def main():
    """Main Function"""
    time = int(input())
    hour = time // 3600
    minute = (time % 3600) // 60
    second = time % 60
    print(hour)
    print(minute)
    print(second)
main()
