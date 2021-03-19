from __future__ import print_function, unicode_literals

print("Hello World")
ip_addr1 = '8.8.8.8'
print(ip_addr1)


try:
    ip_addr = raw_input("Enter an IP address:")
except NameError
    ip_addr = input("Enter an IP address:")

print(ip_addr)


#my_str.lower()
#dir(my_str)
#help(my_str.capitalize)
#id(ip_addr) ; references string memory location 
#ip_addr2 is ip_addr  ; check on object
#type(my_str); by default strings in python3 are unicode(vs ascii)
#my_str =b'whatever' ; convert unicode to ascii/byte string in Python 3

#ip_addr = '192.168.1.1'
#'192.168' in ip_addr; '1.1' in ip_addr ; substring 192.168 or 1.1 in ip_addr? True or Falsse Boolean
# TRY WITH in or not in ...
#ip_addr[0]; ip_addr[1] ; ip_addr[-1]; ip_addr[-2].. get characters of string, first , last , second last etc
#len(ip_addr) ; length of the string
# my_str + ' how are you' ; Hello how are you ; string concantenation
# my_str + 1 ; ERROR, doesnt know if you wan to add or concatenate
#255; bin(255) or hex(255); returns string representation, my_var = bin(255) ; type(my_var); returns string
#reverse to int ; int(my_var, 2)
#my_path = r"C:\Windows\newdir\test"; print(my_path); to print raw format of string; use r


# my_str1 = 'whatever'
# my_str2 = "Hello"
# my_str3 = ''' that spans multiple lines '''  ; for paragraph writing, diferent lines
# print(repr(my_str3)) ; gives me what it looks like internally to python, helps troubleshoot strings
# print(my_str.strip()) ; strips off any and all  leading and trailing white spaces
# print(my_str,lstrip()); strips off any leading white spaces
# print(my_str,rstrip()) ; strips off any trailing white spaces

# ip_addr = '192.168.1.1' ; ip_addr.split(".") or ip_addr.split("168.1") or ip_addr.split("192.168"); gives.........['198', '168', '1', '1'] and other o/p, returns a python list


#para = """ This is a paragraph 
# ...: that I am writing 
#...: to test the split funciton in python
#...: """
# para.split() ; para.splitlines() ; para.split("\n") ; Split paragraph on new lines