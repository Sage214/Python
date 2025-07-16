#--------------------------packages/libraries/connecting files----------------------------
#packages means some kind of folder where all the libraris are stored. Like a folder we where we store a lot of data, then we have packages in coding
#where we can store lot of libraries in that.
#----------------------Libraries----------------------------------------------
#libraries are the diffrent inbiult python files, where we have diffrent functionswhich we can use in our code.
#these all inbuilt functions are like print,input, the diffrence is that these functions were already created when python was created. but other functions were created later afterwards in the form of libraries.
#You have to first import the library into our code, and then use the function. import means connecting with the library.
#example: randint function from randint library, 
#------------------3 ways to connect with the librarys----------
#1. import libraryname ( this willl all functions we can use any function from the library)
#2. from libraryname import * (this will also import all functions we can anything). * means to import all
#3. from libraryname import function () this will import only that function we can only use that.

#First 2 ways are used whne we want to use many functions
#Third way is used when we want to use just one function

#eg 
from random import * 
#or
import random
#or
from random import randint

####################Library/module-----------------------------

#------------------------------------------connect two python Files-------------------------------
#1. we create a function/class in second file, inside which we do all coding. 
#2. No come back to first/main file use import at top to import the function or class
#eg: from filename import classname/function
#3. call function in first class

from s import Hi

Hi()