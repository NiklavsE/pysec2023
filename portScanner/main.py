import sys
import socket
import logging
import time
from datetime import datetime
import multiprocessing
from libs.utils import tcpScan, portList, isHostUp

def doScan(target):
	ports = portList()
	ports = [ports[x:x+300] for x in range(0, len(ports), 300)]

	pool = multiprocessing.Pool()
	results = [pool.apply_async(tcpScan, (target, chunkedPorts)) for chunkedPorts in ports]
	openPorts = []

	for result in filter(lambda i : i.get() != [], results):
		openPorts += result.get()

	return openPorts


if __name__ == '__main__':

	# check if target is reachable & arg count match
	if len(sys.argv) == 2:
		target = socket.gethostbyname(sys.argv[1])
		if False == isHostUp(target):
			print('Host is unreachable.')
			sys.exit()
	else:
		print("Invalid amount of Argument")
		sys.exit()

	print("Scanning Target: " + target)

	startTime = time.time()
	openPorts = doScan(target)

	scanDuration = time.time() - startTime
	print("Scanning completed in %fs" % scanDuration)

	print("-" * 50)
	if openPorts == []:
		print('No open ports detected.')
	else:
		print('List of open ports:')
		for port in openPorts:
			print(port)
	print("-" * 50)