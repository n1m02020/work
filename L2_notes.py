# num1 = 2 ; num2 = 3 , variables
# modulo operator, gives you remainder back , 7 % 2 = 1
# raise to the power operator ; 2 ** 3 = 8
# from __future__ import division  ; 13/3 (ensure divison is carried forward correctly); 13 //3 Python 3 gets old behaviorq

#num1 = 2.3 ; type(num1)  ..... o/p = float , 
#num1 = 2.0 ; is float... if you want to convert it to integer use int(num1)
#num2 = 2 ; is integer.... if you want to convert to float use float(num2)
#num3 = 2.010101 ; and you want to round that number to 3 digits....... round(num3, 3)...gives 2.010   OR round(num3) .. gives 2

#In [25]: .1 +.2
#Out[25]: 0.30000000000000004   ; not .3 since for us its decimal; when these numbers are stored in binay they have to have some position in computer world, artifact that numbers are stored in binary system for storage, round problem thereof; no practical implications

# i = 1 ; i = i + 1 OR i += 1 OR i -= 1 ; increment of decrement i variable


##########################################################################################

#in command terminal in working directory; ls; rm abc.txt ; cat xyx.txt | more (see folder files, remove file and view file)


# in ipython interpreter shell
# f = open("reorg.txt")    ; f is just the variable name ; to read a file in current working directory 

#In [2]: f
#Out[2]: <_io.TextIOWrapper name='reorg.txt' mode='r' encoding='cp1252'>     ; reference to the file, file open for reading

#output = f.read() ; referring to variable f, calling the read function for file.... output is variable where file contents are stored, 1 big string : print(output)

#In [7]: f.read()
#Out[7]: ''               ; null becoz we're sitting at the end of the read of this file


#In [8]: f.seek(0) ; to go to the beginning to the file ; we dont use this too often
#Out[8]: 0

#In [9]: f.read() ; get my entire file contents


#typical python file would look like: 

# f = open("show_version.txt")
# output = f.read()
# print(output)
#f.close()




# f = open("reorg.txt")
#In [2]: f.readline()        ; readline operation reads file content line by line
#Out[2]: 'SD-Edge (Software Defined Edge) : Firewalls, Routing, Switching, WAN, DIA\n'

#In [3]: f.readline()
#Out[3]: 'SD-DC/Cloud Networking :(Software Defined Datacenter) : Firewalls, LB , Routing, Switching, DCI/WAN, ISP\n'

#In [41]: f.readline()
#Out[41]: ''

#In [42]: f.seek(0)
#Out[42]: 0
#In [43]: f.readlines()    ; to read all lines of file together in 1 go; returns a list that has all lines of file, keeps the '/n' new lines

# OR 


#In [46]: f.seek(0)
#Out[46]: 0

#In [47]: output = f.read()
#In [48]: output.splitlines()         ; divide this up as a list based on new lines of the files, this rempoved the '/n' new lines;   f.readlines vs output.splitlines()

#In [49]: f.close()    ; close file after using


# ORRRRR

#In [51]: with open("reorg.txt") as f:               ; context manager form of this proper python, variable f, indended block, all inside this block and we define output, python automatically closes file handle after existing out of block, clse happens automatically
 #   ...:     output = f.read() 
  #  ...: 
#print(output)                                  ; entire content of file as a single string
#In [3]: type(output)
#Out[3]: str

# how to write to a new file

#In [9]: f = open("newfile.txt", mode = "w")  ; write to a file mode, is destructive, overwirtes previously written stuff if you use it second time again, use append operation instead to avoid this

#In [10]: f.write("whatever\n")   ; write contents to a file 
#Out[10]: 9

#In [11]: f.write("whatever\n")
#Out[11]: 9

#In [12]: f.write("whatever\n")
#Out[12]: 9

#In [13]: f.write("whatever\n")
#Out[13]: 9

#In [14]: f.write("whatever\n")
#Out[14]: 9

#In [15]: f.flush()  ; copy, flush contents to the file

#In [16]: f.close()  ; close the file

#PS C:\Users\m660753\Desktop\work> cat newfile.txt
#whatever
#whatever
#whatever
#whatever
#whatever

#In [3]: f = open("newfile.txt", mode = "a")

#In [4]: f.write("what are you doing\n")
#Out[4]: 19

#In [5]: f.write("what are you doing\n")
#Out[5]: 19

#In [6]: f.flush()
#In [7]: f.close()

#In [8]: exit
#PS C:\Users\m660753\Desktop\work> cat newfile.txt
#whatever
#whatever
#whatever
#whatever
#whatever
#what are you doing
#what are you doing


#############################################################################
# Python lists
# programming data is sequential, 1st element, 2nd element, ..nth element;  
#e.g : reading lines from file, reading bytes from network, seperating a sentence up into its words, going through the octets of an IP address, going through parts of IPv6 addr, -- > inherent sequence of elements == We use lists to deal with sequential elements

