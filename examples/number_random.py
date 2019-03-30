import sys
import time
import datetime
from random import randint

import flotilla

dock = flotilla.Client()
print('Client connected')

while not dock.ready:
	pass

print('Finding module...')
number = dock.first(flotilla.Number)

if number is None:
	print("No number module found")
	dock.stop()
	sys.exit(1)
else:
	print('Found. Running...')

try:
	while True:
		randnum = randint(0, 9999)
		number.set_number(randnum)
		number.update()
		time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()