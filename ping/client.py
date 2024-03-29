#!/usr/bin/env python3

#########################################################################
#  Script     : client.py
#  Author     : BrailinsonDisla
#  Date       : July 27th, 2018
#  Last Edited: July 27th, 2018 @ ~ 22:00 , BrailinsonDisla
#########################################################################
# Purpose:
#    --
#
# Requirements:
#    None.
#
# Method:
#    If arguments are given:
#      # The 1st argument is considered as the server's IP Address.
#      # The 2nd argument is considered as the server's port number.
#
# Syntax:
#    # 1. client.py
#    # 2. client.py <IP Address>
#    # 3. client.py <IP Address> <Port Number> 
#    # 4. client.py <IP Address> <Port Number> <String Length>
#
# Notes:
#    None.
#########################################################################
# Import the system module.
import sys

# Import the socket module.
import socket

# Import the struct module.
import struct

# Import time, sleep, localtime and strftime from the time module.
from time import time, sleep, localtime, strftime

# Set short sleep time.
wait = 0.50

#########################################################################
# VERIFY FUNCTIONS
#########################################################################
# Check if the string provided is a valid IPv4 Address.
def verify_IPv4(ipv4):
    # Convert ipv4 to a string if possible.
	try:
		ipv4 = str(ipv4)
	except:
        # Return false if not possible.
		return False
    
    # Split the ipv4 string using '.' as the delimiter.
	ip_octet_list = ipv4.split('.')

    # Check the size of the ip_octet_list.
	if len(ip_octet_list) != 4:
        # Return false if there are not 4 octets.
		return False
    
    # Check that each octet is valid.
	else:
		for octet in ip_octet_list:
            # Check that each octet is an integer between 0 and 255.
			try:
                # Check if the octet is an integer.
				check = int(octet)

                # Check if octet is between 0 and 255.
				if (check < 0 or check > 255):
                    # Return false for octets out of range.
					return False
			except:
                # Return false if an octet is not an integer.
				return False
    # Return true if the string defines a valid IPv4 Address.
	return True

#########################################################################
# DEFAULT ADDRESS SERVER INFO
#########################################################################
# Print header to inform the user of the default settings.
print ('DEFAULT SETTINGS FOR SERVER:'); sleep(wait)

# Set the default server IP Address and inform the user.
server_ip = '127.0.0.1'
print ('\tServer IP:\t\t' + server_ip)

# Set the default server port and inform the user.
server_port = 1543
print ('\tServer Port:\t\t' + str(server_port) + '\n'); sleep(wait)

#########################################################################
# CHECK FOR SYSTEM ARGUMENTS
#########################################################################
# Store bool for args.
argsBool = False

# Store command line arguments.
args = sys.argv

# Store length of arguments list.
argsLength = len(args)

# Reserve variable for error message.
error = ''

# Set string for changes.
changes = ''

# Check if arguments have been provided - for IP Address.
if argsLength > 1:    
    # Set the error.
	error = 'IP ADDRESS ERROR' # The IP Address provided in the arguments is invalid.
    
    # Set temp_ip to first argument.
	temp_ip = args[1]
    
    # Verify if IP Address provided is valid.
	if verify_IPv4(temp_ip):
        # Inform user that IP Address has been chaned by argument.
		changes += 'IP ADDRESS CHANGED\n';

        # Change server_ip.
		server_ip = temp_ip

        # Change argsBool status.
		argsBool = True
	else:
        # Print error if IP Address is invalid.
		print (error)

        # Exit program.
		exit()

