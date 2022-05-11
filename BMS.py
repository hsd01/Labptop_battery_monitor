import time
import pyttsx3
import psutil
from winotify import Notification, audio

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1])

def notify():
    t = Notification(app_id="HemantDhanwar",
                     title="LinkedIn Learning",
                     msg = "Hemant S D",
                     duration="long",
                     icon = 'D:/Itachi.png')
    t.set_audio(audio.LoopingAlarm, loop = False)
    t.add_actions(label='Click me', launch='https://www.linkedin.com/learning/?u=88011874')

    t.show()

def notifyBattLow():
    t = Notification(app_id="HemantDhanwar",
                     title="Battery Status",
                     msg = "Battery is low its below 20%",
                     duration="long",
                     icon = 'D:/Itachi.png')
    t.set_audio(audio.LoopingAlarm, loop = False)
    t.add_actions(label='close', launch='')

    t.show()
    
def notifyBattcom():
    t = Notification(app_id="HemantDhanwar",
                     title="Battery Status",
                     msg = "Battery is charged more than 90%",
                     duration="long",
                     icon = 'D:/Itachi.png')
    t.set_audio(audio.LoopingAlarm, loop = False)
    t.add_actions(label='close', launch='')

    t.show()
    
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

def batterymonitor():
    battery = psutil.sensors_battery()
    battery = psutil.sensors_battery()
    print("Battery percentage : ", battery.percent)
    print("Power plugged in : ", battery.power_plugged)
    
def disconnect():
    engine = pyttsx3.init()
    engine.say("main power supply for charger just disconnected.")
    engine.runAndWait()

def connect():
    engine = pyttsx3.init()
    engine.say("main power supply for charger connected.")
    engine.runAndWait()

def per90percent():
    battery = psutil.sensors_battery()
    engine = pyttsx3.init()
    engine.say("Please remove charger from laptop, battery is {} percent charged".format(battery.percent))
    engine.runAndWait()
    notifyBattcom()
    
def batterypluggedin_1():
    fal = True
    while True:
        engine = pyttsx3.init()
        battery = psutil.sensors_battery()
        flag = battery.power_plugged
        plug = True
        enable = True
        en1 = True
        en2 = True
        flg = True
        
        if not battery.power_plugged:
            if fal == True:
                for i in range(3):
                    engine.say("battery status is {} percent".format(battery.percent))
                    engine.runAndWait()
                fal = False
        else:
            while flag:                
                #print("While else")
                if flag:
                    #print("while if")
                    x = convertTime(battery.secsleft)
                    x = x.split(':')
                    hr = int(x[0])
                    hr = abs(hr)
                    battery = psutil.sensors_battery()
                    while plug:
                        engine.say("power charger just plugged in, battery will be charged in approx {} hour {} minuts and {} seconds.".format(hr,x[1],x[2]))
                        engine.runAndWait()
                        plug = False
                    battery = psutil.sensors_battery()
                    if flag == False:
                        print("not conntcted")
                        break
                    elif psutil.sensors_battery().percent > 90:
                        if flag and enable:
                            per90percent()
                            enable = False
                       
                    elif psutil.sensors_battery().percent < 20:
                        if flg == True:
                            engine.say("Please connect charger to avoid system shutdown or sleep, battery is {} percent and going down".format(battery.percent))
                            engine.runAndWait()
                            notifyBattLow()
                            flg = False
                        #print("Please connect charger to avoid system shutdown or sleep, battery is {} percent and going down".format(battery.percent))

                    elif not psutil.sensors_battery().power_plugged:
                        if flag and en2:
                            disconnect()
                            en2 = False
                            en3 = True
                    elif psutil.sensors_battery().power_plugged:
                        if not en2 and en3:
                            connect()
                            en3 = False
                            en2 = True

if __name__=='__main__':
    batterypluggedin_1()
    
