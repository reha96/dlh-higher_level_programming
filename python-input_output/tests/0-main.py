"""tester file"""
import os


os.system('clear')
print("--"*10)
print("tester 0")
print("--"*5 + "pycode" + "--"*5)
os.system("pycodestyle 0-read_file.py")
print("--"*5 + "pycode" + "--"*5)

read_file = __import__('0-read_file').read_file

read_file("tests/my_file_0.txt")