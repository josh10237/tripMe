import os
import kivy
import requests
import utils
import kivy.utils
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.slider import Slider
from kivy.uix.image import AsyncImage
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import os
from threading import Thread
from time import sleep

SCREEN_MANAGER = ScreenManager()
windowcolor = (0, .6, .6, 1)
personalData = ["name", "email", "age", "gender"]


class TripMe(App):
    def build(self):
        SCREEN_MANAGER.current = 'main'
        return SCREEN_MANAGER


Window.clearcolor = windowcolor


# main color: (3, 1, 1, 1)


class MainScreen(Screen):

    def getStarted(self):
        SCREEN_MANAGER.current = 'one'


class one(Screen):
    def __init__(self, **kwargs):
        Builder.load_file('one.kv')
        super(one, self).__init__(**kwargs)

    def whyDoWeAsk(self):
        SCREEN_MANAGER.current = 'why'

    def submitEmail(self):
        name = self.ids.name.text
        email = self.ids.email.text
        age = self.ids.age.text
        gender = self.ids.gender.text
        check = self.checkInfo(name, email, age, gender)
        if check == "Pass":
            personalData[0] = name
            personalData[1] = email
            personalData[2] = age
            personalData[3] = gender
            print(personalData)
            SCREEN_MANAGER.current = 'two'
        else:
            self.ids.info_error.text = check

    def checkInfo(self, name, email, age, gender):
        # if (name.find(" ") == -1):
        #     return "Name must have first and last seperated by space"
        # if (name.isdigit == True):
        #     return "Please enter a valid name"
        # if (len(name) < 5):
        #     return "Please enter a valid name"
        # if (email.find("@") == -1):
        #     return "Please enter a valid email"
        # if (email.find(".") == -1):
        #     return "Please enter a valid email"
        # if (email.find("com") == -1 and email.find("net") == -1):
        #     return "Please enter a valid email"
        # if (age.isdigit() == False):
        #     return "Please enter valid age"
        # if (len(age) != 2):
        #     return "Please enter a valid age"
        # if (gender != "Male") and (gender != "Female") and (gender != "male") and (gender != "female"):
        #     return "Please type Male or Female"
        # else:
        #     return "Pass"
        return "Pass"


class why(Screen):
    def __init__(self, **kwargs):
        Builder.load_file('why.kv')
        super(why, self).__init__(**kwargs)


class two(Screen):
    def __init__(self, **kwargs):
        Builder.load_file('two.kv')
        super(two, self).__init__(**kwargs)

    def search(self):
        SCREEN_MANAGER.current = 'search'


class search(Screen):
    def __init__(self, **kwargs):
        Builder.load_file('search.kv')
        super(search, self).__init__(**kwargs)

    def searchNow(self):
        location = self.ids.location_search.text
        result = self.apiCall(location)
        tmpList = list()
        for entry in (result["data"]):
            tmpList.append(entry["result_object"]["location_string"])


        tmpList = list(dict.fromkeys(tmpList))
        count = len(tmpList)
        fill = 10 - count
        for i in range(fill):
            tmpList.append("")

        self.ids.sResult1.text = tmpList[0]
        self.ids.sResult2.text = tmpList[1]
        self.ids.sResult3.text = tmpList[2]
        self.ids.sResult4.text = tmpList[3]
        self.ids.sResult5.text = tmpList[4]
        self.ids.sResult6.text = tmpList[5]
        self.ids.sResult7.text = tmpList[6]
        self.ids.sResult8.text = tmpList[7]
        self.ids.sResult9.text = tmpList[8]
        self.ids.sResult10.text = tmpList[9]

        if (fill == 10):
            self.ids.sResult1.text = "No Search Results"

    def sR1(self):
        if self.ids.sResult1.text == "":
             return
        self.dispSearchResult(self.ids.sResult1.text)
    def sR2(self):
        if self.ids.sResult1.text == "":
             return
        self.dispSearchResult(self.ids.sResult2.text)
    def sR3(self):
        if self.ids.sResult1.text == "":
             return
        self.dispSearchResult(self.ids.sResult3.text)
    def sR4(self):
        if self.ids.sResult1.text == "":
             return
        self.dispSearchResult(self.ids.sResult4.text)
    def sR5(self):
        if self.ids.sResult1.text == "":
             return
        self.dispSearchResult(self.ids.sResult5.text)
    def sR6(self):
        if self.ids.sResult1.text == "":
             return
        self.dispSearchResult(self.ids.sResult6.text)
    def sR7(self):
        if self.ids.sResult1.text == "":
             return
        self.dispSearchResult(self.ids.sResult7.text)
    def sR8(self):
        if self.ids.sResult1.text == "":
             return
        self.dispSearchResult(self.ids.sResult8.text)
    def sR9(self):
        if self.ids.sResult1.text == "":
             return
        self.dispSearchResult(self.ids.sResult9.text)
    def sR10(self):
        if self.ids.sResult1.text == "":
             return
        self.dispSearchResult(self.ids.sResult10.text)

    def dispSearchResult(self, locString):
        result = self.apiCall(locString)
        SRname = (result["data"][0]["result_object"]["location_string"])
        SRimg = (result["data"][0]["result_object"]["photo"]["images"]["large"]["url"])
        SRdescription = (result["data"][0]["result_object"]["geo_description"])
        resultParams = list()
        resultParams[0] = SRname
        resultParams[1] = SRimg
        resultParams[2] = SRdescription
        SCREEN_MANAGER.current = 'sresult'




    def apiCall(self, location):
        url = "https://tripadvisor1.p.rapidapi.com/locations/search"

        querystring = {"query": location, "lang": "en_US", "units": "mi"}

        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            'x-rapidapi-key': "7a0f0aff90msh861007d6addde50p1016a9jsn76f3d84a1cd0"
        }
        response = requests.get(url, headers=headers, params=querystring)
        result = response.json()
        print (response.text)
        return result


class sresult(Screen):
    def __init__(self, **kwargs):
        Builder.load_file('sresult.kv')
        super(sresult, self).__init__(**kwargs)


Builder.load_file('main.kv')
SCREEN_MANAGER.add_widget(MainScreen(name='main'))
SCREEN_MANAGER.add_widget(one(name='one'))
SCREEN_MANAGER.add_widget(why(name='why'))
SCREEN_MANAGER.add_widget(two(name='two'))
SCREEN_MANAGER.add_widget(search(name='search'))
SCREEN_MANAGER.add_widget(sresult(name='sresult'))



if __name__ == "__main__":
    TripMe().run()
