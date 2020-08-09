"""String manipulation/operations"""

my_string = "Learning DevOps"


def string_manipulations(string):
    # 1 : String slicing examples
    print("String slice from index 1 to index 3, not including index 3 : {}".format(string[1:3]))
    print("String slice excluding 1st char : {}".format(string[1:]))
    print("String slice containing entire string : {}".format(string[:]))
    print("String slice from 0th index to 5th, not including index 5 : {}".format(string[:5]))
    print("String slice in reverse order : {}".format(string[::-1]))

    # 2 : Build-In
    print("Length of given string : {}".format(len(my_string)))
    print("List of string char in sorted : {}".format(sorted(my_string)))
    print("".join([r for r in reversed(my_string)]))
    print("String in lower case : {}".format(my_string.lower()))
    print("String in upper case : {}".format(my_string.upper()))
    print("String with capitalization : {}".format(my_string.capitalize()))
    print("String with swap case : {}".format(my_string.swapcase()))
    print("True if string starts with '{}' : {}".format("Lear", my_string.startswith("Lear")))
    print("True if string ends with '{}' : {}".format("DevOps", my_string.endswith("DevOps")))
    print("Replace 'DevOps' with 'Ansible' : {}".format(my_string.replace("DevOps", "Ansible")))
    print("Finds the index for 'DevOps' : {}".format(my_string.find("DevOps")))
    print("Counts the number of occurrences of 'DevOps' : {}".format(my_string.count("DevOps")))
    print("Splits the string with ' ' and returns the list : {}".format(my_string.split(" ")))


string_manipulations(my_string)
