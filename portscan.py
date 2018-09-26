import socket 

print("   ____             ______                         ")
print("  /   /  ____   ___   /   ___   ___   ___      ____")
print(" /___/  /   /  /     /    \    /     /   \    /   /")
print("/      /___/  /     /    __\  /___  /___/ \  /   / ")
print("                                        Version 1.0")

class Scanner():
	__ipAdr = "" 
	__startPort = 0
	__stopPort = 0
	#__udp_scan = False

	def __init__(self, ipAdr, startPort, stopPort):
		self.__ipAdr=ipAdr
		self.__startPort=startPort
		self.__stopPort=stopPort
		#self.__udp_scan=udp_scan

	# scanIP(ip)
	# Scans a range of ports on a single IP address.
	# by trying to open a 
	def scanIP(ip):
		for port in range(startPort, stopPort+1):
			sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# connect_ex() tries to find a connection exception
			# thus if the connection exception is false, then 
			# the socket must have been made on that port.
			if sock.connect_ex((ip, port)) == False:
				print("Port " + str(port) + " is open.")
			sock.close()

	def scanIP_range():
		if ipAdr.find("-")==(-1): #Only one IP
			scanIP(ipAdr)
		else:
			ips = ipAdr.split('-')
			startIP = map(int, ips[0].split('.'))
			stopIP = map(int, ips[1].split('.'))
			# Scan all IPs.
			while startIP[0] <= stopIP[0]:
				while startIP[1] <= stopIP[1]:
					while startIP[2] <= stopIP[2]:
						while startIP[3] <= stopIP[3]:
							currIP = str(startIP[0])+"."+str(startIP[1])+"."+str(startIP[2])+"."+str(startIP[3])
							scanIP()
							startIP[3]+=1
						startIP[2]+=1
					startIP[1]+=1
				startIP[0]+=1

#                           #
# Main function starts here #
#                           #

ipAdr = input("Enter target IP Address: ")
ipAdr = socket.gethostbyname(ipAdr)
startPort= int(input("Enter starting port: "))
endPort = int(input("Enter ending port: "))
closed_ports = 0

print("Scanning host " + ipAdr)
print("Scanning ports " + str(startPort) + " to " + str(endPort))
print("Scanning in progress...\n")

# socket(address_family, socket_type)
# AF_INET     => IPv4 Address Family
# SOCK_STREAM => TCP connectons
# SOCK_DGRAM  => UDP connections
for port in range(startPort, endPort+1):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if sock.connect_ex((ipAdr, port)) == 0:
	 	print("Port " + str(port) + " is open.")
	else:
		closed_ports+=1
	sock.close()

print("\nScanning completed.")
print(str(closed_ports) + " ports were closed.")  
