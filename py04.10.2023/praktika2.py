while True:
    y = int(input())


    def is_prime(x):
        if int(x / 2) != float(x / 2) or int(x / 3) != float(x / 3):
            h = True
        else:
            h = False

        return h


    print(is_prime(y))
