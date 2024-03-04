class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0

    def get_item(self, item):
        self.items.append(item)

    def inspect_item(self):
        self.inspections += 1
        item = self.items.pop(0)
        item = self.operation(item) // 3

        next_monkey = self.test(item)
        return (item, next_monkey)


class MonkeyPart2(Monkey):
    def inspect_item(self):
        # I did need some help to find out what to do in part 2
        # this is the product of all divisors used in monkey tests
        lcm = 17 * 3 * 5 * 7 * 11 * 19 * 2 * 13

        self.inspections += 1
        item = self.items.pop(0)
        item = self.operation(item) % lcm

        next_monkey = self.test(item)
        return item, next_monkey


def parse_test(lines):
    split_lines = [line.split() for line in lines]
    divisor = int(split_lines[0][-1])
    t = int(split_lines[1][-1])
    f = int(split_lines[2][-1])

    return lambda n: t if n % divisor == 0 else f


def parse_operation(line):
    # monkey 7
    if line.split()[-1] == "old":
        return lambda n: n * n

    op = line[20:]
    return lambda n: eval(str(n) + op)


def parse_input(file_name, part1=True):
    file = open(file_name)
    lines = [line.strip() for line in file.readlines()]
    file.close()

    monkeys = []

    # defining monkey parameters
    items = []
    operation = lambda: None
    test = lambda: None

    i = 0
    while i < len(lines):
        line = lines[i]
        split = line.split()

        match split[0]:
            case "Starting":
                items = [int(item.strip(",")) for item in split[2:]]
            case "Operation:":
                operation = parse_operation(line)
            case "Test:":
                test = parse_test([lines[j] for j in range(i, i + 3)])
                i += 3
                monkey = (
                    Monkey(items, operation, test)
                    if part1
                    else MonkeyPart2(items, operation, test)
                )
                monkeys.append(monkey)

        i += 1

    return monkeys


def monkey_round(monkeys):
    for monkey in monkeys:
        for _ in range(len(monkey.items)):
            item, next_monkey_index = monkey.inspect_item()
            monkeys[next_monkey_index].get_item(item)


def monkey_business(rounds, monkeys):
    for _ in range(rounds):
        monkey_round(monkeys)

    sort_monkeys = sorted([monkey.inspections for monkey in monkeys])
    return sort_monkeys[-1] * sort_monkeys[-2]


def part1():
    monkeys = parse_input("input.txt")
    return monkey_business(20, monkeys)


def part2():
    monkeys = parse_input("input.txt", False)
    return monkey_business(10000, monkeys)


print(part1())
print(part2())
