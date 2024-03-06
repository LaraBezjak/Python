import numpy as np
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filename = 'WBC_PCA.csv'

def Read_Matrix(filename):
  
  reader = csv.reader(open(filename, "r"), delimiter=',')
  data = list(reader)
  dists = []
  labels = []

  for d in data[1:]:
       dists.append(list(map(lambda x: float(x), d[3:6])))
       labels.append(str(d[2]))
  
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

  if l == 'BASOPHIL': 
      labelColor = 'springgreen'  
  elif l == 'EOSINOPHIL': 
      labelColor = 'midnightblue'
  elif l == 'LYMPHOCYTE': 
      labelColor = '#0093D1'
  elif l == 'MONOCYTE': 
      labelColor = '#F2635F'
  elif l == 'NEUTROPHIL': 
      labelColor = '#E0A025'
  else: 
    l = 'OTHER'
    labelColor = 'white'

  ax.scatter(x, y, z, c=labelColor)
  plt.subplots_adjust(bottom = 0.1)
  
ax.scatter(0, 0, 0, c='springgreen', label='BASOPHIL')
ax.scatter(0, 0, 0, c='midnightblue', label='EOSINOPHIL')
ax.scatter(0, 0, 0, c='#0093D1', label='LYMPHOCYTE')
ax.scatter(0, 0, 0, c='#F2635F', label='MONOCYTE')
ax.scatter(0, 0, 0, c='#E0A025', label='NEUTROPHIL')

plt.legend(labels)
plt.title("WBC by Cell Type")
plt.show()

#plt.savefig('WBC_CT.png')