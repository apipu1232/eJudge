"""Apipu"""
def main(music):
    """Main Function"""
    music = music.split(", ")
    music_1 = []
    for i in music:
        music_2 = [music_1[i].lower() for i in range(len(music_1))]
        if not i.lower() in music_2:
            music_1.append(i)
            music_2.append(i)
    music_1.sort(key=len, reverse=True)
    for i in range(len(music_1)):
        print("{0}.{1}".format(i + 1, music_1[i]))
main(input())
