import re


def readFile(path):
    lines = []

    with open(path) as log_file:
        for line in log_file:
            r = re.compile(
                r'^(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[-+]\d{2}:\d{2})\s+(?P<json>{.*})')
            for match in r.finditer(line):
                lines.append(match.groupdict())

    return lines
