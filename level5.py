import pickle
import sys

sys.stdout = open("banner.txt", 'w')

banner = pickle.load(open("banner.p"))
data = []
for item in banner:
  for seq in item:
    data.append(seq[0]*seq[1])
  data.append('\n')
print "".join(data)