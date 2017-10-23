from random import randint

secret = randint(0, 20)
guess = 0

guess = int(raw_input("Guess the secret number between 1 and 30"))

while guess != secret:
    if guess == secret:
        guess = int(raw_input("Guess the secret number between 1 and 30"))
        print "You guessed it - congragulations! It's number {0}" .format(secret)
    elif guess > secret:
        print 'manjse'
    elif guess < secret:
        print 'vecje'
    else:
        print 'Sorry, your guess is not correct... Secret number is not {guess_val}' .format(guess_val = guess)

# for i in range(5):
#     guess = int(raw_input("Guess the secret number between 1 and 30"))
#
#     if guess == secret:
#         print "you guessed it"
#         break
#     else:
#         print Sorry, maybe next time
