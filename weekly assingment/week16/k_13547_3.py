for t in range(1, int(input()) + 1):
    match = input()
    l = len(match)
    o = match.count("o")
    if o>=8 or l-o<8:
        print("#{} YES".format(t))
    else:
        print("#{} NO".format(t))
