def pick_your_path():
    print('Welcome to Treasure Island.\n Your mission is to find the treasure.')
    road = input(' You are at a crossroad will you go left or right?\n').lower()
    if road == 'left':
        lake = input('You come across a lake. There is an island in the middle. Will you "wait" for a boat or "swim" '
                     'across.\n').lower()
        if lake == 'wait':
            color = input('You arrive at the lake unharmed. There is a house with three doors. One red, one yellow '
                          'and one green. Which will you choose?\n ')
            if color == 'red':
                print('The room is filled with fire, Game Over.')
            elif color == 'yellow':
                print('You entered a room of beasts, Game Over.')
            elif color == 'green':
                print('You found the treasure! You win!')
            else:
                print('You did\'nt choose a real door, Game Over')
        else:
            print('You got attacked by sharks! Game over.')
    else:
        print('You fell into a hole, Game Over.')


pick_your_path()


def leap_year():
    year = int(input("What Year do you want to check?"))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('Leap Year!')
            else:
                print('not leap year')
        else:
            print('leap year')
    else:
        print('Not leap year')


def roller_coaster():
    print('Welcome to the the RollerCoaster!')
    height = int(input('What is your height in inches?'))
    bill = 0
    if height >= 48:
        print('You can ride the ride!')
        age = int(input("What is your age?"))
        if age < 12:
            bill = 5
            print('please pay $5')
        elif age <= 18:
            bill = 7
            print('please pay $7')
        else:
            bill = 12
            print('Please pay $12')
        photo = input("Do you want a photo taken? Y or N")
        if photo == "y":
            bill += 3
        print(f'Your bill is {bill}')
    else:
        print('You must be 48 inches tall to ride the ride, sorry come again.')


roller_coaster()


def pizza_order():
    size = input('What size Pizza do you want? s $5, m 7$, l $10, xl $14')
    add_pep = input('Would you like pepperoni? Y or N')
    extra_cheese = input("Would you like extra cheese? Y or N")

    bill = 0
    if size == 's':
        bill += 5
    elif size == 'm':
        bill += 7
    elif size == 'l':
        bill += 10
    else:
        bill += 14

    if add_pep == 'y':
        if size == 's':
            bill += 2
        else:
            bill += 3

    if extra_cheese == 'y':
        bill += 1

    print(f"Your final bill is {bill}")


pizza_order()


def love_calc():
    print('Welcome to the Love Calculator')
    name1 = input('What is your name?')
    name2 = input('What is their name?')

    string = name1 + name2
    lower_case = string.lower()
    t = lower_case.count('t')
    r = lower_case.count('r')
    u = lower_case.count('u')
    e = lower_case.count('e')
    true = t + r + u + e

    l = lower_case.count('l')
    o = lower_case.count('o')
    v = lower_case.count('v')
    e = lower_case.count('e')
    love = l + o + v + e
    love_score = int(str(true) + str(love))
    if (love_score < 10) or (love_score > 90):
        print(f"Your love score is {love_score}, you go together like coke and mentos.")
    elif (love_score >= 40) or (love_score <= 50):
        print(f"Your love score is {love_score}, you are okay together.")
    else:
        print(f'your score is {love_score}')


love_calc()
