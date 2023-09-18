#Generating the random strong password using python programming
import random

class Password_Generator:
    def random_password(self,number):
        password=""
        '''A password consits uppercase,lowercase,digits and various symbols'''
        lower_case="abcdefghijklmnopqrstuvwxyz"
        upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits="1234567890"
        symbols="!@#$%&()?"
        total_characters=lower_case+upper_case+digits+symbols
        i=0
        #By using while loop we can add number of random character to password attribute
        while i<number:
            password+=random.choice(total_characters)
            i+=1
        return password
    
    
d1=Password_Generator()
#inputing the password length to generate the random password
number=int(input("Enter your password length:"))
my_password=d1.random_password(number)
print("random generated strong password is:"+my_password)#printing the password from importing random
            
        







