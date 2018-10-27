"""Apipu"""
def main(num):
    """Main function"""
    score = list()
    for _ in range(num):
        check = [0]
        length = int(input())
        script = input()
        text = input()
        for i in range(length):
            if script[i] == text[i]:
                check.append(check[i]+1)
            else:
                check.append(0)
        score.append(sum(check))
    for i in score:
        print(i)
main(int(input()))
