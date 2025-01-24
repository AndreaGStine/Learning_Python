#Playing around with convolutions

import numpy
import random
import pandas
import matplotlib_inline

expvect = []

for i in list(range(10)):
    expvect.append(numpy.random.exponential(scale=1.0, size=None))

uniformvect = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

print(expvect)

for i in list(range(3)):
    expvect = numpy.convolve(expvect, uniformvect)
    print(expvect)

dataset = numpy.array([expvect,range(len(expvect))])
dataset.transpose

df = pandas.DataFrame(dataset, columns=["data", "index"])
print(df)

#df.plot(y='index', x='data')