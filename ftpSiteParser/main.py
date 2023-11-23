from ftplib import FTP
import queue
from concurrent.futures import ThreadPoolExecutor
from libs.zoomEyeFtpSearch import generateFtpServerList, getServerList
import socket

dirlists = {}

def worker(queue):
    while not queue.empty():
        site = queue.get()
        print(site + ': connecting to server')

        try:
            ftp = FTP(host=site, timeout=10)
            ftp.login()

            ls = []
            ftp.retrlines('LIST', lambda a : ls.append(a))

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

