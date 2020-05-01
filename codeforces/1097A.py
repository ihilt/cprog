if __name__ == '__main__':
    card = input()
    hand = input().split()

    found = False
    for c in hand:
        if c[0] == card[0] or c[1] == card[1]:
            found = True
            break
    if found == False:
        print("NO")
    else:
        print("YES")
