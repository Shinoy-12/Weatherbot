# Installation
Refer my Chatbot-song-link repo for the installation process and about the basics of RASA components.

# Weatherbot
-- ML based conversational chatbot which tells you about the city's temperature. This bot uses the IP address of your laptop and tells you about the temp. of your city. It also tells us the temperature of some user selected city.
-- Integrating your Project with Messanger
-- Saving your Conversations in MongoDb and extracting it. 


## How to use this Project--
1. Clone or download this repo into your computer
2. Make sure to have all the dependency in your computer
3. Set your working directory to this downloaded folder in terminal
4. Open terminal.
5. $ rasa train (trains your model) this will start a port on 5055 which will handl custom actions
6. $ rasa run actions (Starts an action server using the Rasa SDK.)
7. $ rasa shell --endpoints endpoints.yml

For more Command Line Interface ref- (https://rasa.com/docs/rasa/user-guide/command-line-interface/)

# Use of API-
-- https://openweathermap.org/ 
Login into it ,read the *Documentation*, it will provide you with the personal API key.

# Integration with Messanger
refer - https://rasa.com/docs/rasa/user-guide/connectors/facebook-messenger/#id1
or
refer - https://medium.com/@tatiana.parshina/connecting-rasa-ai-chatbot-to-facebook-messenger-6d024e642dbd

# Tracker
refer - https://rasa.com/docs/rasa/api/tracker-stores/

1. hi
2. Hey! Weather Bot here. What is ur name?
3. my name is shinoy
4. Shinoy which city weather you want to know?
5. /get_weather{"current":"current"}
6. Temp in your city is 18.06
7. thank you
8. Have a nice day
9. /restart
10. hy
11. hello
12. Hey! Weather Bot here. What is ur name?
13. my name is shinoy
14. Shinoy which city weather you want to know?
15. /get_weather{"others":"other"}
16. Select state
17. jaipur
18.Temp in your city is 25
