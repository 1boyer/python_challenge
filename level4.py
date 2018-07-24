import urllib
import re

reg = re.compile('[0-9]{5}|[0-9]{4}|[0-9]{3}')
reg2 = re.compile('Divide')

content = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d" % 8022).readlines()[0]
res = reg.findall(content)

val = 0
while res:
  prev = res[:]
  content = ''.join(urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d" % int(res[len(res)-1])).readlines())
  res = reg.findall(content)
else:
  print prev[0]
  print content