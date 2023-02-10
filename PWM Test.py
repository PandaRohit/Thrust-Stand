import RPi.GPIO as GPIO
from time import sleep

def computeDutyCycle(frequency, percentage):
    # frequency is how many pulses per second - 50 works
    # percentage is between 0 and 100%
    dutyCycle = 100./(1000./frequency)+(percentage/100.)*5
    return dutyCycle

frequency = 50 # in hertz
PWM_PIN = 11 # Rpi PWM pin number

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWM_PIN, GPIO.OUT)

pwm = GPIO.PWM(PWM_PIN,frequency)
pwm.start(computeDutyCycle(frequency,0))
print("Sent zero, sleeping 5")
sleep(5)

pwm.ChangeDutyCycle(computeDutyCycle(frequency,25))
print("Sent 25%, sleeping 5")
sleep(5)

pwm.ChangeDutyCycle(computeDutyCycle(frequency,50))
print("Sent 50%, sleeping 5")
sleep(5)

pwm.ChangeDutyCycle(computeDutyCycle(frequency,100))
print("Sent 100%, sleeping 2")
sleep(2)

pwm.ChangeDutyCycle(computeDutyCycle(frequency,0))
print("Sent 0%, sleeping 2")
sleep(2)


pwm.stop()
GPIO.cleanup()
