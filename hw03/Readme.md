The tempFarenheit.sh script reads the two temperature sensors.

With my current setup, the the debian user is not in the I2C group, so i2C requires sudo.

Additionally, the eQEP setup gives the error of the configuration mode not being a device for the pins. I don't understand how to fix that at the moment, but I can control the led's so I think my sketch.py should work if I can configure eQEP.

sketch.py is the etch-a-sketch. the setup.sh script configures the encoder pins
tempProbes.py reads the temperature probes in F and configures interrupts.

# hw03 grading

| Points      | Description |
| ----------- | ----------- |
|  5/5 | TMP101 
|  3/3 |   | setup.sh
|  2/3 |   | Documentation | 
|  5/5 | Etch-a-Sketch
|  3/3 |   | setup.sh
|  2/2 |   | Documentation
| 20/20 | **Total**