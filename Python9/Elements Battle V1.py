"""Apipu"""
def main(text):
    """Main function"""
    element = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", \
    "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
    dic = {"Normal":"6", "Fire":"2,8,12", "Water":"3,4", "Grass":"1,5,7,9,11", "Electric":"8", \
    "Ice":"1,6,12,16", "Fighting":"9,10,17", "Poison":"8,10", "Ground":"2,3,5", "Flying":"4,5,12",\
     "Psychic":"11,13,15", "Bug":"1,9,12", "Rock":"2,3,6,8,16", "Ghost":"13,16", \
     "Dragon":"5,14,17", "Dark":"6,11,17", "Steel":"1,6,8", "Fairy":"7,16"}
    if text not in element:
        print("Not Found")
    else:
        weak = dic[text].split(",")
        weak = [int(i) for i in weak]
        for i in weak:
            print(element[i])
main(input())
