import random

def guess(x):
    random_number= random.randint(1, x )
    guess=0
    
    while guess != random_number:
          guess=int(input(f"Guess a number between 1 and  {x} : "))
          if guess < random_number:
            print("Guess again! Too low")
          elif guess > random_number:
            print("Guess again ! Too high") 
          else :
                print(f"You have guessed the number correctly!")

def computer_guess(x):
    low = 1
    high = x
    feedback =""
    while feedback!="c" and low!=high:
        guess = random.randint(low,high)
        feedback = input(f"is {guess} too high(H) or low(L) or correct(C)?? : " ).lower()
        if feedback =="h":
            high= guess - 1
        elif feedback=="l":
            low=guess + 1
    print(f"Yay ! The computer guessed your number,{guess}, correctly")
computer_guess(10)

