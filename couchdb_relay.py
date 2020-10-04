#! /usr/bin/env python3
import time, requests, os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO_pin = 6 
server = "http://localhost:5984/helloworld/";

def check_available():
    card_id = input("student id");
    status = requests.get(server+card_id).status_code;
    print(status);
    if status == 200:
        GPIO.output(GPIO_pin, GPIO.LOW); #relay
        time.sleep(3);
        GPIO.output(GPIO_pin, GPIO.HIGH); # on

if __name__ == '__main__':
    while True:
        os.system("sudo systemctl start couchdb");
        check_available();
