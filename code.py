# Import libraries
import requests

# Establish settings and API Key
country_code = 'US'
api_key = "INSERT API"

# This function requests for the user's preferred type of measurement for temperature.
# This function will loop until the user has inputted one of the three available choices.
def temp_selection():
    print("Welcome! To start off, please confirm what type of measurement you would like to see the temperatures in.")
    while True:
        user_temp_type = str(input("You can choose from: \n 1) fahrenheit \n 2) celsius \n 3) kelvin "
                                   "\n Your selection: "))
        user_temp_type = user_temp_type.lower()
        if user_temp_type != 'fahrenheit' and user_temp_type != 'celsius' and user_temp_type != 'kelvin':
            print("Sorry! That was an invalid selection.")
        else:
            break
    converted_temp_type = temp_conversion(user_temp_type)
    return converted_temp_type

# This function takes the user's preferred type of measurement for temperature as a parameter and converts
# the variable to the OpenWeather's terminology and vice versa.
def temp_conversion(temp_type):
    if temp_type == 'fahrenheit':
        temp_type = 'imperial'
    elif temp_type == 'imperial':
        temp_type = 'fahrenheit'
    elif temp_type == 'celsius':
        temp_type = 'metric'
    elif temp_type == 'metric':
        temp_type = 'celsius'
    elif temp_type == 'kelvin':
        temp_type = ''
    else:
        temp_type = 'kelvin'
    return temp_type

# This function takes the temperature type as a parameter and requests to search for
# current weather by US zip code or city and state.
# This function will loop until the user has inputted one of the two available choices.
# It then calls upon either the zip code or city look up functions, passing the temperature type as a parameter.
def loc_selection(temp_type):
    print("Next, please confirm the US location.")
    while True:
        loc_type = str(input("You can look up by a US: \n 1) zip code\n 2) city and state \n Your selection: "))
        loc_type = loc_type.lower()
        if loc_type != 'zip code' and loc_type != 'city and state':
            print("Sorry! That was an invalid answer.")
        else:
            break
    if loc_type == 'zip code':
        zip_code_lookup(temp_type)
    else:
        city_lookup(temp_type)

# This function takes the temperature type as a parameter and requests the user to input a zip code.
# This function will loop until the user has inputted a valid answer.
# It will request the location data from the OpenWeather API and extract the latitude and longitude.
# It then calls upon the latitude and longitude look up function, passing the
# latitude, longitude, and temperature type as parameters.
def zip_code_lookup(temp_type):
    while True:
        zip_code = input("Please enter the US zip code: ")
        retrieve_zip_code_data = requests.get('http://api.openweathermap.org/geo/1.0/zip?zip=' + str(zip_code) + ',' +
                                              str(country_code) + '&appid=' + str(api_key))
        try:
            retrieve_zip_code_data.raise_for_status()
        except requests.exceptions.HTTPError:
            print("Sorry! The program is running into error " + str(retrieve_zip_code_data.status_code) + ": "
                  + retrieve_zip_code_data.reason + "." +
                  "\n You can check out 'https://openweathermap.org/faq' for more information on API "
                  "error codes and their meanings. Please fix your error and try again.")
        else:
            break
    data = retrieve_zip_code_data.json()
    lat = data.get('lat')
    lon = data.get('lon')
    lat_long_lookup(lat, lon, temp_type)

# This function takes the temperature type as a parameter and requests the user to input a city and state.
# This function will loop until the user has inputted a valid answer.
# It will request the location data from the OpenWeather API and extract the latitude and longitude.
# It then calls upon the latitude and longitude look up function, passing the
# latitude, longitude, and temperature type as parameters.
def city_lookup(temp_type):
    while True:
        city = input("Please enter the US city: ")
        state = input("Please enter the US state abbreviations: ")
        retrieve_city_data = requests.get('http://api.openweathermap.org/geo/1.0/direct?q=' + str(city) + ',' +
                                          str(state) + ',' + str(country_code) + '&appid=' + str(api_key))
        data = retrieve_city_data.json()
        try:
            retrieve_city_data.raise_for_status()
        except requests.exceptions.HTTPError:
            print("Sorry! The program is running into error " + str(retrieve_city_data.status_code) + ": "
                  + retrieve_city_data.reason + "." +
                  "\n You can check out 'https://openweathermap.org/faq' for more information on API "
                  "error codes and their meanings.")
        else:
            if len(data) == 0:
                print("Sorry! That was an invalid US city and state. "
                      "The city name should be fully written out and the state should only be 2 letters.")
            else:
                break
    lat = data[0]['lat']
    lon = data[0]['lon']
    lat_long_lookup(lat, lon, temp_type)

# This function takes the latitude, longitude, and the temperature type
# as parameters and requests the current weather from the OpenWeather API.
# It then calls upon the final message function and passes the data and temp type as parameters.
def lat_long_lookup(lat, lon, temp_type):
    while True:
        retrieve_lat_lon_data = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) +
                                             '&lon=' + str(lon) + '&units=' + str(temp_type) + '&appid=' + str(api_key))
        data = retrieve_lat_lon_data.json()
        try:
            retrieve_lat_lon_data.raise_for_status()
        except requests.exceptions.HTTPError:
            print("Sorry! The program is running into error " + str(retrieve_lat_lon_data.status_code) + ": "
                  + retrieve_lat_lon_data.reason + "." +
                  "\n You can check out 'https://openweathermap.org/faq' for more information on API "
                  "error codes and their meanings.")
        else:
            break
    final_message(data, temp_type)

# This function takes the weather data and temperature type. It then converts the temperature type back into
# the user's inputted preference using the temp conversion function to be able to be restated back to the user.
# This function then prints out the details of the current weather conditions.
def final_message(data, temp_type):
    temp_type = temp_conversion(temp_type)
    print("The current weather conditions in " + data['name'] + ":")
    print("Current temp: " + str(data['main']['temp']) + "° " + temp_type)
    print("Feels like: " + str(data['main']['feels_like']) + "° " + temp_type)
    print("Highest temp: " + str(data['main']['temp_max']) + "° " + temp_type)
    print("Lowest temp: " + str(data['main']['temp_min']) + "° " + temp_type)
    print("Pressure: " + str(data['main']['pressure']) + "hPa")
    print("Humidity: " + str(data['main']['humidity']) + "%")
    print("Description: " + str(data['weather'][0]['description']))

# This is the main method and will loop the entire program until the user inputs 'q' to quit.
def main():
    sentinel_value = 'q'
    answer = ''
    while answer != sentinel_value:
        temp_type = temp_selection()
        loc_selection(temp_type)
        answer = input("Enter 'q' to quit or enter any other key to restart. \n Your selection: ")
        answer = answer.lower()
    print("Program has ended. Thanks for visiting!")

if __name__ == "__main__":
    main()

