import numpy as np
from importlib import resources
import chipwhisperer as cw
import pickle
import random
import time

def gen_numpy_trace_text_func(lab_name, course_name="sca101"):
    def load_trace_text():
        """Load lab data as a dictionary as numpy arrays

        Example:
            data = lab_data['lab3_1']()
            data['trace_array']
        """
        trace_array =  np.load(resources.files("cwtraces").joinpath("{}/{}_traces.npy".format(course_name, lab_name)))
        textin_array = np.load(resources.files("cwtraces").joinpath("{}/{}_textin.npy".format(course_name, lab_name)))
        rtn = {"trace_array": trace_array, "textin_array": textin_array}
        try:
            key = np.load(resources.files("cwtraces").joinpath("{}_key.npy".format(lab_name)))
            rtn["key"] = key
        except:
            pass
        return rtn

    return load_trace_text

# get 
numpy_trace_text_lab_names = ["lab3_1", "lab3_3", "lab4_1", "lab4_2"]

sca101_lab_data = {}
def cap_pass_trace(pass_guess):
    traces_to_load = pickle.load(open(resources.files("cwtraces").joinpath("sca101/lab2_1b_passwords_full.p"), "rb"))
    if pass_guess.endswith("\n") is False:
        raise ValueError("Password guess must end with \\n")
        
    pass_guess = pass_guess.strip("\n")
    
    known_passwd = "h0px3"
        
    trylist = "abcdefghijklmnopqrstuvwxyz0123456789 \x01"
    
    if len(pass_guess) > 5:
        raise ValueError("Only guesses up to 5 chars recorded, sorry about that.")
        
    for a in pass_guess:
        if a not in trylist:
            raise ValueError("Part of guess (%c) not in recorded enumeration list (%s)"%(a, trylist))
            
    #Only recorded is correct passwords
    recorded_pw = ""
    for i in range(0, len(pass_guess)):
        if known_passwd[i] != pass_guess[i]:
            recorded_pw += " " * (len(pass_guess) - i)
            break
        else:
            recorded_pw += pass_guess[i]
            
    time.sleep(0.05)

    # print (recorded_pw)
    return traces_to_load[recorded_pw][random.randint(0, 99)]

def sca204_load_traces(filename):
    np.load(resources.files("cwtraces").joinpath("sca204/{}".format(filename)), allow_pickle=True)

def sca205_load_traces(filename):
    np.load(resources.files("cwtraces").joinpath("sca205/{}".format(filename)), allow_pickle=True)
    

sca101_lab_data["lab2_1"] = {"cap_pass_trace": cap_pass_trace}

for lab in numpy_trace_text_lab_names:
    sca101_lab_data[lab] = gen_numpy_trace_text_func(lab)

sca101_lab_data["lab4_3"] = {"project": lambda: cw.open_project(resources.files("cwtraces").joinpath("Lab_4_3.cwp"))}

sca201_lab_data = {}
sca204_lab_data = {"get_traces": sca204_load_traces}
sca205_lab_data = {"get_traces": sca205_load_traces}