from datetime import datetime
import json
import random
import time

# CONSTs
JSON_FILE = "request_data_with_duration_time.json"
PATH = "./statics"
LIMIT_ROW_IN_FILE = 14798


class ValuesFixed:
    controller_pods = ["pod-1", "pod-2"]
    paths = ["/home", "/users"]
    duration_time = [t/1000 for t in range(1, 803)]  # seconds


def random_value(arr):
    val = random.choice(arr)
    return val


def write(row_data):
    """Write row data to json file"""
    path_to_write = f"{PATH}/{JSON_FILE}"
    print(f"Write: {row_data}")
    with open(path_to_write, "a") as f:
        json.dump(row_data, f)
        f.write("\n")


def generate():
    current_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    row = {
        "timestamp": current_time,
        "path": random_value(ValuesFixed.paths),
        "method": "GET",
        "service_name": "process_log",
        "controller_pod": random_value(ValuesFixed.controller_pods),
        "duration_time": random_value(ValuesFixed.duration_time)
    }
    return row


if __name__ == "__main__":
    count = 0
    while True:
        if count == LIMIT_ROW_IN_FILE:
            break
        row = generate()
        write(row_data=row)
        count += 1
        time.sleep(0.2)
    print("Done!")
