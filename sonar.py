import time
import RPi.GPIO as GPIO
import ConfigParser


Config = ConfigParser.ConfigParser()
Config.read("sonar.ini")
MAX_DISTANCE = int(Config.get("Sonar", "distance"))
TRIG = 23
ECHO = 24


if __name__ == "__main__":
    print "Start sonar GPIO with max distance to {}".format(MAX_DISTANCE)
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        GPIO.output(TRIG, False)
        time.sleep(2)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        if distance < MAX_DISTANCE:
            print "Alert something at distance: {} cm".format(distance)
        else:
            print "all is safe"
        GPIO.cleanup()
