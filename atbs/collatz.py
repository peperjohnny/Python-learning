def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(str(number))
        elif number % 2 == 1:
            number = 3 * number + 1
            print(str(number))

print('Please put in a number: ')

while True:
    try:
        number = int(input())
        break
    except ValueError:
        print('Error: Please type in a number.')

collatz(number)
