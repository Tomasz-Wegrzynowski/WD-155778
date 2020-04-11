def parzyste(data):
    for index in range(0, len(data)-1, 2):
        yield data[index]

slowo = parzyste("abcdef")

for element in slowo:
    print(element)