# This is a sample Python script.
import requests
import json
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dog = {"name": 'sheleg', "age": 12, "breed": 'husky'}
    json_header = {'Content-Type': 'application/json'}
    res = requests.post('http://127.0.0.1:5000/add_dog', data=json.dumps(dog), headers=json_header)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
