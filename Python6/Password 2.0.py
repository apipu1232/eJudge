"""Apipu"""
def main(pwd):
    """Main function"""
    if len(pwd) < 6:
        print("try again")
        pwd = input()
        if len(pwd) < 6:
            print("process terminated")
        else:
            print("Password :", "*" * len(pwd))
            print("Security score :", check(pwd))
            print("Security level :", level(check(pwd)))
    else:
        print("Password :", "*" * len(pwd))
        print("Security score :", check(pwd))
        print("Security level :", level(check(pwd)))

def check(text):
    """Count score"""
    score = ord(text[-1])
    if text.isdigit():
        score += 50
    if text.isalpha():
        score += 30
        if any(i.islower() for i in text) and any(i.isupper() for i in text):
            score += 175
        if text.islower():
            score += 100
        if text.isupper():
            score += 85
    if any(i.isdigit() for i in text) and any(i.isalpha() for i in text):
        score += 75
    if text.count(text[0]) > 4:
        score -= 15 * (text.count(text[0]) - 4)
    if len(text) > 10:
        score += 10 * (len(text) - 10)
    return score

def level(num):
    """Quality level"""
    if num < 150:
        return "poor"
    elif num < 300:
        return "acceptable"
    else:
        return "secure"
main(input())
