import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(f_name: str, delimiter=',') -> list[dict]:
    with open(f_name) as file:
        header = file.readline()[: -1].split(delimiter)
        return [dict(zip(header, line[: -1].split(delimiter))) for line in file]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))