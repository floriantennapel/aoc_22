file = open('input.txt')
signal = file.readline()
file.close()


def n_unique(n):
    count = n
    buffer = list(signal[:n])

    for c in signal[n:]:
        if (len(set(buffer)) == len(buffer)):
            return count
        
        buffer.pop(0)
        buffer.append(c)
        count += 1


def part1():
    return n_unique(4)


def part2():
    return n_unique(14)
    

print(part1())
print(part2())

