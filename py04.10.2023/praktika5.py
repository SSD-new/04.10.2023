while True:
    y = input()


    def is_palindrome(x):
        if x == x[::-1]:
            h = True
        else:
            h = False

        return h


    print(is_palindrome(y))
