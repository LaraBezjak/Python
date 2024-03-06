import numpy as np
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filename = 'WBC_PCA.csv'

def Read_Matrix(filename):
  reader = csv.reader(open(filename, mode="r"), delimiter=',')
  data = list(reader)
  dists = []
  labels = []

  for d in data[1:]:
    dists.append(list(map(lambda x: float(x), d[3:6])))
    labels.append(str(d[1]))

  adist = np.array(dists)

  amax = np.amax(adist)

  adist /= amax   

  return (adist, labels)

(mat, labels) = Read_Matrix(filename)

fig = plt.figure()
ax = Axes3D(fig)

for i in range(len(mat)):
  x = mat[i][0]
  y = mat[i][1]
  z = mat[i][2]
  l = labels[i]

  if (l == 'GRANULOCYTE'):
      labelColor = '#007CC3' 
  elif l == 'LYMPHOCYTE':
      labelColor = '#F47A1F'
  elif l == 'MONOCYTE':
      labelColor = '#7AC142'
  else: 
    l = 'OTHER'
    labelColor = 'white'

  ax.scatter(x, y, z, c=labelColor)
  plt.subplots_adjust(bottom = 0.1)
  
ax.scatter(0, 0, 0, c="#007CC3", label='GRANULOCYTE')
ax.scatter(0, 0, 0, c='#F47A1F', label='LYMPHOCYTE')
ax.scatter(0, 0, 0, c='#7AC142', label='MONOCYTE')

plt.legend(labels)
plt.title("WBC by Cell Family")
plt.show()

#plt.savefig('WBC_CF.png')