import time
import RPi.GPIO as GPIO
import ConfigParser

from send_email import Email


Config = ConfigParser.ConfigParser()
Config.read("sonar.ini")
MAX_DISTANCE = int(Config.get("Sonar", "distance"))
TRIG = 23
ECHO = 24
SOUND_SPEED = 34300
MAX_ALERT = 3


def set_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, False)
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)


if __name__ == "__main__":
    email_to = Config.get("Email", "email_from")
    print "Start sonar GPIO with max distance to {}".format(MAX_DISTANCE)
    print "Email to {}".format(email_to)
    email = Email('Alert', Config.get("Email", "email_from"), email_to, Config.get("Email", "smtp"))
    count_alert = 0
    while True:
        set_gpio()
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = round(pulse_duration * SOUND_SPEED / 2, 2)

        if distance < MAX_DISTANCE:
            print "Alert something at distance: {} cm".format(distance)
            count_alert += 1
            if count_alert >= MAX_ALERT:
                print "Send email to: {} cm".format(email_to)
                email.send()
        else:
            count_alert = 0
            print "all is safe"
        GPIO.cleanup()
