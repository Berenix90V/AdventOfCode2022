# https://pypi.org/project/anytree/

class Command:
    def __init__(self, string_list: list):
        self.type = string_list[1]
        self.argument = [x.strip() for x in string_list[2:]]
class Directory:
    def __init__(self, name:str, parent_dir):
        self.name = name
        self.children = {}
        self.size = 0
        self.parent = parent_dir

    def add_child(self, child, child_name):
        self.children.update({child_name: child})
    
    def update_size(self, added_size):
        self.size+=added_size
        if self.parent != None:
            self.parent.update_size(added_size)
    
    def print_dir(self, level):
        print("\t"*level, "-", self.name, "(dir", self.size, ")")
        level +=1
        for k in self.children:
            child = self.children[k]
            if isinstance(child, File):
                print("\t"*(level), "-", child.name, "(file ", child.size, ")")
            else:
                child.print_dir(level)
    
    def get_dir_less_than_size(self, size, dir_list):
        for k in self.children:
            child = self.children[k]
            if isinstance(child, Directory):
                if child.size <= size:
                    dir_list.append(child.size)
                child.get_dir_less_than_size(size, dir_list)
            

class File:
    def __init__(self, name:str, size:int, parent: Directory):
        self.name = name
        self.size = int(size.strip())
        self.parent = parent
        self.update_size(self.size)

    def update_size(self, size):
        self.parent.update_size(size)    

class Filesystem:
    def add_root(self, root:Directory):
        self.root = root
    
    def print_fs(self):
        self.root.print_dir(0)
    
    def get_dir_less_than_size(self, size):
        dir_list=[]
        self.root.get_dir_less_than_size(size, dir_list)
        return dir_list

def day7a(filepath):
    fs = Filesystem()
    cursor_position = None
    with open(filepath) as f:
        for line in f:
            if cursor_position != None:
                print(cursor_position.name)
            string_list = line.split(' ')
            string_list = [x.strip() for x in string_list]
            if string_list[0]=='$':
                cmd = Command(string_list=string_list)
                print("line is command ", cmd.type)
                if cmd.type == "cd":
                    dir_name = cmd.argument[0]
                    print(dir_name)
                    if dir_name == "/":
                        root = Directory("root", None)
                        fs.add_root(root)
                        cursor_position = root
                    elif dir_name == "..":
                        cursor_position = cursor_position.parent
                    else:
                        cursor_position = cursor_position.children[dir_name]
            else:
                if string_list[0] == "dir":
                    dir_name = string_list[1]
                    new_dir = Directory(dir_name, cursor_position)
                    cursor_position.add_child(new_dir, dir_name)
                else:
                    file_name = string_list[1]
                    file_size = string_list[0]
                    new_file = File(file_name, file_size, cursor_position)
                    cursor_position.add_child(new_file, file_name)

                print("line is list")
    fs.print_fs()
    list_dir = fs.get_dir_less_than_size(100000)
    return sum(list_dir)

print(day7a('day7_veronica.txt'))  
