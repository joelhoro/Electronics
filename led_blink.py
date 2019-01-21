import RPi.GPIO as GPIO
import time

LED_PORT = 7



try:

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LED_PORT,GPIO.OUT)

        pwm = GPIO.PWM(LED_PORT, 1000)
        pwm.start(0)

	for i in range(100):
                dc = float(input())
##		print(i);
		pwm.ChangeDutyCycle(dc)
		
#    		GPIO.output(LED_PORT,True)
    		time.sleep(0.05)
##		print("OFF");
##    		GPIO.output(LED_PORT,False)
##	    	time.sleep(0.1)

except:
	print("Error!")
finally:
	print("Cleaning up")
	GPIO.output(LED_PORT,False)
	time.sleep(2)
	GPIO.cleanup()

