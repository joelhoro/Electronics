import RPi.GPIO as GPIO
import time

LED_PORT = 7



try:

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LED_PORT,GPIO.OUT)

	print("Starting");
	pwm = GPIO.PWM(LED_PORT, 50)
	pwm.start(0)
	dc_min = 3.0
	dc_max = 15.0
	increase = 1
	n = 50
	dc = dc_min
	step = 0.1
	while True:
		if dc > dc_max:
			increase = -1
		if dc < dc_min:
			increase = 1
#                dc = float(input())
		dc += step * increase
		print(dc);
		pwm.ChangeDutyCycle(dc)
		
#    		GPIO.output(LED_PORT,True)
		time.sleep(0.01)
	##		print("OFF");
	##    		GPIO.output(LED_PORT,False)
	##	    	time.sleep(0.1)

except Exception as e:
	print("Error!");
	print(e);
finally:
	print("Cleaning up")
	GPIO.output(LED_PORT,False)
	time.sleep(2)
	GPIO.cleanup()

