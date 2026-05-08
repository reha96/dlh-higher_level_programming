"""tester file"""
import os

task = 0
os.system('clear')
print("--"*10)
print("tester 0")
print("--"*5 + "pycode" + "--"*5)
os.system(f"pycodestyle {task}-read_file.py")
print("--"*5 + "pycode" + "--"*5)

read_file = __import__('0-read_file').read_file

try:
    read_file("tests/my_file_0.txt")
except Exception as err:
        print("[{}] {}".format(err.__class__.__name__, err))

task += 1
os.system('clear')
print("--"*10)
print("tester 1")
print("--"*5 + "pycode" + "--"*5)
os.system(f"pycodestyle {task}-write_file.py")
print("--"*5 + "pycode" + "--"*5)

write_file = __import__('1-write_file').write_file

try:
    nb_characters = write_file(
        "my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
except Exception as err:
        print("[{}] {}".format(err.__class__.__name__, err))