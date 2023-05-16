for i in range(1, 501):
    n = i
    arm = 0
    while (i != 0):
        r = i % 10
        arm = arm+r*r*r
        i = i//10
    if n == arm:
        print(n, "Number is armstrong")
