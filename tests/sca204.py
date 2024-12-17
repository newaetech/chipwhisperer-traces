from cwtraces import sca204_lab_data
steps = []
parts = [range(1, 6), range(1,5), range(1,8), range(1,6)]

for i in range(len(parts)):
    for j in parts[i]:
        steps.append("part{}_{}.npz".format(i + 1, j))

get_traces = sca204_lab_data["get_traces"]

for file in steps:
    get_traces(file)
    print("Loading {}".format(file))