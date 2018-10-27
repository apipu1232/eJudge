"""Apipu"""
def main():
    """Main function"""
    text1, text2, text3, text4, text5 = "|", "|", "|", "|", "|"
    dic = {
        "N": ["  A  |", " AAA |", "A A A|", "  A  |", "  A  |"], \
        "E": ["  A  |", "   A |", "AAAAA|", "   A |", "  A  |"], \
        "S": ["  A  |", "  A  |", "A A A|", " AAA |", "  A  |"], \
        "W": ["  A  |", " A   |", "AAAAA|", " A   |", "  A  |"], \
        "NE": [" AAAA|", "   AA|", "  A A|", " A  A|", "A    |"], \
        'SE': ["A    |", " A  A|", "  A A|", "   AA|", " AAAA|"], \
        'SW': ["    A|", "A  A |", "A A  |", "AA   |", "AAAA |"], \
        'NW': ["AAAA |", "AA   |", "A A  |", "A  A |", "    A|"] \
    }
    count = 0
    for _ in range(3):
        text = input()
        if text in dic:
            text1 += dic[text][0]
            text2 += dic[text][1]
            text3 += dic[text][2]
            text4 += dic[text][3]
            text5 += dic[text][4]
            count += 1
    if count == 3:
        print('-------------------')
        print(text1, text2, text3, text4, text5, sep='\n')
        print('-------------------')
    else:
        print('Error 405 Guide not found')
main()
