while True:
    y = input()


    def count_vowels(x):
        t = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
        return x.count(t[0]) + x.count(t[1]) + x.count(t[2]) + x.count(t[3]) + x.count(t[4]) + x.count(t[5]) + x.count(
            t[6]) + x.count(t[7]) + x.count(t[8]) + x.count(t[9])


    print(count_vowels(y))