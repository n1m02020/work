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

