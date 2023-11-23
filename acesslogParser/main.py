from libs.AccessLogParser import AccessLogParser
from datetime import datetime

##########################################################################
# Small script that parses an undisclosed application's access log.
# Example of the log records is provided in the access.log.example file.
# Record filtering is done via JSON Path and the matched results (if any)
# are compared against the provided value.
# Required to run: jsonpath-ng==1.6.0
##########################################################################

AcessLogParser = AccessLogParser()
AcessLogParser.info()
# return all the log records that match the following value for request id
events = AcessLogParser.readFile(
    '$.request_id', 'ad9f0ce4296e562242cdb529f4044fbb')

for event in events:
    print(event)
