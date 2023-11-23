import re
from libs.utils import readFile
import json
from jsonpath_ng import jsonpath, parse
import datetime


class AccessLogParser(object):
    def __init__(self):
        pass

    def info(self):
        print("This is access log parser!")

    log_file_path = 'access.log.example'

    # Given a json path and value, return all the log records that match the value at the given path
    def readFile(self, path, value):
        matched_events = []

        pathExpression = parse(path)

        lines = readFile(self.log_file_path)
        for log_dict in lines:
            jsonData = json.loads(log_dict['json'])

            match = pathExpression.find(jsonData)
            if (value == match[0].value):
                matched_events.append({
                    'timestamp': log_dict['timestamp'],
                    'json': log_dict['json']
                })

        return matched_events
