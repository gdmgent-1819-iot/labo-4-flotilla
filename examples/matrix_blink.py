import sys
import time

import flotilla

dock = flotilla.Client()
print('Client connected')

while not dock.ready:
	pass

print('Finding module...')
matrix = dock.first(flotilla.Matrix)

if matrix is None:
	print("No matrix module found")
	dock.stop()
	sys.exit(1)
else:
	print('Found. Running...')

state = True

try:
	while True:
		for module in dock.available.values():
			if module.is_a(flotilla.Matrix):
				module.set_pixel(3, 3, state).update()

		state = not state
		time.sleep(1)

except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()