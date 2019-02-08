'''
a = 'hello world'
b = ['hello', 'shreyans', 2, 3]
c = {
    'semester': 6,
    'section': 'b',
    'subjects': ['WT', 'C', 'DS'],
    'name': 'Shreyans',
}
print(b[0])
print(c['semester'])

# most evil thing in the world
# a = 'b'

if 1 == 1:
    print('1 is 1')
elif 2 == 2:
    print('2 is 2')
else:
    print('everything is true')

while (False):
    print('INFINITE LOOP')

for i in range(0, 2, 1):
    print(i)

def hello_world(name):
    print("Hello " + name)

print(hello_world("Sameer Kumar"))

class Person:

    URL = "https://www.google.com"

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def __del__(self):
        self.name = ''

sameer = Person('Sameer')
print(sameer.URL)

a = ('ace', 'hours', 32, 69)


# import funcs

from funcs import hello_world

print(hello_world("sameer"))
'''

# import flask
from flask import Flask

app = Flask(__name__)

# Classes - First letter upper case
# variables - seperated with underscore
# objects - camelCase


