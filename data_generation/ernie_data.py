import os


f_1 = open("train.txt", 'r+',encoding="utf-8")
f_2 = open('train.0', 'w+',encoding="utf-8")
#f_1 = open("dev.txt", 'r+',encoding="utf-8")
#f_2 = open('dev.0', 'w+',encoding="utf-8")


cur_str = ''
tag_str = ''

for line in f_1:
	if line != '\n':
		line = line.strip('\n')
		line = line.split(' ')
		cur_str += line[0]
		tag_str += line[1] + ''
	else:
		tag_str = tag_str[:-1].strip('\r')
		cur_str = list(cur_str)
		cur_str = ''.join(cur_str)

		f_2.write(cur_str+'\t'+tag_str+'\n')
		cur_str = ''
		tag_str = ''
