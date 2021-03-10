import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_valid = False
    while city_valid == False:
        city = input("Of which city do you want to explore bikeshare data: \n"
                     "'Chicago', 'New York City' or 'Washington'?\n"
                     "Type in the city, its first letter or 1, 2, 3, respectively:\n")
        valid_cities = {'chicago': ['chicago', 'c', '1'],
                        'new york city': ['new york city', 'new york', 'n', 'nyc', '2'],
                        'washington': ['washington', 'w', '3']}
        for key, value in valid_cities.items():
            if str(city).lower().strip() in value:
                city = key
                city_valid = True
                break
        else:
            print('\n-----Please enter a valid city!-----\n\n')

    # get user input for month (all, january, february, ... , june)
    month_valid = False
    while month_valid == False:
        month = input("Of which month (January to June) would you like do see data?\n"
                      "If you don\'t want to filter by month, type 'all' or '0'!\n"
                      "Type in the month, its first three letters or '1', '2' or '3' etc., respectively:\n")
        valid_months = {'all': ['all', '0'],
                        'january': ['january', 'jan', '1'],
                        'february': ['february', 'feb', '2'],
                        'march': ['march', 'mar', '3'],
                        'april': ['april', 'apr', '4'],
                        'may': ['may', '5'],
                        'june': ['june', 'jun', '6']}
        for key, value in valid_months.items():
            if str(month).lower().strip() in value:
                month = key
                month_valid = True
                break
        else:
            print('\n-----Please enter a valid month!-----\n\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_valid = False
    while day_valid == False:
        day = input("Of which day of the week (Monday to Sunday) would you like do see data?\n"
                    "If you don\'t want to filter by day type, 'all' or '0'!\n"
                    "Type in the day, its first three letters or '1' for Monday, '2' for Tuesday etc.:\n")
        valid_days = {'all': ['all', '0'],
                      'monday': ['monday', 'mon', '1'],
                      'tuesday': ['tuesday', 'tue', '2'],
                      'wednesday': ['wednesday', 'wed', '3'],
                      'thursday': ['thursday', 'thu', '4'],
                      'friday': ['friday', 'fri', '5'],
                      'saturday': ['saturday', 'sat', '6'],
                      'sunday': ['sunday', 'sun', '7']}
        for key, value in valid_days.items():
            if str(day).lower().strip() in value:
                day = key
                day_valid = True
                break
        else:
            print('\n-----Please enter a valid day of the week!-----\n\n')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower())+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # index of the day list to get the correspondig int
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day.lower())

        # filter by day of week to create the new dataframe
        df =  df[df['day_of_week']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print(df.head())
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    mode_month = df['month'].mode()[0]
    print('The month with the most times of travel:', mode_month)
    # display the most common day of week
    mode_day = df['day_of_week'].mode()[0]
    print('The day of week with the most times of travel:', mode_day)
    # display the most common start hour
    mode_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour:', mode_hour)

    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('-'*40)
#
#
# def station_stats(df):
#     """Displays statistics on the most popular stations and trip."""
#
#     print('\nCalculating The Most Popular Stations and Trip...\n')
#     start_time = time.time()
#
#     # display most commonly used start station
#
#
#     # display most commonly used end station
#
#
#     # display most frequent combination of start station and end station trip
#
#
#     print("\nThis took {} seconds.".format(time.time() - start_time))
#     print('-'*40)
#
#
# def trip_duration_stats(df):
#     """Displays statistics on the total and average trip duration."""
#
#     print('\nCalculating Trip Duration...\n')
#     start_time = time.time()
#
#     # display total travel time
#
#
#     # display mean travel time
#
#
#     print("\nThis took {} seconds.".format(time.time() - start_time))
#     print('-'*40)
#
#
# def user_stats(df):
#     """Displays statistics on bikeshare users."""
#
#     print('\nCalculating User Stats...\n')
#     start_time = time.time()
#
#     # Display counts of user types
#
#
#     # Display counts of gender
#
#
#     # Display earliest, most recent, and most common year of birth
#
#
#     print("\nThis took {} seconds.".format(time.time() - start_time))
#     print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
#        station_stats(df)
#        trip_duration_stats(df)
#        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()


# filename = 'chicago.csv'
#
# # load data file into a dataframe
# df = pd.read_csv(filename)
#
# # convert the Start Time column to datetime
# df['Start Time'] = pd.to_datetime(df['Start Time'])
#
# # extract hour from the Start Time column to create an hour column
# df['hour'] = df['Start Time'].dt.hour
#
# # find the most common hour (from 0 to 23)
# popular_hour = df['hour'].value_counts().idxmax()
# # !!!!OR popular_hour = df['hour'].mode()[0]!!!!
#
# print('Most Frequent Start Hour:', popular_hour)
