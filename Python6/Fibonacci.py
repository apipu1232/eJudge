"""Apipu"""
def main():
    """Main function"""
    num = int(input())
    ans_a = 0
    ans_b = 1
    for _ in range(num):
        ans_a, ans_b = ans_b, ans_a+ans_b
    print(ans_a)
main()
