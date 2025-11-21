MENU = {'sandwich': 10, 'tea': 7, 'salad': 9} 


def resturant():
    total=0

    while True:

        order = input('order: ').strip()

        if not order:
            break 

        if order in MENU:
            total += MENU[order]
            print(f'{order} is {MENU[order]}, total is {total}')

        else:
            print(f'we are fresh out of {order} today ..!')

    
    print(f'your total is {total}')

#resturant()


############################# SIMPLE LOGIN ################################

USERS = {'root': '1234', 'ceo': '!!!!!', 'reuven': 'GrEaTpW?'}


def simple_login():

    while True:
        user = input(f'Enter Username: ').strip()
        password = input (f'Enter password: ').strip() 

        # if user in USERS and USERS[user] == password:
        #     print(f'you have succesfull logged in...!')

        # else:
        #     print('Kindly retry again..! with correct username & password ')

        if USERS.get(user) == password:
            print(f'you have succesfull logged in...!')
            break
        else:
            print('Kindly retry again..! with correct username & password ')

#simple_login()        


#"""Solution to chapter 4, exercise 14: beyond 2: temps"""

from datetime import datetime, timedelta, date 


TEMPS = {'2020-08-16': 30,
         '2020-08-17': 32,
         '2020-08-18': 32,

         }


def temps():
    while True:
        today = input("Enter date in YYYY-MM-DD format:").strip()

        if not today:
            break

        if len(today) != 10:
            print(f'Invalid format; try again. ')
            continue

        if today.count('-') != 2:
            print(f'Invalid format; try again. ')
            continue

        if today not in TEMPS:
            print(f'The date {today} is unknown; try again. ')
            continue

        try:
            today_date = datetime.fromisoformat(today).date() ## converting string to datetime.date datatype 
            # print(today_date)
            # print(type(today_date))
        except ValueError as e:
            print(f'Not a valid date string; try again. ')
            continue

        yesterday_date = str(today_date - timedelta(1)) ## if date format is datetime.date then only we can use timedelta 
        tomorrow_date = str(today_date + timedelta(1))

        print(f'{yesterday_date}: {TEMPS.get(yesterday_date, "No data available")}')
        print(f'{today_date}: {TEMPS[str(today_date)]}')
        print(f'{tomorrow_date}: {TEMPS.get(tomorrow_date, "No data available")}')


#temps()

## """Solution to chapter 4, exercise 14: beyond 3: days_old"""



PEOPLE = {'abhilash': '1992-08-03',
          'aashish': '1999-07-28',
          'rainuka':'1993-06-02',
          'Amotz': date.fromisoformat('2005-10-31')
          }

def calculate_days():
    while True:
        name = input("Enter a person's name: ").strip()

        if not name:
            break

        today = date.today()

        if name in PEOPLE:
            print(datetime.fromisoformat(PEOPLE[name]).date())
            print(f'{name} is {(today - datetime.fromisoformat(PEOPLE[name]).date())}')
        else:
            print(f'{name} is not in the system.')

calculate_days()