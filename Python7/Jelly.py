"""Apipu"""
def main(jelly):
    """Main function"""
    jelly = jelly.split(" ")
    jelly = [int(i) for i in jelly]
    count = 0
    while jelly != [1, 1, 1]:
        cut(jelly)
        count += 1
    print(count)
def cut(jelly):
    """cut jelly"""
    cut1 = jelly.index(max(jelly))
    jelly[cut1] = jelly[cut1] // 2
    return jelly

main(input())
