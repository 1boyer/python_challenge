
S = r"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

S2 = "map"

key = 2

output = ""

for ch in S2.lower():
  code_val = 0
  if ch.isalpha():
    code_val = ord(ch) + key
    if code_val > ord('z'):
      code_val -= 26
  else:
    code_val = ord(ch)

  output += chr(code_val)

print output