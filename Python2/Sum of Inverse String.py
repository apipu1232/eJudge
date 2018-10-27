"""Apipu"""
def main():
    """Main"""
    text = input()
    text2 = input()
    num = int(input())
    num2 = int(input())
    text = text[::-1]
    text2 = text2[::-1]
    print(ord(text[num-1]) + ord(text2[num2-1]))
 
main()