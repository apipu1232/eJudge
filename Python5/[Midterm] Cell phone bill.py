"""Apipu"""
def main(bill):
    """Main Function"""
    bill = bill.split(",")
    minute = int(bill[0])
    text = int(bill[1])
    add_call = 0
    add_text = 0
    print("Cell phone plan: $15.00")
    if minute > 50:
        add_call += (minute - 50) * 0.25
        print("Additional air time: ${0:.2f}".format(add_call))
    if text > 50:
        add_text += (text - 50) * 0.15
        print("Additional text messages: ${0:.2f}".format(add_text))
    print("911 Call center support: $0.44")
    total = (15 + add_call + add_text + 0.44) * 1.05
    print("Total: ${0:.2f}".format(total))
main(input())
