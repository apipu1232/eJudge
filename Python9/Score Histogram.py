"""Apipu"""
def main(text):
    """Main function"""
    text = text.split(",")
    text = [float(i) for i in text]
    for i in range(10):
        print("{0}-{1}:{2}".format(i, i+1, "|"*check(text, i, i+1)))
def check(lis, start, stop):
    """Check if i in range"""
    count = 0
    for i in lis:
        if start < i <= stop:
            count += 1
        if i == 0 and start == 0:
            count += 1
    return count
main(input())
