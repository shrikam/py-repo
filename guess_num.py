import random
ran_num=random.randint(0,10)
print(ran_num)
guess_num=None
#guess_num= input(" guess the number : ")

while(ran_num != guess_num):
	guess_num= input(" guess the number : ")
	if (guess_num < ran_num):
		print("number is less than the random number")
	if (guess_num > ran_num):
		print ("number is greater than the random number")
	if (guess_num == ran_num):
		print(" yes correct guess")