#In [1]: my_list = []     ; how to define a string

#In [2]: type(my_list)
#Out[2]: list

#In [4]: my_list = [22, 3.0, 'how are you'] ; different data types in the elements of a string - integer, float, string

#In [5]: my_list[1]     ; looking at different elements of a list
#Out[5]: 3.0

#In [6]: my_list[2]
#Out[6]: 'how are you'

#In [7]: my_list[0]
#Out[7]: 22

#In [8]: my_list[2] = 'something else'   ; give an index in a list a new value

#In [9]: my_list
#Out[9]: [22, 3.0, 'something else']    ; new value changed

#In [10]: len(my_list)  ; length of the list has total 3 elements
#Out[10]: 3



#In [14]: my_list.append('hello')   ; append elements to the list
#In [15]: my_list
#Out[15]: [22, 3.0, 'something else', 'hello']

#In [16]: my_list.append(55)
#In [17]: my_list
#Out[17]: [22, 3.0, 'something else', 'hello', 55]

#In [19]: my_list + [2, 3, 'for']     ; list concatenation, without modifying original list, makes a new list 
#Out[19]: [22, 3.0, 'something else', 'hello', 55, 2, 3, 'for']


#In [21]: my_list = my_list + [5, 4.0, 'how are you']   ; list concatenation with modifying the original list value
#In [22]: my_list
#Out[22]: [22, 3.0, 'something else', 'hello', 55, 5, 4.0, 'how are you']


#In [23]: my_list
#Out[23]: [22, 3.0, 'something else', 'hello', 55, 5, 4.0, 'how are you']
#In [26]: my_list.extend(['adding more to the end', 6.0])                      ; adding elements at the end of the list
#In [28]: my_list
#Out[28]: 
#[22,
# 3.0,
# 'something else',
# 'hello',
# 55,
# 5,
# 4.0,
# 'how are you',
# 'adding more to the end',
# 6.0]





#In [30]: my_list.pop()            ; using pop to remove last element of the list
#Out[30]: 6.0

#In [31]: my_list
#Out[31]: 
#[22,
# 3.0,
# 'something else',
# 'hello',
# 55,
# 5,
# 4.0,
# 'how are you',
# 'adding more to the end']



#In [34]: my_list.pop(0)     ; remove element[0] from list 
#Out[34]: 22

#In [35]: my_list
#Out[35]: 
#[3.0,
# 'something else',
# 'hello',
# 55,
# 5,
# 4.0,
# 'how are you',
# 'adding more to the end']


#In [37]: my_list.pop(2)   ; remove element[2] from list
#Out[37]: 'hello'

#In [38]: my_list
#Out[38]: [3.0, 'something else', 55, 5, 4.0, 'how are you', 'adding more to the end']



#In [40]: my_list
#Out[40]: [3.0, 'something else', 55, 5, 4.0, 'how are you', 'adding more to the end']

#In [41]: del my_list[0]   ; another way to remove 1st element from list

#In [42]: my_list
#Out[42]: ['something else', 55, 5, 4.0, 'how are you', 'adding more to the end']




#In [43]: dir(my_list)   ; bunch of list methods available to us
#Out[43]: 
#['__add__',
 #'__class__',
 #'__class_getitem__',
 #'__contains__',
 #'__delattr__',
 #'__delitem__',
 #'__dir__',
 #'__doc__',
 #'__eq__',
 #'__format__',
 #'__ge__',
 #'__getattribute__',
 #'__getitem__',
 #'__gt__',
 #'__hash__',
 #'__iadd__',
 #'__imul__',
 #'__init__',
 #'__init_subclass__',
 #'__iter__',
 #'__le__',
 #'__len__',
 #'__lt__',
 #'__mul__',
 #'__ne__',
 #'__new__',
 #'__reduce__',
 #'__reduce_ex__',
 #'__repr__',
 #'__reversed__',
 #'__rmul__',
 #'__setattr__',
 #'__setitem__',
 #'__sizeof__',
 #'__str__',
 #'__subclasshook__',
 #'append',
 #'clear',
 #'copy',
 #'count',
 #'extend',
 #'index',
 #'insert',
 #'pop',
 #'remove',
 #'reverse',
 #'sort']

#In [47]: my_list
#Out[47]: ['something else', 55, 5, 4.0, 'how are you', 'adding more to the end']

#In [44]: my_list.count('hello')   ; count how many occurences of string 'hello' in our list
#Out[44]: 0

#In [45]: my_list.count('something else') ; count how many occurences of string 'something else' in outr list
#Out[45]: 1

#In [46]: my_list.index('something else') ; give me the index where string 'something else' first occurs
#Out[46]: 0

#In [48]: my_list.remove('something else') ; find the 1st occureence of string hello and remove this string 'something else '

#In [49]: my_list
#Out[49]: [55, 5, 4.0, 'how are you', 'adding more to the end']