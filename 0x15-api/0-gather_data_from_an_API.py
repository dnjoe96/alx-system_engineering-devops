#!/usr/bin/python3
""" Python script to call an api """

if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee id>")
        exit()
    response = requests.get(
                     "https://jsonplaceholder.typicode.com/users/{}"
                     .format(argv[1])
                    ).json()
    if not response:
        exit()
    else:
        name = response.get('name')
    total = requests.get(
                     "https://jsonplaceholder.typicode.com/todos?userId={}"
                     .format(argv[1])
                    ).json()
    dones = [i for i in total if i.get('completed')]
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(dones), len(total)))
    for d in dones:
        print("\t {}".format(d.get('title')))
