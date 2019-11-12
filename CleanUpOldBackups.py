#!/usr/bin/python
import os
import time
import datetime
from datetime import datetime
current_time = time.time()
os.chdir("90files")
for f in os.listdir('.'):
    mod_time = os.path.getmtime(f)
    ep = ((current_time - mod_time) // (24 * 3600))
    print mod_time
    if ep <= 30:
        print f
    elif datetime.fromtimestamp(mod_time).strftime("%A") == 'Saturday' and ep <= 90:
        print "Monday"
    else:
        print "REMOVE f"
        os.remove(f)
        