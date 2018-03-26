from weather import Weather, Unit
weather = Weather(unit=Unit.CELSIUS)

# Lookup WOEID via http://weather.yahoo.com.
loc = raw_input("Enter location:")
location = weather.lookup_by_location(loc)
condition = location.condition()
#forecast = location.forecast()
print(condition.temp()+" C")
print(condition.text())
#print(forecast)
