from Skills.Acore import speak, record_action
import webbrowser
import geocoder
import requests

# Weather forecast
def weather_forecast():
    try:
        print('Getting your weather forecast')
        speak('Getting your weather forecast')
        webbrowser.open('https://www.google.com/search?q=weather+forecast')
        print('Search completed')   
        speak('Search completed')
        record_action('Weather forecast')
    except Exception as e:
        print("An error has occurred in the weather_forecast command, output has been sent to errors.log")
        speak("An error has occurred in the weather_forecast command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write("weather_forecast: " + str(e) + "\n")

# Current weather
def get_current_weather():
    try:
        g = geocoder.ip('me', timeout=10)
        latitude, longitude = g.latlng
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        response = requests.get(url)
        data = response.json()
        temperature = str(data['current_weather']['temperature'])
        wind_speed = str(data['current_weather']['windspeed'])
        weather_type = str(data['current_weather']['weathercode'])
        if weather_type == '0':
            weather_type = ' weather type is unkown, cloud development not observed or not observable'
        elif weather_type == '1': 
            weather_type = 'the sky is becoming clear, clouds are generally disolving or becoming less developed'
        elif weather_type == '2': 
            weather_type = 'the sky is clear'
        elif weather_type == '3': 
            weather_type = 'the sky is almost clear, clouds are forming'
        elif weather_type == '4': 
            weather_type = 'the sky visibility is reduced due to smoke, possible due to examples like forest fires, industrial smoke or volcanic ashes'
        elif weather_type == '5': 
            weather_type = 'the sky is hazey'
        elif weather_type == '6': 
            weather_type = 'there is widespread dust in suspension in the air, not raised by wind at or near the station at the time of observation'
        elif weather_type == '7': 
            weather_type = 'dust or sand raised by wind at or near the station at the time of observation, but no well developed dust whirl(s) or sand whirl(s), and no duststorm or sandstorm seen'
        elif weather_type == '8': 
            weather_type = 'there are well developed dust whirl(s) or sand whirl(s) seen at or near the station during the preceding hour or at the time ot observation, but no duststorm or sandstorm'
        elif weather_type == '9': 
            weather_type = 'there is a duststorm or sandstorm within sight at the time of observation, or at the station during the preceding hour'
        elif weather_type == '10': 
            weather_type = 'the weather is misty'
        elif weather_type == '11': 
            weather_type = 'there are patches of rain in the area'
        elif weather_type == '12': 
            weather_type = 'there is more or less continous rain'
        elif weather_type == '13': 
            weather_type = 'there is lightning visible, no thunder heard'
        elif weather_type == '14': 
            weather_type = 'there is precipitation in sight, but is not reaching the ground or surface of the sea'
        elif weather_type == '15': 
            weather_type = 'there is precipitation within sight, reaching the ground or the surface of the sea, but distant, i.e. estimated to be more than 5 km from the station'
        elif weather_type == '16': 
            weather_type = 'there is precipitation within sight, reaching the ground or the surface of the sea, near to, but not at the station'
        elif weather_type == '17': 
            weather_type = 'there is a thunderstorm, but no precipitation at the time of observation'
        elif weather_type == '18': 
            weather_type = 'there are gusts of winds or a localized storm'
        elif weather_type == '19': 
            weather_type = 'funnel cloud(s) have been observed'
        elif weather_type == '20': 
            weather_type = 'there is a Drizzle (not freezing) or snow grains'
        elif weather_type == '21': 
            weather_type = 'there is rain (not freezing)'
        elif weather_type == '22': 
            weather_type = 'there is snow'
        elif weather_type == '23': 
            weather_type = 'there is rain and snow or ice pellets'
        elif weather_type == '24': 
            weather_type = 'there is a freezing drizzle or freezing rain'
        elif weather_type == '25': 
            weather_type = 'shower(s) of rain have been observed'
        elif weather_type == '26': 
            weather_type = 'shower(s) of snow, or of rain and snow have been observed'
        elif weather_type == '27': 
            weather_type = 'shower(s) of hail, or of rain and hail have been observed'
        elif weather_type == '28': 
            weather_type = 'fog or ice fog has been observed'
        elif weather_type == '29': 
            weather_type = 'there is a thunderstorm (with or without precipitation)'
        elif weather_type == '30': 
            weather_type = 'there is a slight or moderate duststorm or sandstorm'
        elif weather_type == '31': 
            weather_type = 'there is a slight or moderate duststorm or sandstorm'
        elif weather_type == '32': 
            weather_type = 'there is a slight or moderate duststorm or sandstorm'
        elif weather_type == '33': 
            weather_type = 'there is a severe duststorm or sandstorm'
        elif weather_type == '34': 
            weather_type = 'there is a severe duststorm or sandstorm'
        elif weather_type == '35': 
            weather_type = 'there is a severe duststorm or sandstorm'
        elif weather_type == '36': 
            weather_type = 'there is a slight or moderate blowing snow'
        elif weather_type == '37': 
            weather_type = 'there is a heavy drifting snow'
        elif weather_type == '38': 
            weather_type = 'there is a slight or moderate blowing snow'
        elif weather_type == '39': 
            weather_type = 'there is a heavy drifting snow'
        elif weather_type == '40': 
            weather_type = 'there is a fog or ice fog at a distance at the time of observation, but not at the station during the preceding hour, the fog or ice fog extending to a level above that of the observer'
        elif weather_type == '41': 
            weather_type = 'there is a fog or ice fog in patches'
        elif weather_type == '42': 
            weather_type = 'there is a fog or ice fog, sky is visible'
        elif weather_type == '43': 
            weather_type = 'there is a fog or ice fog, sky is invisible'
        elif weather_type == '44': 
            weather_type = 'there is a fog or ice fog, sky is visible'
        elif weather_type == '45': 
            weather_type = 'there is a fog or ice fog, sky is invisible'
        elif weather_type == '46': 
            weather_type = 'there is a fog or ice fog, sky is visible'
        elif weather_type == '47': 
            weather_type = 'there is a fog or ice fog, sky is invisible'
        elif weather_type == '48': 
            weather_type = 'there is a fog, depositing rime, sky is visible'
        elif weather_type == '49': 
            weather_type = 'there is a fog, depositing rime, sky is invisible'
        elif weather_type == '50': 
            weather_type = 'there is a drizzle, not freezing, intermittent'
        elif weather_type == '51': 
            weather_type = 'there is a drizzle, not freezing, continuous'
        elif weather_type == '52': 
            weather_type = 'there is a drizzle, not freezing, intermittent'
        elif weather_type == '53': 
            weather_type = 'there is a drizzle, not freezing, continuous'
        elif weather_type == '54': 
            weather_type = 'there is a drizzle, not freezing, intermittent'
        elif weather_type == '55': 
            weather_type = 'there is a drizzle, not freezing, continuous'
        elif weather_type == '56': 
            weather_type = 'there is a drizzle, freezing, slight'
        elif weather_type == '57': 
            weather_type = 'there is a drizzle, freezing, moderate or heavy (dence)'
        elif weather_type == '58': 
            weather_type = 'there is a drizzle and rain, slight'
        elif weather_type == '59': 
            weather_type = 'there is a drizzle and rain, moderate or heavy'
        elif weather_type == '60': 
            weather_type = 'there is rain, not freezing, intermittent'
        elif weather_type == '61': 
            weather_type = 'there is rain, not freezing, continuous'
        elif weather_type == '62': 
            weather_type = 'there is rain, not freezing, intermittent'
        elif weather_type == '63': 
            weather_type = 'there is rain, not freezing, continuous'
        elif weather_type == '64': 
            weather_type = 'there is rain, not freezing, intermittent'
        elif weather_type == '65': 
            weather_type = 'there is rain, not freezing, continuous'
        elif weather_type == '66': 
            weather_type = 'there is rain, freezing, slight'
        elif weather_type == '67': 
            weather_type = 'there is rain, freezing, moderate or heavy (dence)'
        elif weather_type == '68': 
            weather_type = 'there is rain or drizzle and snow, slight'
        elif weather_type == '69': 
            weather_type = 'there is rain or drizzle and snow, moderate or heavy'
        elif weather_type == '70': 
            weather_type = 'there is an intermittent fall of snowflakes'
        elif weather_type == '71': 
            weather_type = 'there is a continuous fall of snowflakes'
        elif weather_type == '72': 
            weather_type = 'there is an intermittent fall of snowflakes'
        elif weather_type == '73': 
            weather_type = 'there is a continuous fall of snowflakes'
        elif weather_type == '74': 
            weather_type = 'there is an intermittent fall of snowflakes'
        elif weather_type == '75': 
            weather_type = 'there is a continuous fall of snowflakes'
        elif weather_type == '76': 
            weather_type = 'there is diamond dust (with or without fog)'
        elif weather_type == '77': 
            weather_type = 'there are now grains (with or without fog)'
        elif weather_type == '78': 
            weather_type = 'there are isolated star-like snow crystals (with or without fog)'
        elif weather_type == '79': 
            weather_type = 'there are ice pellets'
        elif weather_type == '80': 
            weather_type = 'slight rain shower(s) have been observed'
        elif weather_type == '81': 
            weather_type = 'moderate or heavy rain shower(s) have been observed'
        elif weather_type == '82': 
            weather_type = 'violent rain shower(s) have been observed'
        elif weather_type == '83': 
            weather_type = 'slight shower(s) of rain and snow mixed have been observed'
        elif weather_type == '84': 
            weather_type = 'moderate or heavy shower(s) of rain and snow mixed have been observed'
        elif weather_type == '85': 
            weather_type = 'slight snow shower(s) have been observed'
        elif weather_type == '86': 
            weather_type = 'moderate or heavy snow shower(s) have been observed'
        elif weather_type == '87': 
            weather_type = 'shower(s) of snow pellets or small hail, with or without rain or rain and snow mixed have been observed'
        elif weather_type == '88': 
            weather_type = 'shower(s) of snow pellets or small hail, with or without rain or rain and snow mixed have been observed'
        elif weather_type == '89': 
            weather_type = 'shower(s) of hail, with or without rain or rain and snow mixed that are not associated with thunder have been observed'
        elif weather_type == '90': 
            weather_type = 'shower(s) of hail, with or without rain or rain and snow mixed that are not associated with thunder have been observed'
        elif weather_type == '91': 
            weather_type = 'there is slight rain at time of observation'
        elif weather_type == '92': 
            weather_type = 'there is moderate or heavy rain at time of observation'
        elif weather_type == '93': 
            weather_type = 'there is slight snow, or rain and snow mixed or hail at time of observation'
        elif weather_type == '94': 
            weather_type = 'moderate or heavy snow, or rain and snow mixed or hail at time of observation'
        elif weather_type == '95': 
            weather_type = 'there is a thunderstorm, slight or moderate, without hail but with rain and/or snow at time of observation'
        elif weather_type == '96': 
            weather_type = 'there is a thunderstorm, slight or moderate, with hail at time of observation'
        elif weather_type == '97': 
            weather_type = 'there is a thunderstorm, heavy, without hail but with rain and/or snow at time of observation'
        elif weather_type == '98': 
            weather_type = 'there is a thunderstorm combined with duststorm or sandstorm at time of observation'
        elif weather_type == '99': 
            weather_type = 'there is a thunderstorm, heavy, with hail at time of observation'
        print('The temperature is at ' + temperature + ' degrees Celcius, wind speed is ' + wind_speed + ' meters per second and ' + weather_type)
        speak('The temperature is at ' + temperature + ' degrees Celcius, wind speed is ' + wind_speed + ' meters per second and ' + weather_type)
        record_action(f"Getting weather - Temp: {temperature}, Wind speed: {wind_speed}, Weather Type: {weather_type}")
    except Exception as e:
        print("An error has occurred in the get_current_weather command, output has been sent to errors.log")
        speak("An error has occurred in the get_current_weather command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write("get_current_weather: " + str(e) + "\n")
# Website: https://www.meteomatics.com/en/api/available-parameters/derived-weather-and-convenience-parameters/general-weather-state/