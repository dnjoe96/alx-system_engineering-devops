#!/usr/bin/python3
""" script for api to employee todos info and export into csv format """

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    if len(argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee id>")
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
    with open('{}.csv'.format(argv[1]), 'w') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["userId", "username", "completed", "title"],
            quoting=csv.QUOTE_ALL
        )
        for d in total:
            writer.writerow({
                "userId": argv[1],
                "username": username,
                "completed": d.get('completed'),
                "title": d.get('title')
            })
