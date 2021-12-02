import pickle
import time

def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

My_Things = ['Python', 'Body Building', 'Machine Learning', 'Power Electronics', 'Neuroscience', 'Linux/Ubuntu', 'Guitar']
time_record = {}
for thing in My_Things:
    time_record[thing] = {}

time_record['Python']['initial'] = 700.0
time_record['Body Building']['initial'] = 550.0
time_record['Machine Learning']['initial'] = 200.0
time_record['Power Electronics']['initial'] = 3000.0
time_record['Neuroscience']['initial'] = 50.0
time_record['Linux/Ubuntu']['initial'] = 200.0
time_record['Guitar']['initial'] = 10.0

passcode = input('You are resetting all the time records before, to go on please input the passcode __________\n')
if passcode == '123459':
    save_obj(time_record, 'record')
    print('Reset successful.')
else:
    print('passcode worng, now quitting.')
time.sleep(1)
