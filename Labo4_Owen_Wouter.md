# Flotilla

## Installation and setup

**Step 1:** You purchase and take out the Mega Treasure Chest from flotilla. If you do not have one available, you can get it from [this webiste](https://shop.pimoroni.com/products/flotilla-mega-treasure-chest).

**Step 2:** You plug in and start your Raspberry Pi. You will either need a SSH connection to it or plug in a mouse, keyboard and monitor to make this work.

**Step 3:** Take the Flotilla dock and modules out of the box. You will need the dock during installation.

**Step 4:** Make sure the Pi is connected to the internet. At home this can be either through WiFi or an ethernet cable. ***At Artevelde this has to be a WiFi connection to make the commands work!***

**Step 5:** Run the following command in your terminal: `curl -sS get.pimoroni.com/flotilla | bash` and follow the instructions on the screen. Make sure to disconnect the dock at the end of the installation.

**Step 6:** Plug the dock back in to the Pi using the red cable.

**Step 7:** Create a python file. Write (or copy-paste) the following code in that file.

```py
import flotilla
dock = flotilla.Client()
print(dock)
```

**Step 8:** Run this file using `python3 [filename].py`. If you get a response in the terminal, the dock is succesfully connected. You can now use the modules and the Python API to create cool things.

## Examples

We have provided 4 examples in `./exapmples`. The first example uses the colour module to read any colour that hovers over the sensor. The second one uses the LED Matrix to randomly flash a pixel. The third one displays a random 4-digit number on the number display.

Our fourth example is a bit bigger, since it uses two modules. The barometer and the rainbow display are used to display a colour on the rainbow depending on the air pressure.