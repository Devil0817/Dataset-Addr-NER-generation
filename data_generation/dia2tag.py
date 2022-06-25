import os
import numpy as np
import random


f_sentence = open("dialogue.txt", "r+",encoding="utf-8")
f_tag = open("tag.txt", "r+",encoding="utf-8")
f_out1 = open("train.txt", "w+",encoding="utf-8")
f_out2 = open("dev.txt", "w+",encoding="utf-8")
count_train = 0
count_dev = 0

random_num = random.randint(1,10)
for line in f_sentence:
	line_tag = f_tag.readline()
	print('line:',line)
	print('lint_tag:',line_tag)
	if random_num <= 7:
		if line != '\n':
			line = line.strip('\n')
			line_tag = line_tag.strip('\n')
			line_tag = line_tag.split(' ')
			print(len(line_tag))
			print(len(line))
			for i in range(len(line)):
				if line_tag[i][-1] == '2' or line_tag[i][-1] == '3' or line_tag[i][-1] == '4':
					line_tag[i] = line_tag[i][:-1]
				f_out1.write(line[i]+' '+line_tag[i]+'\n')
			f_out1.write('\n')
		else:
			random_num = random.randint(1,10)
			count_train += 1
			continue
	else:
		if line != '\n':
			line = line.strip('\n')
			line_tag = line_tag.strip('\n')
			line_tag = line_tag.split(' ')
			print(len(line_tag))
			print(len(line))
			for i in range(len(line)):
				if line_tag[i][-1] == '2' or line_tag[i][-1] == '3' or line_tag[i][-1] == '4':
					line_tag[i] = line_tag[i][:-1]
				f_out2.write(line[i]+' '+line_tag[i]+'\n')
			f_out2.write('\n')
		else:
			random_num = random.randint(1,10)
			count_dev += 1
			continue

print('train',count_train)
print('dev',count_dev)
f_sentence.close()
f_tag.close()
f_out1.close()
f_out2.close()