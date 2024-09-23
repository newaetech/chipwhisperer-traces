from cwtraces import sca101_lab_data

data = sca101_lab_data["lab4_3"]
project = data["project"]()

import chipwhisperer.analyzer as cwa
leak_model = cwa.leakage_models.sbox_output
attack = cwa.cpa(project, leak_model)

cb = cwa.get_jupyter_callback(attack)
results = attack.run()

assert (results.key_guess() == project.keys[0]).all()