#!/usr/bin/env python
import sys 
from sense_hat import SenseHat
sense = SenseHat()
argv = sys.argv
program_name = argv.pop(0)
argv_string = ' '.join(argv)
print argv_string
sense.show_message(argv_string)
