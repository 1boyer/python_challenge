import zipfile

zipper = zipfile.ZipFile("channel.zip")
comments = ''
word_list = ["90052"]

while word_list:
  for word in word_list:
    if word.isdigit():
	  break
  else:
    word = 0

  if word:
    file_info = zipper.getinfo(word + ".txt")
    comments += file_info.comment
    file_des = zipper.open(file_info)
    word_list = file_des.read().split(" ")
  else:
    word_list = 0

print comments