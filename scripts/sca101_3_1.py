from script_common import *

scope = cw.scope(name="Husky")
target = cw.target(scope, cw.targets.SimpleSerial2)

scope.default_setup()
build_copy_prog_fw(scope, "simpleserial-aes")

cw.set_all_log_levels(cw.logging.CRITICAL)

from tqdm import trange
import numpy as np

ktp = cw.ktp.Basic()
trace_array = []
textin_array = []

key, text = ktp.next()

target.simpleserial_write('k', key)

N = 100
for i in trange(N, desc='Capturing traces'):
    scope.arm()
    if text[0] & 0x01:
        text[0] = 0xFF
    else:
        text[0] = 0x00
    target.simpleserial_write('p', text)
    
    ret = scope.capture()
    if ret:
        print("Target timed out!")
        continue
    
    response = target.simpleserial_read('r', 16)
    
    trace_array.append(scope.get_last_trace())
    textin_array.append(text)
    
    key, text = ktp.next() 

np.save(tracedir + "lab3_1_traces.npy", trace_array)
np.save(tracedir + "lab3_1_textin.npy", textin_array)