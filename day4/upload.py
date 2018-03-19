import socket
import socketserver

socket.socket


class Person(object):
    def __init__(self, name):
        self.name = name


class Student(object):
    def __init__(self, name, age, sex):
        super(Student, self).__init__(name)
        self.age = age
        self.sex = sex
