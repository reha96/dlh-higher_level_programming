"""tester file"""

import os

os.system("clear")
print("--" * 10)
print("tester 0-read_file.py")
print("--" * 5 + "pycode" + "--" * 5)
os.system("pycodestyle 0-read_file.py")
print("--" * 5 + "pycode" + "--" * 5)

read_file = __import__("0-read_file").read_file

try:
    read_file("tests/my_file_0.txt")
except Exception as err:
    print("[{}] {}".format(err.__class__.__name__, err))

os.system("clear")
print("--" * 10)
print("tester 1-write_file.py")
print("--" * 5 + "pycode" + "--" * 5)
os.system("pycodestyle 1-write_file.py")
print("--" * 5 + "pycode" + "--" * 5)

write_file = __import__("1-write_file").write_file

try:
    nb_characters = write_file(
        "my_first_file.txt", "This School is so cool!\n"
    )
    print(nb_characters)
except Exception as err:
    print("[{}] {}".format(err.__class__.__name__, err))

os.system("clear")
print("--" * 10)
print("tester 2-append_write.py")
print("--" * 5 + "pycode" + "--" * 5)
os.system("pycodestyle 2-append_write.py")
print("--" * 5 + "pycode" + "--" * 5)

append_write = __import__("2-append_write").append_write

try:
    print("test: file does not exist")
    nb_characters_added = append_write(
        "file_append.txt", "This School is so cool!\n"
    )
    print(nb_characters_added)
except Exception as err:
    print("[{}] {}".format(err.__class__.__name__, err))

try:
    print("test: append existing")
    os.system("rm my_first_file.txt")
    nb_characters = write_file(
        "my_first_file.txt", "This School is so cool!\n"
    )
    nb_characters_added = append_write(
        "my_first_file.txt", "This School is so cool!\n"
    )
    print(nb_characters_added)
except Exception as err:
    print("[{}] {}".format(err.__class__.__name__, err))

os.system("rm file_append.txt")
os.system("rm my_first_file.txt")
os.system("clear")
print("--" * 10)
print("tester 3-to_json_string.py")
print("--" * 5 + "pycode" + "--" * 5)
os.system("pycodestyle 3-to_json_string.py")
print("--" * 5 + "pycode" + "--" * 5)

to_json_string = __import__("3-to_json_string").to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = {
    "id": 12,
    "name": "John",
    "places": ["San Francisco", "Tokyo"],
    "is_active": True,
    "info": {"age": 36, "average": 3.14},
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = {132, 3}
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

os.system("clear")
print("--" * 10)
print("tester 4-from_json_string.py")
print("--" * 5 + "pycode" + "--" * 5)
os.system("pycodestyle 4-from_json_string.py")
print("--" * 5 + "pycode" + "--" * 5)

from_json_string = __import__("4-from_json_string").from_json_string

s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = """
{"is_active": true, "info": {"age": 36, "average": 3.14}, 
"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
"""
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_dict = """
    {"is_active": true, 12 }
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

os.system("clear")
print("--" * 10)
print("tester 5-save_to_json_file.py")
print("--" * 5 + "pycode" + "--" * 5)
os.system("pycodestyle 5-save_to_json_file.py")
print("--" * 5 + "pycode" + "--" * 5)

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = {
    "id": 12,
    "name": "John",
    "places": ["San Francisco", "Tokyo"],
    "is_active": True,
    "info": {"age": 36, "average": 3.14},
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = {132, 3}
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

os.system("cat my_list.json ; echo " "")
os.system("cat my_dict.json ; echo " "")
os.system("cat my_set.json ; echo " "")

os.system("rm my_set.json")


os.system("clear")
print("--" * 10)
print("tester 6-load_from_json_file.py")
print("--" * 5 + "pycode" + "--" * 5)
os.system("pycodestyle 6-load_from_json_file.py")
print("--" * 5 + "pycode" + "--" * 5)


load_from_json_file = __import__(
    "6-load_from_json_file"
).load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

os.system("rm my_dict.json my_list.json ")

os.system("clear")
print("--" * 10)
print("tester 7-add_item.py")
print("--" * 5 + "pycode" + "--" * 5)
os.system("pycodestyle 7-add_item.py")
print("--" * 5 + "pycode" + "--" * 5)

os.system("python3 7-add_item.py")
os.system("cat add_item.json ; echo " "")
os.system("python3 7-add_item.py Best School")
os.system("cat add_item.json ; echo " "")
os.system("python3 7-add_item.py 89 Python C")
os.system("cat add_item.json ; echo " "")
os.system("python3 7-add_item.py T")
os.system("python3 7-add_item.py E")
os.system("python3 7-add_item.py S")
os.system("python3 7-add_item.py T")
os.system("cat add_item.json ; echo " "")
os.system("rm add_item.json")
