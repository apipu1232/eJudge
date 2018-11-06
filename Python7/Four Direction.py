"""Apipu"""
def main(text):
    """Main function"""
    print(direct(text))
def direct(text):
    """direction"""
    text1, text2, text3, text4, text5 = "", "", "", "", ""
    dic = {
        "N": ["  *   ", " ***  ", "* * * ", "  *   ", "  *   "], \
        "E": ["  *   ", "   *  ", "***** ", "   *  ", "  *   "], \
        "S": ["  *   ", "  *   ", "* * * ", " ***  ", "  *   "], \
        "W": ["  *   ", " *    ", "***** ", " *    ", "  *   "], \
    }
    for i in text:
        if i in dic:
            text1 += dic[i][0]
            text2 += dic[i][1]
            text3 += dic[i][2]
            text4 += dic[i][3]
            text5 += dic[i][4]
    text1 += "\n" + text2 + "\n" + text3 + "\n" + text4 + "\n" + text5
    return text1
main(input())
