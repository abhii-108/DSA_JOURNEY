#"""Solution to chapter 4, exercise 15: rainfall"""

def get_rainfall():
    """Ask the user repeatedly for a city name and mm of rainfall.

If the city is blank, then stop asking questions,
and report all cities and rainfall.

Otherwise, ask for rainfall and add the current rainfall
to any previous report for that city.
"""
    rainfall = {}

    while True:
        cityname = input(f'Enter city name: ').strip()

        if not cityname:
            break 
        
        try:
            mm_rain = int(input(f'Enter mm rain: ').strip())
        except ValueError:
            print(f'Enter valid integer number')

        
        rainfall[cityname] = rainfall.get(cityname, 0) + mm_rain


        for city, rain in rainfall.items():
            print(f'{city} : {rain}')

get_rainfall()
