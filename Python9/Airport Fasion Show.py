"""Apipu"""
def main(text, time):
    """Main function"""
    if "am" in time:
        time = time.replace("am", "")
        time1 = 0
    else:
        time = time.replace("pm", "")
        time1 = 720
    time = time.split(":")
    hour = int(time[0])
    minute = int(time[1])
    time1 += minute + (hour%12) * 60
    dic = {"A":160, "B":140, "C":115}
    time1 -= dic[text]
    if time1 >= 720 or time1 < 0:
        mmm = "pm"
    else:
        mmm = "am"
    hour = (time1 % 720) // 60
    if hour == 0:
        hour = 12
    minute = time1 % 60
    print("{0:02d}:{1:02d}{2}".format(hour, minute, mmm))
main(input(), input())
