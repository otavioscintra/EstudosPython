#https://www.youtube.com/watch?v=1YbTDczvqco

string = 'Otávio Cintra'
number_letters = 2
new_string = '.'.join([string[indice:indice + number_letters] for indice in range(0, len(string),number_letters)])

print(new_string)