# Checks if arguments have been provided - for port.
if argsLength > 2:
    # Set the error.
	error = 'PORT NUMBER ERROR' # Port provided is invalid.

    # Set temp_port to second argument.
	temp_port = args[2]
    
    # Verify if port provided is valid.
	try:
		temp_port = int(temp_port)

		if temp_port >= 0 and temp_port <= 65536:
            # Inform user that port has been chaned by argument.
			changes += 'PORT NUMBER CHANGED\n';

            # Change server_port.
			server_port = temp_port

            # Change argsBool status.
			argsBool = True
		else:
            # Raise error to execute the except block if port is not in range.
			int ('raise')
	except:
        # Print changes.
		print (changes)

        # Print error if port is invalid.
		print (error)

        # Exit program.
		exit()

if argsBool:
	# Print changes.
	print (changes)
#########################################################################
# ARGS MODIFIED ADDRESS SERVER INFO
#########################################################################
# Check if settings were changed by arguments.
if argsBool:
    # Print header to inform the user of new settings.
	print ('NEW SERVER SETTINGS:'); sleep(wait)

    # Print the new server IP Address and inform the user.
	print ('\tServer IP:\t\t\t' + server_ip)

    # Print the new server port and inform the user.
	print ('\tServer Port:\t\t\t' + str(server_port) + '\n'); sleep(wait)

#########################################################################
# ADDRESS INFO FOR SERVER
#########################################################################
# Check if settings were changed by arguments.
if not argsBool:
	# Ask the user about changing settings.
	print ('Do you wish to change default settings? [Yes/No]')

	# Read user response.
	prompt = input().lower()

	# Check if user provided an invalid response, if so ask again.
	while prompt not in ['yes', 'no', 'y', 'n']:

		# Ask the user again.
		print ('Please answer Yes or No | Y or N.')

		# Read response.
		prompt = input().lower()

	# Request information.
	if prompt in ['yes', 'y']:
		# Request, read and store ip address.
		print ('Enter Server IP Address in IPv4 format: ')
		temp_server_ip = input()

		# Check if user omitted to setting the IP Address.
		if len(temp_server_ip) != 0:
			# Vefiry IP Address provided is an valid IPv4.
			ipv4_verification = verify_IPv4(temp_server_ip)

			# Check if IP Address provided is invalid, if so ask again.
			while not ipv4_verification:
				# Check if user omitted to setting the IP Address.
				if len(temp_server_ip) == 0:
					# Break out of the while loop
					break
				
				# Request, read and store ip address again.
				print ('Enter a valid IP Address in IPv4 format: ')
				temp_server_ip = input()

				# Vefiry IP Address provided is an valid IPv4.
				ipv4_verification = verify_IPv4(temp_server_ip)

			# Change server_ip if address provided is valid.
			if ipv4_verification:
				# Set Server IP Address to a valid IPv4 obtained from user.
				server_ip = temp_server_ip

				# Change argsBool status.
				argsBool = True

		# Request port.
		print ('Enter Server Port: ')

		# Check if port provided is invalid, if so ask again.
		while True:
			# Check if the port string provided is an integer.
			try:
				# Store the port string provided.
				temp_server_port = input()
				
				# Skip if user presses enter.
				if len(temp_server_port) == 0:
				    break
				
				# Parse the port string provided to an integer.
				temp_server_port = int(temp_server_port)

				# Set Server Port to a valid port obtained from the user.
				server_port = temp_server_port

				# Change argsBool status.
				argsBool = True
				
				# Break out of the while loop if port provided is valid.
				break
			except:
				# Request, read and store port again.
				print ('Enter a valid Port: ')
				
				continue

#########################################################################
# FINAL ADDRESS SERVER INFO
#########################################################################
# Check if user changed settings.
if argsBool:
    # Print header to inform the user of the final settings.
    print ('\nFINAL SETTINGS FOR SERVER:'); sleep(wait)

    # Inform the user of final server ip address.
    print ('\tServer IP:\t\t' + server_ip)

    # Inform the user of the final server port.
    print ('\tServer Port:\t\t' + str(server_port)); sleep(wait)
    
# Indicate the server being pinged and port.
print ('\nPinging ' + server_ip + ' on port ' + str(server_port)); sleep(wait)

