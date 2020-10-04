import json, os, time
import urllib.request as request
#import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO_pin = 6 
server = "http://localhost:5984/helloworld/"

def main():
    usercheck()
    getcard()
    time.sleep(3000)
    relayout()

def usercheck():
    global stuId
    stuId = input("student id")
    global response
    response = request.Request(server+stuId)
    print(response)

def relayout():
    # GPIO.output(GPIO_pin, GPIO.LOW) # out
    pass

def relayin():
    # GPIO.output(GPIO_pin, GPIO.HIGH) # on
    pass


def getcard():
    if response == "<Response [200]>":
        relayin()
        with request.urlopen(server+stuId) as url:
            data = json.loads(url.read().decode())
            print(data['name'])

    else:
        usercheck()

if __name__ == '__main__':
    main()
