#! /usr/bin/python
import string
rot2 = string.maketrans(
		"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
		"CDEFGHIJKLMNOcdefghijklmnoPQRSTUVWXYZABpqrstuvwxyzab")
print string.translate("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.", rot2);

print string.translate("pc/def/map.html",rot2);