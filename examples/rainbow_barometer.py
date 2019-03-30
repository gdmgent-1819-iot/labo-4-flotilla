import sys
import time

import flotilla

dock = flotilla.Client()
print('Client connected')

while not dock.ready:
	pass

print('Finding module...')
weather = dock.first(flotilla.Weather)
rainbow = dock.first(flotilla.Rainbow)

if weather is None or rainbow is None:
	print("No modules found")
	dock.stop()
	sys.exit(1)
else:
	print('Found. Running...')



try:
	while True:
		for module in dock.available.values():
			if module.is_a(flotilla.Weather):
				pressure = module.pressure

				if pressure >= 10150:
						rainbow.set_pixel (0, 255, 0, 0)
				elif pressure > 9850:
						rainbow.set_pixel (2, 0, 255, 0)
				elif pressure > 8000:
						rainbow.set_pixel (4, 0, 0, 255)

				rainbow.update()
		time.sleep(0.5)
		for x in range(rainbow.num_pixels):
			rainbow.set_pixel (x, 0, 0, 0)

except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()