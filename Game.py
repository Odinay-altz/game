import random 
secret = random.randint(1,100)
guess = int(input (" Угадай число от 1 до 100 " ))
if guess == secret:
  print ("Ты угадал!")
else:
      print("Не угадал!")
if guess < secret:
  print ("Моё число больше!")
if guess > secret:
  print ("Моё число меньше!")
attempts = 3 
while attempts > 0:
    guess = int(input (" Угадай число от 1 до 100 " ))
if guess == secret:
  print ("Ты угадал!") 
if guess < secret:
  print ("Моё число больше!") 
if guess > secret: 
  print ("Моё число меньше!") 
while attempts -1:
 print ("Осталось 2 попытки") 
guess = int(input ("Угадай число от 1 до 100"))
if guess == secret: 
  print ("Ты угадал!")
if guess < secret:
  print ("Моё число больше!")
if guess > secret: 
  print ("Моё число меньше!")
while attempts -1:
 guess = int(input ("Угадай число от 1 до 100"))
if guess == secret: 
  print ("Ты угадал!")
if guess < secret:
  print ("Моё число больше!")
if guess > secret: 
  print ("Моё число меньше!")
while attempts -1:
  attempts = 3
