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
trace_array = []
textin_array = []

key, text = ktp.next()

target.simpleserial_write('k', key)

N = 50
for i in trange(N, desc='Capturing traces'):
    scope.arm()
    
    target.simpleserial_write('p', text)
    
    ret = scope.capture()
    if ret:
        print("Target timed out!")
        continue
    
    response = target.simpleserial_read('r', 16)
    
    trace_array.append(scope.get_last_trace())
    textin_array.append(text)
    
    key, text = ktp.next() 
    
trace_array = np.array(trace_array)
textin_array = np.array(textin_array)

np.save(tracedir + "lab4_2_traces.npy", trace_array)
np.save(tracedir + "lab4_2_textin.npy", textin_array)
np.save(tracedir + "lab4_2_key.npy", key)