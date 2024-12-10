# Lucas Brinks
# 12/10/24
# while loops

# Movie Tickets
while True:
    try:
        age = int(input('Enter your age (put in -99 to quit):'))
        if age == -99:
            break
        elif age < 3:
            print('You get your ticket for free small person.')
        elif age <= 12:
            print('Your ticket costs $10.')
        else:
            print('Your ticket cost $15.')
    except ValueError:
        print('Please enter in a number only.')

# Three Exits
people = []
while len(people) < 7:
    try:
        age = int(input('Enter your age (put in -99 to quit):'))
        if age == -99:
          break
        else:
            people.append(age)
    except ValueError:
        print('Please enter in a number only')
print(f'These ages bought tickets: {people}')
