"""Apipu"""
import json
def main():
    """Main function"""
    fibo = json.loads(input())
    num = int(input())
    for i in range(3, num):
        next_num = fibo[i-1] + fibo[i-2] + fibo[i-3]
        fibo.append(next_num)
    print(fibo[:num])
main()
