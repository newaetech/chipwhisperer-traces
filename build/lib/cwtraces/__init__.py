import numpy as np
def gen_numpy_trace_text_func(lab_name):
    def load_trace_text():
        trace_array = np.open("{}_traces.npy".format(lab_name))
        textin_array = np.open("{}_traces.npy".format(lab_name))
        rtn = {"trace_array": trace_array, "textin_array": textin_array}
        try:
            key = np.open("{}_key.npy".format(lab_name))
            rtn["key"] = key
        except:
            pass
        return rtn

    return load_trace_text

numpy_trace_text_lab_names = ["lab3_1", "lab3_3", "lab4_1", "lab4_2"]


lab_data = {}

for lab in numpy_trace_text_lab_names:
    lab_data[lab] = gen_numpy_trace_text_func(lab)