
import random 
count =0
number =random . randint(0,100)

print("warning: you have 7 chances to guess my number")

while True:
 count +=1
 num = int(input("guess: "))
 if count == 8:
       print("out of chances!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
       break
 elif num<0 or num>100:
        print("wrong interval")
        print("try again")
 elif num< number:
        print("higher")
 elif number < num:
        print("lower")

       
 else:
        print("ok fella !!!!!")
        break




