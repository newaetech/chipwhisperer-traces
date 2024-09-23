from script_common import *
from tqdm import trange


scope = cw.scope(name="Husky")
target = cw.target(scope, cw.targets.SimpleSerial2)
scope.default_setup()
build_copy_prog_fw(scope, "basic-passwdcheck")
cw.set_all_log_levels(cw.logging.CRITICAL)

scope.adc.samples = 3000
def cap_pass_trace(pass_guess):
    reset_target(scope)
    num_char = target.in_waiting()
    while num_char > 0:
        target.read(num_char, 10)
        time.sleep(0.01)
        num_char = target.in_waiting()

    scope.arm()
    target.write(pass_guess)
    ret = scope.capture()
    if ret:
        print('Timeout happened during acquisition')

    trace = scope.get_last_trace()
    return trace

from tqdm.notebook import tqdm_notebook
import pickle
cw.set_all_log_levels(cw.logging.CRITICAL)

trylist = "abcdefghijklmnopqrstuvwxyz0123456789"
pw = ""

traces = {}
    
known_passwd = "h0px3"
    
#Capture N of each
N_each = 100

traces["N_each"] = N_each

for j in trange(1,6):
    #j = capture length
    #Get totally wrong option
    guesslist = [" "*j]
        
    for k in range(1, j):
        guess = known_passwd[0:k] + " "*(j-k)
        guesslist.append(guess)
        
    guesslist.append(known_passwd[0:j])
    print(guesslist)
    
    #Get fully correct
    for guess in tqdm_notebook(guesslist):
        traces[guess] = [0] * N_each
        for i in range(0, N_each):
            traces[guess][i] = cap_pass_trace(guess + "\n")
        
pickle.dump(traces, open(tracedir + "lab2_1b_passwords_full.p", "wb"))