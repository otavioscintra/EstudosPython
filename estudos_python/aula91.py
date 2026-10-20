# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, max=10):
    while True:
        yield n

        n += 1

        if n > max:
            return
        

gen = generator(n=-222, max=-11)
for n in gen:
    print(n)


