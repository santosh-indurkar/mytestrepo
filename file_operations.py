"""File operations"""

f_name = "f1.txt"


def read_file(file):
    # 1 : Open a file and read as string
    f = open(file)
    print("Reading file at once")
    print(f.read())

    # 2 : Open a file and read line by line
    print("Reading the given file line by line")
    f.seek(0)
    for line in f.readlines():
        print(line)
    f.close()


# 3 : Open a file and append a string
def append_file(file):
    f = open(file, "a")
    f.write("Appending this line ...\n")
    f.close()


# 4 : Open a file using "with"
def read_file_with(file):
    with open(file) as f:
        print(f.read())


read_file(f_name)
append_file(f_name)
read_file_with(f_name)
