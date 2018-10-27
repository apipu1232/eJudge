"""Apipu"""
def main():
    """Main function"""
    time = input()
    time = time.split(" ")
    hour = int(time[0])
    minute = int(time[1])
    hr_deg = hour * 30 + minute * 0.5
    min_deg = minute * 6
    if hr_deg - min_deg < 6 and hr_deg >= min_deg:
        print("True")
    else:
        print("False")
main()