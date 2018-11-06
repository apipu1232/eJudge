"""Apipu"""
def main(text):
    """Main function"""
    text = text.replace("-", "")
    for i in text:
        print(t2sp(i), end=" ")
def t2sp(text):
    """text to speech"""
    dic = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", \
    "6":"six", "7":"seven", "8":"eight", "9":"nine"}
    return dic[text]
    
main(input())
