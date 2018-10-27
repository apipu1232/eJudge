"""Apipu"""
def main(text):
    """Main function"""
    text = text.split(" ")
    score = 0
    match = []
    bonus = []
    for i in text:
        if i == "X":
            match.append(10)
        else:
            for j in i:
                if j == "-":
                    match.append(0)
                elif j in "123456789":
                    match.append(int(j))
                elif j == "/":
                    match.append(10 - match[-1])
                    bonus.append(len(match) - 1)
                elif j == "X":
                    match.append(10)
    before10 = 18 - text[0:].count("X")
    for i in range(len(match)):
        if i in bonus and i < before10:
            score += match[i] + match[i+1]
        elif match[i] == 10 and i < before10:
            score += 10 + match[i+1] + match[i + 2]
        else:
            score += match[i]
    print(score)
main(input())
