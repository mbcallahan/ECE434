The shell script reads the two temperature sensors.

With my current setup, the the debian user is not in the I2C group, so i2C requires sudo.

Additionally, the eQEP setup gives the error of the configuration mode not being a device for the pins. I don't understand how to fix that at the moment, but I can control the led's so I think my sketch.py should work if I can configure eQEP.

sketch.py is the etch-a-sketch.
tempProbes.py reads the temperature probes in F and configures interrupts.
