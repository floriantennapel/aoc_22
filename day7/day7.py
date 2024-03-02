class File:
    def __init__(self, name, size=-1):
        self.name = name
        self.size = size 


class Dir(File):
    def __init__(self, name):
        super().__init__(name)
        self.contents = set()


    def add_file(self, file: File):
        for content in self.contents:
            if content.name == file.name and type(content) == type(file):
                return

        self.contents.add(file)
        file.parent = self


def size_directory(current_dir) -> int:
    '''recursively sets size of all directories'''

    size = 0
    for content in current_dir.contents:
        if type(content) == Dir and content.size == -1:
            size += size_directory(content)
        else:
            size += content.size

    current_dir.size = size
    return size
            

def parse_input(file_name) -> Dir:
    '''returns the top node of a tree structure representing file system given an input file'''

    file = open(file_name)
    lines = [line.strip() for line in file.readlines()]
    file.close()

    root = Dir('/')
    current_dir = root
    
    for line in lines:
        if line[:4] == '$ cd':
            dir_name = line[5:]
            if dir_name == '..' and current_dir.name != '/':
                current_dir = current_dir.parent
            else:
                for file in current_dir.contents:
                    if file.name == dir_name and type(file) == Dir:
                        current_dir = file
                        break
        elif line[:4] == '$ ls':
            continue
        elif line[:3] == 'dir':
            current_dir.add_file(Dir(line[4:]))
        else:
            splitted = line.split(' ') 
            size = int(splitted[0])
            name = splitted[1]
            current_dir.add_file(File(name, size=size))

    # adding directory-sizes
    size_directory(root)

    return root


def all_dirs(current_dir) -> [Dir]:
    '''returns a flat list of all directories in file system, these are found recursively'''
    dirs = [current_dir]
    for content in current_dir.contents:
        if type(content) == Dir:
            dirs += all_dirs(content)

    return dirs 
    
    

#########################################
#-Start of program-----------------------
#########################################

root = parse_input("input.txt")

def part1():
    dirs = all_dirs(root)
    return sum([dir.size for dir in dirs if dir.size <= 100000])


def part2():
    space_to_free = 30000000 - (70000000 - root.size)
    dirs = all_dirs(root)
    min = root.size

    for dir in dirs:
        size = dir.size
        if size >= space_to_free and size < min:
            min = size

    return min


print(part1())
print(part2())
