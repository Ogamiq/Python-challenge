#runs at python 3.5

import pickle


#open file data_p5.p in a read-binary mode
with open('data_p5.p','rb') as file:
    raw_data = file.read()


data = pickle.loads(raw_data)

for dict in data:
    print(''.join(tuple[0] * tuple[1] for tuple in dict))

