class Encryption:
#################################
# constuctor
#################################
    def __init__(self):
        self.encryption = ""


#################################
# the encode method gathers user input regarding a key word 
# and the location of the file we are translating
#################################
    def encode(self):
        key = input("what key would you like to use: ")
        if any(char.isdigit() for char in key):
            print("no numbers in key please")
        elif len(key.split(" "))>1:
            print("only one word please")
        else:
            file_name = input("filename please: ")
            self.coding(key,file_name,1)


#################################
# the coding method is what converts 
# the files contents into the encryption.
#################################
    def coding(self,key,file_name,num_e):
        file_cont = self.read_file(file_name)
        key = key.strip()
        key = key.lower()
        key_position = []
        file_cont = str(file_cont)
        for i in range(0,len(key)):
            key_position.append((ord(key[i])- 97) *num_e)
        temp_letter = 0
        temp_letter_char = ""
        temp_strg = ""
        pos = 0
        temp_list = file_cont.split(" ")
        for n in temp_list:
            temp_word = ""
            n = n.lower()
            for i in range(0,len(n)):
                
                if ord(n[i]) >= 97 and ord(n[i]) <= 122: 
                
                    temp_letter = ord(n[i]) + key_position[pos]
                
                
                    if pos == len(key_position) - 1:
                        pos = 0
                    
                    if temp_letter >122:
                        temp_letter -= 26
                    if temp_letter <97:
                        temp_letter += 26 
                        
                    if len(key_position) != 1:
                        pos += 1
                    temp_letter_char = chr(temp_letter)
                elif ord(n[i]) == 10:
                    temp_letter_char = "\n"
                else:
                    temp_letter_char = n[i]

                temp_word += temp_letter_char
                
            temp_strg += temp_word + " "
            
        self.encryption = temp_strg


#################################
# the decode method is almost the same
# as the encode class the only differnece
# is that it is used to change the coding to 
# shifting the letters back.
#################################
    def decode(self):
        key = input("what key would you like to use: ")
        if any(char.isdigit() for char in key):
            print("only letters in key please")
        elif len(key.split(" "))>1:
            print("only one word please")
        else:
            file_name = input("filename please: ")
            self.coding(key,file_name,-1)



#################################
# the read_file method makes sure the file is openable 
# and if it is it returns the contents of the file
#################################
    def read_file(self,file_name):
        file_cont = " "
        try:   
            fin = open(file_name, "r")
            file_cont = fin.read()
            fin.close()
        except:
            print("im sorry, I can not find the file")
            print("please check the spelling and try again")
        return file_cont


#################################
# the write_file method writes the current encryption
# and writes it a file.
# if the file does not exist it will make a new one.
# this method also makes sure that the file name is in the right format before writing 
#################################
    def write_file(self,cont,wfile_name):
        
        try:  
            fout = open(wfile_name,"w")
            fout.write(cont)
            fout.close()
        except:
            print("we are having trouble writing to this file")
            print("please try again")
  
#################################
#the print_encrypt method prints the current encryption to the terminal
#################################
    def print_encrypt(self):
        print(self.encryption)
    

#################################
# the write_encrypt method writes the current encryption to a user determined file
#################################
    def write_encrypt(self):
        wfile_name = input("what file do you want to write to: ")
        self.write_file(self.encryption,wfile_name)
   
    

#################################
# displays a user menu
#################################
def display():
    print("**************************")
    print("enter 1 for encryping a file")
    print("enter 2 to display translation")
    print("enter 3 to write the translation to file")
    print("enter 4 to decode a file")
    print("enter 5 to exit")
    print("**************************")

#################################
# accepts user input to use the Encrytion classes features
#################################
def menu():
    
    fs = True
    encrip = Encryption()
    while fs:
        display()
        answer = input("enter your choice please: ")
        if answer == "1":
            encrip.encode()
            encrip.print_encrypt()
        elif answer == "2":
            encrip.print_encrypt()
        elif answer == "3":
            encrip.write_encrypt()
        elif answer == "4":
            encrip.decode()
            encrip.print_encrypt()
        elif answer == "5":
            fs = False
        else:
            print("please enter a listed option")

menu()