num_of_likes = 123
for n in range(1, 6):
    if n == 1:
        print("За", n, "годинy поставили", num_of_likes * n, "лайків")
    elif n == 5:
        print("За", n, "годин поставили", num_of_likes*n, "лайків")
    else:
        print("За", n, "години поставили", num_of_likes*n, "лайків")
