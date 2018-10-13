import socket

print("   ____             ______                         ")
print("  /   /  ____   ___   /   ___   ___   ___      ____")
print(" /___/  /   /  /     /    \    /     /   \    /   /")
print("/      /___/  /     /    __\  /___  /___/ \  /   / ")
print("                                        Version 1.0")

class Scanner():
	__ipAdrStart = ""
	__ipAdrStop = "" 
	__startPort = 0
	__stopPort = 0
	#__udp_scan = False

	def __init__(self, ipAdrStart, ipAdrStop, startPort, stopPort):
		self.__ipAdrStart=ipAdrStart
		self.__ipAdrStop=ipAdrStop
		self.__startPort=startPort
		self.__stopPort=stopPort
		#self.__udp_scan=udp_scan

	# scanIP(ip)
	# Scans a range of ports on a single IP address.
	# by trying to open a 
	def scanIP(self, ip):
		closedPorts = 0
		for port in range(int(startPort), int(stopPort)+1):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# connect_ex() tries to find a connection exception
			# thus if the connection exception is false, then 
			# the socket must have been made on that port.
			if sock.connect_ex((ip, port)) == False:
				print("Port {} is open.".format(port))
			else:
				closedPorts+=1
				#print("Port {} is closed.".format(port))
			sock.close()
		print("{} ports are closed!".format(closedPorts))

	def scanIP_range(self):
		if ipAdrStop == 0:
			scanIP(ipAdr)
		else:
			startIP = ipAdrStart.split('.')
			stopIP = ipAdrStop.split('.')
			# Scan all IPs.
			while int(startIP[0]) <= int(stopIP[0]):
				while int(startIP[1]) <= int(stopIP[1]):
					while int(startIP[2]) <= int(stopIP[2]):
						while int(startIP[3]) <= int(stopIP[3]):
							# Concat all IP sections
							currIP = str(startIP[0])+"."+str(startIP[1])+"."+str(startIP[2])+"."+str(startIP[3])
							print("Scanning IP Address {}:".format(currIP))
							self.scanIP(currIP)
							print()
							startIP[3]= int(startIP[3]) + 1
						startIP[2]= int(startIP[2]) + 1
					startIP[1]= int(startIP[1]) + 1
				startIP[0]= int(startIP[0]) + 1





ipAdrStart, ipAdrStop = input("Enter target IP Address (StartIP-EndIP): ").split("-")

startPort, stopPort = input("Enter ports (StartPort-StopPort): ").split("-")

startPort_int = int(startPort)
stopPort_int = int(stopPort)

closed_ports = 0

print("Scanning hosts " + ipAdrStart + " to " + ipAdrStop + ".")
print("Scanning ports " + str(startPort) + " to " + str(stopPort))
print("Scanning in progress...\n")

scanner = Scanner(ipAdrStart, ipAdrStop, startPort_int, stopPort_int)
scanner.scanIP_range()
