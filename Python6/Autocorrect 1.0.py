"""Apipu"""
def main():
    """Main function"""
    text = input().lower()
    text_num = ["zero", "one", "two", "three",\
     "four", "five", "six", "seven", "eight", "nine"]
    for i in range(10):
        count = 0
        if len(text) == len(text_num[i]):
            for j in range(len(text)):
                if text[j] in text_num[i]:
                    count += 1
                else:
                    continue
                if count == len(text):
                    print(i)
                    break
        else:
            continue
main()
