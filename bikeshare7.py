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
    print('Hello! Let\'s explore some US bikeshare data! Shall we?!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Let's start! Select one of the available Cities: Chicago, New York City or Washington. -> ").strip().lower()

        if city in CITY_DATA:
            print(f'Found! {city} → {CITY_DATA[city]}')
            break
        else:
            print('\nNot found. Please try again.')

    while True:
        choose_filter = ['month', 'weekday', 'both', 'none']
        filter = input('Choose a filter: month, weekday, both or none. -> ').strip().lower()
        
        if filter in choose_filter:
            print('You chose: {}'.format(filter))
            
            while filter == 'month':
                choose_month = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
                month = input("\nChoose a month: all, january, february, ... , june. -> ").strip().lower()

                if month in choose_month:
                    print('You chose: {}'.format(month))
                    day ='all'
                    break
                else:
                    print('\nNot found. Please try again.')
                    continue                
                                 
            while filter == 'weekday':
                choose_day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
                day = input("\nChoose a weekday: all, monday, tuesday, ... sunday. -> ").strip().lower()

                if day in choose_day:
                    print('You chose: {}'.format(day))
                    month = 'all'
                    break
                else:
                    print("\nNot found. Please try again.")
                    continue

            while filter == 'both':
                choose_month = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
                month = input("\nChoose a month: all, january, february, ... , june. -> ").strip().lower()

                if month in choose_month:
                    print('You chose: {}'.format(month))

                    while True:
                        choose_day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
                        day = input("\nChoose a weekday: all, monday, tuesday, ... sunday. -> ").strip().lower()

                        if day in choose_day:
                            print('You chose: {}'.format(day))
                            break
                        else:
                            print("\nNot found. Please try again.")
                            continue
                else:
                    print('\nNot found. Please try again.')
                    continue
                
                break

            if filter == 'none':

                month = 'all'

                day = 'all'

                break
            
            break

        else:
            print('\nNot found. Please try again.')
  
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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        df = df[df['month'] == int(month)]

    if day != 'all':
        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = weekdays.index(day)

        df = df[df['day_of_week'] == int(day)] 
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].value_counts().idxmax()
    display_months = ['January', 'February', 'March', 'April', 'May', 'June']
    print("The most common month is: {}".format(display_months[common_month-1]))

    # display the most common day of week
    common_weekday = df['day_of_week'].value_counts().idxmax()
    display_weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print("The most common weekday is: {}".format(display_weekday[common_weekday]))

    #display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is: {} o'clock".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].value_counts().idxmax()
    print("The most common start station is: {}".format(common_start))

    # display most commonly used end station
    common_end = df['End Station'].value_counts().idxmax()
    print("The most common end station is: {}".format(common_end))

    # display most frequent combination of start station and end station trip
    count_combination = df.groupby(['Start Station', 'End Station']).size()
    common_combination = count_combination.idxmax()
    print("The most frequent combination of stations is: {}".format(common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time_total = df['Trip Duration'].sum()
    print("The total travel time is: {} seconds".format(travel_time_total))

    # display mean travel time
    travel_time_mean = df['Trip Duration'].mean()
    print("The average travel time is: {} seconds".format(travel_time_mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print("The counts of user types is: {}\n".format(count_user_types))

    # Display counts of gender

    while True:

        if 'Gender' in df.columns:
            count_gender = df['Gender'].value_counts()

            print("The counts of gender is: {}\n".format(count_gender))

            break

        else:
            print("\nGender is not included in dataset.")

            break


    # Display earliest, most recent, and most common year of birth
    while True:

        if 'Birth Year' in df.columns:
            birth_earliest = df['Birth Year'].min()
            birth_recent = df['Birth Year'].max()
            birth_common = df['Birth Year'].value_counts().idxmax()

            print("The earliest year of birth is: {}".format(int(birth_earliest)))
            print("The most recent year of birth is: {}".format(int(birth_recent)))
            print("The most common year of birth is: {}".format(int(birth_common)))

            break

        else:
            print("\nBirth year is not included in dataset.")

            break
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays raw data of chosen csv if wanted."""

    row_index = 0
    total_rows = len(df)
    start_row = 0
    end_row = 5

    while True:
        
        raw_data = input('Do you want to see 5 (more) rows of raw data: yes or no? -> ').strip().lower()

        if raw_data == 'yes':
            
            if row_index < total_rows:
                print(df.iloc[start_row:end_row])
                start_row += 5
                end_row += 5
                row_index += 5
            
            else:
                print('End of data.')
                break

        elif raw_data == 'no':
            break

        else:
            print('\nNot found. Please try again.')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
