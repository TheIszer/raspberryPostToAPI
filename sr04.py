O.output(TRIG, False)
 
while GPIO.input(ECHO) == False:
	start = time.time()
 
while GPIO.input(ECHO) == True:
	end = time.time()
 
sig_time = end-start
 
#CM:
distance = sig_time / 0.000058
 
#inches:
#distance = sig_time / 0.000148
 
print('Distance: {} centimeters'.format(distance))
 
GPIO.cleanup()
