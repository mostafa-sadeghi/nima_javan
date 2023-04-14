import datetime
import random


def get_birthdays(number_of_peoples):
    birthdays = []

    start_date = datetime.date(2013, 1, 1)
    for i in range(number_of_peoples):
        random_numbers_of_days = datetime.timedelta(random.randrange(0, 365))
        birthdays.append(start_date + random_numbers_of_days)
    return birthdays


def getMatch(birthdays):
    for i in range(len(birthdays)):  # ['1','2','3',.....'23']
        for j in range(i+1, len(birthdays)):
            if birthdays[i] == birthdays[j]:
                return birthdays[i]
    return None


print('''Birthday paradox.
The shows us that in a group of n people, probablity of matching birthdays is surprisingly increasing when n become bigger.
in 23 numbers of people The probability is greater than 50%,
and in 70 numbers of people this probability is 99.9%
''')

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
while True:
    print("How many birthdays shall I generate? (Max = 100)")
    resp = input('> ')
    if resp.isdecimal() and (0 < int(resp) <= 100):
        numDays = int(resp)
        break
print()
print("Here are", numDays, 'birthdays')
birthdays = get_birthdays(numDays)

for birthday in birthdays:
    print(birthday.day, MONTHS[birthday.month-1])
print()

match = getMatch(birthdays)

# Display the results
print('In this simulation, ', end=' ')
if match != None:
    month_name = MONTHS[match.month - 1]
    dateText = f'{month_name} {match.day}'
    print('multiple people have a birthday on', dateText)
else:
    print("there are no matching birthdays.")

print()

print('Let\'s test 100,000 simulations.')
simMatch = 0

for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run ...')
    birthdays = get_birthdays(numDays)
    if getMatch(birthdays) != None:
        simMatch += 1

print('100,000 simulation run.')
p = simMatch/100_000*100
print(p, "%")
