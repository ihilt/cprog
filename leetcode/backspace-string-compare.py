def backspaceCompare(S, T):
    if S == T:
        return True
    i = 0
    while i < len(S):
        if i == 0 and S[i] == "#":
            S = S[1:]
            continue
        if S[i] == "#":
            S = S[0:i - 1] + S[i + 1:]
            i -= 2
        i += 1
        if i < 0:
            break

    i = 0
    while i < len(T):
        if i == 0 and T[i] == "#":
            T = T[1:]
            continue
        if T[i] == "#":
            T = T[0:i - 1] + T[i + 1:]
            i -= 2
        i += 1
        if i < 0:
            break

    if T != S:
        return False
    return True

if __name__ == '__main__':
    S = raw_input()
    T = raw_input()

    print(backspaceCompare(S, T))
