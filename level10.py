#a = [1, 11, 21, 1211, 111221, 


def next(curr):
  ret = []
  seqL = list(curr)
  i = 0
  while i < len(seqL):
    for j in range(i,len(seqL)):
      if seqL[i] != seqL[j]:
	    multiplicity = j - i
	    break;
      elif j == len(seqL)-1:
	    multiplicity = j-i+1
	    break;
	  
    ret = ret + [str(multiplicity), seqL[i]]
    i = i+multiplicity
  ret = ''.join(ret)
  return ret

a = ["1"]
for i in range(30):
  a = a + [next(a[-1])]
print "Answer:", len(a[30])