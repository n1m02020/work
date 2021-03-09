

ip_addr1 = '192.168.1.1'
ip_addr2 = '172.16.1.1'
ip_addr3 = '10.1.1.1'


print("\n")
print("-" *80)
print(ip_addr1, ip_addr2, ip_addr3)
print("\n")
print("-" *80)


print("\n")
print("-" *80)
print("{}{}{}".format(ip_addr1, ip_addr2, ip_addr3))
print("-" *80)
print("\n")



print("\n")
print("-" *80)
print("{:20}{:20}{:20}".format(ip_addr1, ip_addr2, ip_addr3)) #enter in column thats 20 wide 
print("-" *80)
print("\n")


print("\n")
print("-" *80)
print("{:>20}{:>20}{:>20}".format(ip_addr1, ip_addr2, ip_addr3)) #right column aligned
print("{:<20}{:<20}{:<20}".format(ip_addr1, ip_addr2, ip_addr3)) #left column aligned
print("{:^20}{:^20}{:^20}".format(ip_addr1, ip_addr2, ip_addr3)) #center column aligned
print("-" *80)
print("\n")



#pass variables with format method


print("\n")
print("-" *80)
print("{my_ip:^20}{your_ip:^20}{their_ip:^20}".format(their_ip = ip_addr1, your_ip = ip_addr2, my_ip = ip_addr3)) #named arguments passed (intead of positional arguments) and referring to names in format arugument list
print("-" *80)
print("\n")



ip_addr4 = "199.59.1.1"
octets = ip_addr4.split('.') # gets a list of all the octets


print("\n")
print("-" * 80)
print(octets)
print("{:10}{:10}{:10}{:10}".format(octets[0], octets[1], octets[2], octets[3]))
print("{:10}{:10}{:10}{:10}".format(*octets)) # dont treat this as a list, but a sequence of items in the list, get list components
print("-" * 80)
print("\n")




ip_addr5 = '192.168.3.3'
port1 = 80
ip_addr6 = '192.168.4.4'
port2 = 443

print("%s %s" % (ip_addr5, ip_addr6))  # older version of using format method

# in Python3.6 or higher using f string
print(f"{ip_addr5}")
print(f"My ip address is : {ip_addr5}")
print(f"My ip address is : {ip_addr5:^20}")
print(f"My ip address is : {ip_addr6:^20}")

print(f"My ip address1 and port1 is : {ip_addr5:^20} {port1:^8}")
print(f"My ip address2 and port2 is : {ip_addr6:^20} {port2:^8}")