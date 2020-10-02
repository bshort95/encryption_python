# encryption_python

## background

the Vigenère cipher was first described in 1553 and survived until it was broken in 1863.earning the title "the indecipherable cipher". this cypher is somewhat based on the caeser cipher, which is where you choose a letter of the alphabet and shift the entire alphabet that position. for example if the letter is c. 
abcdefghijklmnopqrstuvwxyz
cdefghijklmnopqrstuvwxyzab

the Vigenère cipher works by using the caeser cipher but instead shifing with one letter the cipher takes in a key word and ever letter is shifted that many times in order of the word.

## what i learned

i am new to python so the principles i was focusing of during this exercise was
* working with classes and class methods
* reading files
* writing files
* lists
* user error prevention
* string manipulation

## how it works

i used the python extention in vs code  

this program is a class with a small user interface to use the class  

the class is call Encryption and it contains seven methods  

the encode method gathers user input regarding a key word and the location of the file we are translating  

the coding method is what converts the files contents into the encrytion.  

the decode method is almost the same as the encode class the only differnece 
is that it is used to change the coding to shifting the letters back.  

the read_file method makes sure the file is openable and if it is it returns the contents of the file  

the write_file method writes the current encription and writes it a file. if the file does not exist it will make a new one.  
this method also makes sure that the file name is in the right format before writing     
how it works  

the print_encrypt method prints the current encryption to the terminal  

the write_encrypt method writes the current encryption to a user determined file  

there are also two functions that deal with user input to use the before mentioned class  

## program example

the game starts with a menu option

![menu example]()

enter 1 to choose a file.  
to code a file
![instructions example]()  

enter 2 to display the current encryption
![display]()

enter 3 to write the current encryption into a file
![write]()

enter 4 to decode a file
![decode]()

enter 5 to exit
![exit]()  

## useful websites
[Git](https://git-scm.com/)  
[visual studios code](https://code.visualstudio.com/)  
[Python](https://www.python.org/)  
[Python tutorials](https://www.w3schools.com/python)  
[cypher info](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
