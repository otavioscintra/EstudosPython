#https://www.youtube.com/watch?v=1YbTDczvqco

# for x in range(1,11):
#     for y in range(1,6):
#         print(x,y)

lines_and_columns = [
    (x,y)
    if y != 2 else (x * 1000, y * 1000)
    for x in range(1,11)
    for y in range(1,6)
    if x != 2
] 
# print(lines_and_columns)
for n in lines_and_columns:
    print(n)