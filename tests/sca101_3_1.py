from cwtraces import sca101_lab_data
import numpy as np
from tqdm import trange

data = sca101_lab_data["lab3_1"]()
trace_array =  data["trace_array"]
textin_array = data["textin_array"]

one_list = []
zero_list = []

for i in range(len(trace_array)):
    if textin_array[i][0] == 0x00:
        zero_list.append(trace_array[i])
    else:
        one_list.append(trace_array[i])
# ###################
# END SOLUTION
# ###################

assert len(one_list) > len(zero_list)/2
assert len(zero_list) > len(one_list)/2

one_avg = np.mean(one_list, axis=0)
zero_avg = np.mean(zero_list, axis=0)