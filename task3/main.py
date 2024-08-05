import json
import sys

file1_input = sys.argv[1]
file2_input = sys.argv[2]
file_output = sys.argv[3]

# file1_input = './task3/values.json'
# file2_input = './task3/tests.json'
# file_output = './task3/report.json'


def read_json(file_input):
    with open(file1_input, 'r') as f:
        return json.load(f)


def get_report_structure(test, values):
    if isinstance(test, dict):
        for key, value in test.items():
            if key == 'id' and value in values:
                test['value'] = value
            else:
                get_report_structure(item, value)
    elif isinstance(test, list):
        for item in test:
            get_report_structure(item, values)


values = read_json(file1_input)
test = read_json(file2_input)

with open(file_output, 'w') as output:
    json.dump(test, output)
