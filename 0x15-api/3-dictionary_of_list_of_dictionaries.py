#!/usr/bin/python3
'''
Export employee data to JSON
'''

import requests
import json
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def get_employee_todo_list_progress(employee_id):
    """
    Returns the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        A list of tasks owned by the employee.
    """
    try:
        employee_url = "{}users/{}".format(REST_API, employee_id)
        response = requests.get(
            employee_url, headers={"Accept": "application/json"}
        )
        response.raise_for_status()
        employee_data = response.json()

        todos_url = "{}todos".format(REST_API)
        response = requests.get(
            todos_url, headers={"Accept": "application/json"}
        )
        response.raise_for_status()
        task_data = response.json()

        tasks = [task for task in task_data if task["userId"] == employee_id]

        return tasks, employee_data["username"]
    except requests.RequestException as e:
        print("Error: {}".format(e))
        return None, None


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        employee_id = int(sys.argv[1])
        tasks, username = get_employee_todo_list_progress(employee_id)
        if tasks:
            data = {
                str(employee_id): [
                    {
                        "username": username,
                        "task": task["title"],
                        "completed": task["completed"]
                    }
                    for task in tasks
                ]
            }
            with open(
                "{}.json".format(employee_id), "w"
            ) as jsonfile:
                json.dump(data, jsonfile, indent=4)
            print("Data exported to {}.json".format(employee_id))
        else:
            print("No data found for employee ID {}".format(employee_id))
    else:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
