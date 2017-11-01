#runs at python 3.5

import pickle


#open file data_p5.p in a read-binary mode
file = open('data_p5.p','rb')
raw_data = file.read()
file.close()

data = pickle.loads(raw_data)


for li in data: #for list of tuples in data print list of tuple
    print(li)
