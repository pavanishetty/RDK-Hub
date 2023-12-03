# import required modules
import requests, json
 
# API key generated from openweathermap
apiKey = "53eaaec0f3ca78aea752689cea6d3e61"
 
# base_url variable to store url
baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
 

# weatherDetails: prints current temperature, atmospheric pressure, humidity and weather description
def weatherDetails(cityName):
    # completeUrl: stores complete url address
    completeUrl = baseUrl + "appid=" + apiKey + "&q=" + cityName

    # response: stores response object
    response = requests.get(completeUrl)

    # result: contains attributes as List 
    result = response.json()
    

    # if cod value is equal to 404 then city is existing otherwise city not found
    if result["cod"] != "404":
        weatherList = result["main"]
 
        # currTemp: stores current temperature of given city in kelvin unit
        currTemp = weatherList["temp"]

        # currHumidity: stores current humidity as percentage
        currHumidity = weatherList["humidity"]
        
        # currPressure: stores current atmospheric pressure in hPa unit
        currPressure = weatherList["pressure"]
 
        
        k = result["weather"]
        weatherCond = k[0]["description"]
 
        print("\n City Name = " + str(cityName))
        print("\n Temperature = " +
                    str(currTemp) +
          "\n atmospheric pressure = " +
                    str(currPressure) +
          "\n humidity = " +
                    str(currHumidity) +
          "\n description = " +
                    str(weatherCond))
    else:
        print(" City Not Found ")

# Give city name
cityName = input("Enter city name : ")
weatherDetails(cityName)

#favorite_cities: stores maximum of 3 favorite cities of users
favorite_cities = []

# takes input from the user for 3 times to store favorite city into list 
while len(favorite_cities) < 3:
    favorite_city = input("Enter your favorite city ")
    favorite_cities.append(favorite_city)

else:
    res = input("Do you want to enter more cities yes/no")
    if res == "no":
        pass
    else:
        # if list contains 3 favorite cities, then user will be prompted to delete one city
        print("You reached maximum limit for adding favorite cities")
        print("Please delete one city from the list")
        delete_city = input("Enter city name to be deleted from favorite list ")
        favorite_cities.remove(delete_city)

        favorite_city = input("Enter your favorite city ")
        favorite_cities.append(favorite_city)

# list favoritie cities along with current weather details
print("Favorite Cities", favorite_cities)
count = len(favorite_cities)
i = 0
while count > 0:
    weatherDetails(favorite_cities[i])
    count = count - 1
    i = i + 1
                   


    
