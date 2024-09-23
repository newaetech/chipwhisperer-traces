
from script_common import *

scope = cw.scope(name="Husky")
target = cw.target(scope, cw.targets.SimpleSerial2)

scope.default_setup()
build_copy_prog_fw(scope, "simpleserial-aes")

cw.set_all_log_levels(cw.logging.CRITICAL)

import time

scope.adc.samples = 5000

def reset_target(scope):
    scope.io.nrst = 'low'
    time.sleep(0.005)
    scope.io.nrst = 'high'
    time.sleep(0.005)

from tqdm import trange
import numpy as np

#Capture Traces
from tqdm import trange
import numpy as np
import time

ktp = cw.ktp.Basic()

traces = []
N = 2500  # Number of traces

scope.adc.samples = 4000
    
print(scope)
for i in trange(N, desc='Capturing traces'):
    key, text = ktp.next()  # manual creation of a key, text pair can be substituted here

    trace = cw.capture_trace(scope, target, text, key)
    if trace is None:
        continue
    traces.append(trace)

#Convert traces to numpy arrays
trace_array = np.asarray([trace.wave for trace in traces])
textin_array = np.asarray([trace.textin for trace in traces])
known_keys = np.asarray([trace.key for trace in traces])  # for fixed key, these keys are all the same

np.save(tracedir + "lab3_3_traces.npy", trace_array)
np.save(tracedir + "lab3_3_textin.npy", textin_array)