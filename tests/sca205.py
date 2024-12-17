from cwtraces import sca205_lab_data

get_traces = sca205_lab_data["get_traces"]

for i in range(1, 9):
    get_traces("uecc_{}.npz".format(i))
    print("Loading {}".format("uecc_{}.npz".format(i)))

get_traces("uecc_ttimes2.npz".format(i))
print("Loading " + "uecc_ttimes2.npz".format(i))