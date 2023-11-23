import zoomeye.sdk as zoomeye
import os.path
from dotenv import load_dotenv

load_dotenv()

def generateFtpServerList():
    apiToken = os.getenv('ZOOMEYE_API_TOKEN', '')

    if '' == apiToken:
        raise Exception('ZoomEye API Token missing in .env')

    zm = zoomeye.ZoomEye(api_key=apiToken)
    data = zm.dork_search('"Anonymous+user+logged+in"')
    data = zm.dork_filter('ip')
    
    with open('serverList.txt', 'w') as file:
        for item in data:
            file.writelines(item[0] + '\n')  

def getServerList():
    if False == os.path.isfile('serverList.txt'):
        raise Exception('No serverlist found. Please generate one using generateFtpServerList')     
   
    serverList = []
    with open('serverList.txt', 'r') as file:
        servers = file.readlines()

        for server in servers:
            server = server.rstrip('\n')

            if ('' == server):
                continue

            serverList.append(server)
    
    return serverList
