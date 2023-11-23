from ftplib import FTP
import queue
from concurrent.futures import ThreadPoolExecutor
from libs.zoomEyeFtpSearch import generateFtpServerList, getServerList
import socket

##########################################################################
# Script that connects to a list of FTP servers and lists the root directory contents.
# In order to retrieve a list of available IP adresses, ZoomEye SDK is used.
# To use this script, you must retrieve ZoomEye API key and place it in .env file
# To generate a list of vulnerable IP addresses, run the following function:
# generateFtpServerList()
##########################################################################

dirlists = {}


def worker(queue):
    while not queue.empty():
        site = queue.get()
        print(site + ': connecting to server')

        try:
            ftp = FTP(host=site, timeout=10)
            ftp.login()

            ls = []
            ftp.retrlines('LIST', lambda a: ls.append(a))

            dirlists[site] = ls
            print(site + ': directory list successful')

            ftp.quit()
        except socket.timeout:
            print(site + ': timeout reached, skipping')


queue = queue.Queue()
servers = getServerList()
for server in servers:
    queue.put(server)

with ThreadPoolExecutor() as executor:
    executor.submit(worker, queue)
    executor.submit(worker, queue)
    executor.submit(worker, queue)


for site, dirs in dirlists.items():
    print("======= {} =======".format(site))

    for dir in dirs:
        print(dir)
