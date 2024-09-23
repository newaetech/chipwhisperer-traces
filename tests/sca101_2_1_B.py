from cwtraces import sca101_lab_data
import numpy as np
from tqdm import trange

cap_pass_trace = sca101_lab_data["lab2_1"]["cap_pass_trace"]

guessed_pw = ""

for _ in range(0, 5):  
    biggest_diff = 0
    biggest_char = '\x00'
    ref_trace = cap_pass_trace(guessed_pw + "\x01\n")
    
    for c in 'abcdefghijklmnopqrstuvwxyz0123456789': 
        trace = cap_pass_trace(guessed_pw + c + "\n")
        diff = np.sum(np.abs(trace - ref_trace))

        if diff > biggest_diff:
            biggest_diff = diff
            biggest_char = c
            
    guessed_pw += biggest_char
    # print(biggest_char)
    print(guessed_pw)