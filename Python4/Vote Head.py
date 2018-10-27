"""Apipu"""
def main(num):
    """Main function"""
    vote = {1:0, 2:0, 0:0}
    count = num
    while count > 0:
        vote1 = int(input())
        if vote1 not in vote:
            pass
        vote[vote1] += 1
        count -= 1
        if vote1 != 0:
            vote[0] -= vote[0]
        if vote[0] == 3:
            break
        elif vote[1] > num / 2 or vote[2] > num / 2:
            break
    if vote[0] == 3:
        print("Vote is Voided.")
    elif ((vote[1] <= num / 2) and (vote[2] <= num / 2)) or (vote[1] == vote[2]):
        print("No Winner.")
    elif vote[1] > vote[2]:
        print("Winner is A.")
    else:
        print("Winner is B.")
main(int(input()))
