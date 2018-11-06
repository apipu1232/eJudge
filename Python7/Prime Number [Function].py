"""Apipu"""
def main(num):
    """Main function"""
    if prime(num):
        print("Yes")
    else:
        print("No")
def prime(num):
    """Check prime number"""
    if num > 1:
        for i in range(2, int(num**0.5+1)):
            if (num % i) == 0:
                return False
        return True
    else:
        return False
main(int(input()))
