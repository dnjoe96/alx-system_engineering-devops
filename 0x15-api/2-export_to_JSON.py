#!/usr/bin/python3
""" script for api to employee todos info and export into csv format """

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    if len(argv) != 2:
        print("Usage: ./2-export_to_json.py <employee id>")
        exit()
    response = requests.get(
                     "https://jsonplaceholder.typicode.com/users/{}"
                     .format(argv[1])
                    ).json()

    if not response:
        exit()
    else:
        username = response.get('username')

    total = requests.get(
                     "https://jsonplaceholder.typicode.com/todos?userId={}"
                     .format(argv[1])
                    ).json()
    
    json_obj = {}
    obj_list = []

    for d in total:
        one = {
                'task': d.get('title'),
                'completed': d.get('completed'),
                'username': username
                }

        obj_list.append(one)

    json[argv[1]] = obj_list

    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump(json_obj, f)
