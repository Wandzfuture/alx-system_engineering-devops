#!/usr/bin/python3
"""
gather employee data from API
"""

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def get_employee_todo_list_progress(employee_id):
    """
    Returns the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        A string representing the TODO list progress.
    """
    try:
        response = requests.get(f"{REST_API}/users/{employee_id}",
                                headers={"Accept": "application/json"})
        response.raise_for_status()
        employee_data = response.json()

        response = requests.get(f"{REST_API}/todos",
                                headers={"Accept": "application/json"})
        response.raise_for_status()
        task_data = response.json()

        tasks = [task for task in task_data if task["userId"] == employee_id]
        completed_tasks = [task for task in tasks if task["completed"]]

        output = "Employee {} is done with tasks({}/{})".format(
            employee_data["name"], len(completed_tasks), len(tasks))
        for task in completed_tasks:
            output += "\n\t{}".format(task["title"])

        return output
    except requests.RequestException as e:
        print("Error: {}".format(e))
        return None


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            employee_id = int(sys.argv[1])
            result = get_employee_todo_list_progress(employee_id)
            if result:
                print(result)
        else:
            print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
            sys.exit(1)
    else:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
