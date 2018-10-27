"""Apipu"""
def main(num1, num2):
    """Main function"""
    count = 0
    for i in range(num1, num2+1):
        count += int(prime(i))
    print(count)
def prime(num):
    """Check prime number"""
    if num > 1:
        for i in range(2, int(num**0.5+1)):
            if (num % i) == 0:
                return False
        return True
    else:
        return False
main(int(input()), int(input()))
