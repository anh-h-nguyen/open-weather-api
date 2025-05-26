# ⛅ OpenWeather API

## Technologies Used
- Programming Language: Python  
- Libraries: requests  
- API Used: OpenWeather API  

## Project Overview
This Python script allows users to look up current weather conditions in the United States using either a zip code or a city and state. Users can also specify their preferred temperature unit (Fahrenheit, Celsius, or Kelvin). The program fetches data from the OpenWeather API, processes it, and displays key weather details interactively.

## Table of Contents
1. Introduction  
2. Features  
3. How It Works  
4. Usage Instructions  
5. Future Improvements  

## Introduction
The Weather Lookup API project is designed to provide users with real-time weather data for any U.S. location using zip codes or city names. The program:
- Allows users to choose their preferred temperature unit (Fahrenheit, Celsius, or Kelvin).
- Retrieves weather data from the OpenWeather API.
- Displays temperature, humidity, pressure, and general weather conditions.
- Handles invalid inputs with helpful error messages.

## Features
- Interactive Temperature Selection: Users can choose between Fahrenheit, Celsius, or Kelvin.  
- Multiple Location Options: Look up weather by zip code or city and state.  
- Detailed Weather Information: Displays temperature, humidity, pressure, and more.  
- Error Handling: Ensures proper input validation and displays helpful messages if an issue arises.  

## How It Works
1. User selects temperature unit (Fahrenheit, Celsius, or Kelvin).  
2. User chooses location method (zip code or city/state).  
3. The script fetches coordinates (latitude & longitude) using OpenWeather’s geo API.  
4. Weather data is retrieved using the coordinates and displayed to the user.  

## Usage Instructions
1. Install dependencies (if needed):* 
   ```bash
   pip install requests

## Future Improvements
- Expand location support to international cities.
- Implement 5-day forecasts for extended weather predictions.
- Add additional weather metrics like wind speed and air quality.
- Build a GUI or web app for a more interactive user experience.
