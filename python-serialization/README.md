Python - Serialization
Introduction:

Welcome to our exploration of marshaling and serialization, two fundamental concepts in computer science that enable the efficient storage and transmission of data. In this programming project, you will delve deep into how data can be transformed and communicated between different parts of a system, or even across different systems. This project is designed to enhance your understanding and practical skills in handling data in real-world applications.
What is Marshaling?

Marshaling is the process of transforming memory objects into a format that can be stored or transmitted over a network. It involves packaging complex objects and their attributes into a simpler, often binary, format. This is crucial in scenarios such as remote procedure calls, where objects need to be represented in a standard format across different computing platforms.
What is Serialization?

Serialization, closely related to marshaling, specifically involves converting data structures or object states into a format that can be easily saved to a file or sent over a network. The main goal of serialization is to preserve the state of an object, so it can be recreated in an identical state elsewhere. This becomes essential in developing applications that require data persistence, distributed computing, and data sharing between different software components.
Learning Objectives:

    Articulate the differences and similarities between marshaling and serialization.
    Implement serialization in a practical programming task.
    Understand how serialized data can be used in web applications, databases, and network communications.
    Evaluate the performance implications of different serialization formats, like JSON, XML, and binary formats.

Resources:

    Real Python Serialization
    Real Python: Working With JSON Data in Python
    Python's pickle documentation
    Corey Schafer on Pickle
    CSV to JSON in Python
    Python XML ElementTree Guide
    Socket Programming Guide

This project will equip you with the skills needed to manipulate and manage data effectively, preparing you for more advanced topics in computer science and software development. Get ready to build a solid foundation in data handling that will support your future projects and career in the technology sector.



0. Basic Serialization

Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.
Instructions:

Write a Python module named task_00_basic_serialization.py with the following functions:

def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    pass

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    pass

The function serialize_and_save_to_file take 2 parameters:

    data: A Python Dictionary with data
    filename: The filename of the output JSON file. If the output file already exists it should be replaced.

The function load_and_deserialize take 1 parameters:

    filename: The filename of the input JSON file This function returns a Python Dictionary with the deserialized JSON data from the file.

Execution Output Example:

#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Sample data to be serialized
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Serialize the data to JSON and save it to a file
serialize_and_save_to_file(data_to_serialize, 'data.json')

# Output: The data has been serialized and saved to 'data.json'
print("Data serialized and saved to 'data.json'.")

# Load and deserialize data from 'data.json'
deserialized_data = load_and_deserialize('data.json')

# Output: The deserialized data
print("Deserialized Data:")
print(deserialized_data)

Data serialized and saved to 'data.json'.
Deserialized Data:
{'name': 'John Doe', 'age': 30, 'city': 'New York'}

Repo:

    GitHub repository: dlh-higher_level_programming
    Directory: python-serialization
    File: task_00_basic_serialization.py


1. Pickling Custom Classes

Learn how to serialize and deserialize custom Python objects using the pickle module.
Instructions:

1 - Create a custom Python class named CustomObject. This class should have the following attributes:

    name (a string)

    age (an integer)

    is_student (a boolean)

    Additionally, the class should have a method display method to print out the object's attributes with the following format:

Name: John
Age: 25
Is Student: True

2 - Implement two methods within this class:

    serialize(self, filename): This method will take a filename as its parameter. Using the pickle module, it will serialize the current instance of the object and save it to the provided filename.
    @classmethod deserialize(cls, filename): This class method will take a filename as its parameter. Using the pickle module, it will load and return an instance of the CustomObject from the provided filename.

3 - Save your code in a file named task_01_pickle.py.

    Make sure to handle possible exceptions for non-existent or malformed files. If this happens, the methods should return None

Sample Test:

#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()

Output:

Original Object:
Name: John
Age: 25
Is Student: True

Deserialized Object:
Name: John
Age: 25
Is Student: True
