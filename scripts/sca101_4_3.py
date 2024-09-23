from script_common import *

scope = cw.scope(name="Husky")
target = cw.target(scope, cw.targets.SimpleSerial2)

scope.default_setup()
build_copy_prog_fw(scope, "simpleserial-aes")

cw.set_all_log_levels(cw.logging.CRITICAL)

#Capture Traces
from tqdm import trange
import numpy as np
import time

ktp = cw.ktp.Basic()

traces = []
N = 50  # Number of traces
    
print(scope)

project = cw.create_project("./Lab_4_3.cwp", overwrite=True)
for i in trange(N, desc='Capturing traces'):
    key, text = ktp.next()  # manual creation of a key, text pair can be substituted here

    trace = cw.capture_trace(scope, target, text, key)
    if trace is None:
        continue
    project.traces.append(trace)

project.export(tracedir + "lab_4_3.zip")
project.save()
project.close()