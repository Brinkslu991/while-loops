# Lucas Brinks
# 12/10/24
# while loops

# Movie Tickets
# while True:
#     age = int(input('Enter your age (put in -99 to quit):'))
#     if age == -99:
#         break
#     elif age < 3:
#         print('You get your ticket for free small person.')
#     elif age <= 12:
#         print('Your ticket costs $10.')
#     else:
#         print('Your ticket cost $15.')

# Three Exits
people = []
while len(people) < 7:
    age = int(input('Enter your age (put in -99 to quit):'))
    if age == -99:
        break
    else:
        people.append(age)

print(f'These ages bought tickets: {people}')