print ('--------------------------------------')

#########################################################################
# CREATE A CLIENT SOCKET
#########################################################################
# Create the client socket.
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set server address.
serverIPv4 = server_ip

# Set port for the service.
serverPort = server_port

# Set a timeout for the client socket.
client.settimeout(1)

#########################################################################
# PING SERVER
#########################################################################
# Create variable to set maximun number of pings.
maxPings = 10

# Create variable to track pings.
currentPing = 1

# Create variable to track pings requests serviced.
serviced = 0

# Create variable to track pings requests dropped.
dropped = 0

# Create variable to track min ott and rtt.
minTT = [1000000, 1000000]

# Create variable to track max ott and rtt.
maxTT = [0, 0]

# Create variable to calculate average ott and rtt.
avgTT = [0, 0]

# Loop for pinging to server a certain amount of times.
while currentPing <= maxPings:
    # Create variable to store time when packet is sent.
    sentTime = ''

    # Create variable to store time when packet is received.
    receivedTime = ''

    # Pack the current ping number -- 4-byte sequence number that identifies packet.
    packedSeqNum = struct.pack('i', currentPing)

    # Record time stamp in seconds.
    sentTime = time()
    
    # Send message (sequence number) from client to serverIPv4 at port serverPort.
    client.sendto(packedSeqNum, (serverIPv4, serverPort))

    # Handle response from the server.
    try:
        # Receive response from server.
        serverResp, (serverAddr, serverPort) = client.recvfrom(8000)

        # Record time stamp in seconds.
        receivedTime = time()

        # Update number of pings serviced.
        serviced += 1
        
        # Unpack client's sequence number and time packet was received by server -- 4-byte + 8-byte.
        pingSeqNum, serverReceiveTime = struct.unpack('id', serverResp)[0:2]
        
        # Calculate OTT.
        ott = serverReceiveTime - sentTime
        
        # Calculate RTT.
        rtt = ott + (receivedTime - serverReceiveTime)

        # Update maxTTs.
        if maxTT[0] < ott:
            maxTT[0] = ott
        if maxTT[1] < rtt:
            maxTT[1] = rtt

        # Update minTTs.
        if minTT[0] > ott:
            minTT[0] = ott
        if minTT[1] > rtt:
            minTT[1] = rtt

        # Update avgTT.
        avgTT[0] += ott
        avgTT[1] += rtt
        
        # Update minTTs.
        # Indicate ping message number, ott and rtt.
        print ('Pinging Message ' + str(currentPing )+ ': OTT: ' + str(ott) + 'secs and RTT: ' + str(rtt) + 'secs'); sleep(wait)

        # Reset ott and rtt.
        ott = 0; rtt = 0
        
        # Update the currentPing count.
        currentPing += 1

        continue
        
    except:
        # Indicate ping message number, timed out.
        print ('Pinging Message ' + str(currentPing) + ': Request Timed Out'); sleep(wait)

        # Update the currentPing count.
        currentPing += 1

        # Update number of pings serviced.
        dropped += 1
        
        continue

# Check if all pings were sent and print statistics.
if currentPing >= maxPings:
    # Print statistics:
    print ('\nPing Statistics: ' + server_ip + ':')
    print ('Packets: \n\tSent = ' + str(maxPings) + '\n\tReceived = ' + str(serviced) + '\n\tLost = ' + str(dropped)
               + '\n\tLost (%) = ' + str((100 * float(dropped)/maxPings)) + '%\n')
    print ('\tMax OTT: ' + str(maxTT[0]) + '\n\tMin OTT: ' + str(minTT[0]) + '\n\tMax RTT: ' + str(maxTT[1])
                + '\n\tMin RTT: ' + str(minTT[1]) + '\n\tAverage OTT: ' + str((float(avgTT[0])/maxPings))
                + '\n\tAverage RTT: ' + str(float(avgTT[1])/maxPings))
    
client.close()
