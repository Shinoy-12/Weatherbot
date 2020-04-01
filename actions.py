# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action,Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
from rasa_sdk.events import SlotSet, FollowupAction
#
global cursor


class ActionHelloWorld(Action):

    def name(self):
        return "action_current_location"

    def run(self, dispatcher, tracker, domain) :
        r = requests.get("https://geolocation-db.com/json/0f761a30-fe14-11e9-b59f-e53803842572")
        t = r.json()
        city = t["city"]
        return [SlotSet("STATE",city)]


class ActionHelloUniverse(Action):

    def name(self):
        return "action_other_location"

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot("STATE")
        API1 = "73287e02418bc7e33a3bfa4650cf8022"
        a = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(location, API1))
        print(a)
        print(a.text)
        print(location)
        z = a.json()
        temp = z["main"]["temp"]
        print("hi")
        dispatcher.utter_message("Temp in your city is {}".format(temp))

        return []
