import sys
import time

import flotilla

dock = flotilla.Client()
print('Client connected')

while not dock.ready:
	pass

print('Finding module...')
colour = dock.first(flotilla.Colour)

if colour is None:
	print("No colour module found")
	dock.stop()
	sys.exit(1)
else:
	print('Found. Running...')

COLOR_INFO = "{red}, {green}, {blue}, {clear}"

try:
	while True:
		print(COLOR_INFO.format(
			red = colour.red,
			green = colour.green,
			blue = colour.blue,
			clear = colour.clear
		))
		time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()