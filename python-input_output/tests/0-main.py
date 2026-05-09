"""tester file"""
import os

os.system('clear')
print("--"*10)
print("tester 0")
print("--"*5 + "pycode" + "--"*5)
os.system("pycodestyle 0-read_file.py")
print("--"*5 + "pycode" + "--"*5)

read_file = __import__('0-read_file').read_file

try:
    read_file("tests/my_file_0.txt")
except Exception as err:
    print("[{}] {}".format(err.__class__.__name__, err))

os.system('clear')
print("--"*10)
print("tester 1")
print("--"*5 + "pycode" + "--"*5)
os.system("pycodestyle 1-write_file.py")
print("--"*5 + "pycode" + "--"*5)

write_file = __import__('1-write_file').write_file

try:
    nb_characters = write_file(
        "my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
except Exception as err:
    print("[{}] {}".format(err.__class__.__name__, err))

os.system('clear')
print("--"*10)
print("tester 1")
print("--"*5 + "pycode" + "--"*5)
os.system("pycodestyle 2-append_write.py")
print("--"*5 + "pycode" + "--"*5)

append_write = __import__('2-append_write').append_write

try:
    print("test: file does not exist")
    nb_characters_added = append_write(
        "file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
except Exception as err:
    print("[{}] {}".format(err.__class__.__name__, err))

try:
    print("test: append existing")
    os.system('rm my_first_file.txt')
    nb_characters = write_file(
        "my_first_file.txt", "This School is so cool!\n")
    nb_characters_added = append_write(
        "my_first_file.txt", "This School is so cool!\n")
    print(nb_characters_added)
except Exception as err:
    print("[{}] {}".format(err.__class__.__name__, err))
