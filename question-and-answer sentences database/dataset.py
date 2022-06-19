import numpy as np
import os
import random

question_prov_city_list = []
question_city_list = []
question_district_list1 = []
question_district_list2 = []
question_town_list1 = []
question_town_list2 = []
question_town_list3 = []
question_road_list1 = []
question_road_list2 = []
question_road_list3 = []
question_road_list4 = []
question_community_list = []
question_poi_list = []
question_num_list = []
question_detail_list = []
question_error_list = []

#question_fill_replace = {'@':'city','#':'town','&':'district','-':'district2','*':'town2','+':'community','/':'road'}
question_fill_replace = {'@':'city','#':'town','&':'district','/':'road','+':'roadno'}

f1 = open("1-开头.txt", "r+",encoding="utf-8")
f2 = open("2-市.txt", "r+",encoding="utf-8")
f31 = open("3-区.txt", "r+",encoding="utf-8")
f32 = open("3-县.txt", "r+",encoding="utf-8")
f41 = open("4-镇.txt", "r+",encoding="utf-8")
f42 = open("4-乡.txt", "r+",encoding="utf-8")
f43 = open("4-街道.txt", "r+",encoding="utf-8")
f51 = open("5-路.txt", "r+",encoding="utf-8")
f52 = open("5-巷.txt", "r+",encoding="utf-8")
f53 = open("5-街.txt", "r+",encoding="utf-8")
f54 = open("5-路号.txt", "r+",encoding="utf-8")
f6 = open("6-小区.txt", "r+",encoding="utf-8")
f7 = open("7-详细.txt", "r+",encoding="utf-8")

f_ty = open("fs_tongyin.txt", "r+",encoding="utf-8")
f_error = open("random_error.txt", "r+",encoding="utf-8")

'''
f32 = open("3-2-镇.txt", "r+",encoding="utf-8")
f41 = open("4-1-街道路.txt", "r+",encoding="utf-8")
f42 = open("4-2-村.txt", "r+",encoding="utf-8")
f5 = open("5-小区.txt", "r+",encoding="utf-8")
f6 = open("6-号.txt", "r+",encoding="utf-8")
'''


f_w = open("dialogue_3.txt", "w+",encoding="utf-8")
f_tag = open("tag_3.txt", "w+",encoding="utf-8")
f_list = {f1:question_prov_city_list,f2:question_city_list,f31:question_district_list1,f32:question_district_list2,
          f41:question_town_list1,f42:question_town_list2,f43:question_town_list3,
          f51:question_road_list1,f52:question_road_list2,f53:question_road_list3,f54:question_road_list4,
          f6:question_community_list,f7:question_detail_list,f_error:question_error_list}
          #f41:question_road_list,f42:question_community_list,f5:question_poi_list,f6:question_num_list}

f_address = open("new2.conll", "r+",encoding="utf-8")



def list_constrct(file):
	for key,value in f_list.items():
		for line in key:
			#print(line)
			value.append(line)
	#print(question_prov_city_list)

def diction_chinese():
	f_dic = open("中文词典.txt", "r+",encoding="utf-8")
	chinese_dic = {}
	for line in f_dic:
		line = line.strip('\n')
		if line[0] not in chinese_dic.keys():
			chinese_dic[line[0]] = []
			chinese_dic[line[0]].append(line)
		else:
			chinese_dic[line[0]].append(line)
		if line[1] not in chinese_dic.keys():
			chinese_dic[line[1]] = []
			chinese_dic[line[1]].append(line)
		else:
			chinese_dic[line[1]].append(line)

	return chinese_dic

def supplyment(cur_str,tag_str,addr,diction,diction_sort):
	if 'intersection' in diction.keys():
		if diction_sort[addr] + 1 == diction_sort['intersection']:
			cur_str += diction['intersection']
			if len(diction['intersection']) == 1:
				tag_str += 'S-intersection '
			else:
				for i in diction['intersection']:
					if i == diction['intersection'][0]:
						tag_str += 'B-' + 'intersection' + ' '
					elif i == diction['intersection'][-1]:
						tag_str += 'E-' + 'intersection' + ' '
					elif i in diction['intersection'][1:-1]:
						tag_str += 'I-' + 'intersection' + ' '
			if 'distance' in diction.keys():
				if diction_sort['intersection'] + 1 == diction_sort['distance']:
					cur_str += diction['distance']
					if len(diction['distance']) == 1:
						tag_str += 'S-distance '
					else:
						for i in diction['distance']:
							if i == diction['distance'][0]:
								tag_str += 'B-' + 'distance' + ' '
							elif i == diction['distance'][-1]:
								tag_str += 'E-' + 'distance' + ' '
							elif i in diction['distance'][1:-1]:
								tag_str += 'I-' + 'distance' + ' '
			return cur_str,tag_str
	if 'assist' in diction.keys():
		if diction_sort[addr] + 1 == diction_sort['assist']:
			cur_str += diction['assist']
			if len(diction['assist']) == 1:
				tag_str += 'S-assist '
			else:
				for i in diction['assist']:
					if i == diction['assist'][0]:
						tag_str += 'B-' + 'assist' + ' '
					elif i == diction['assist'][-1]:
						tag_str += 'E-' + 'assist' + ' '
					elif i in diction['assist'][1:-1]:
						tag_str += 'I-' + 'assist' + ' '
			if 'distance' in diction.keys():
				if diction_sort['assist'] + 1 == diction_sort['distance']:
					cur_str += diction['distance']
					if len(diction['distance']) == 1:
						tag_str += 'S-distance '
					else:
						for i in diction['distance']:
							if i == diction['distance'][0]:
								tag_str += 'B-' + 'distance' + ' '
							elif i == diction['distance'][-1]:
								tag_str += 'E-' + 'distance' + ' '
							elif i in diction['distance'][1:-1]:
								tag_str += 'I-' + 'distance' + ' '
			return cur_str,tag_str
	if 'village_group' in diction.keys():
		if diction_sort[addr] + 1 == diction_sort['village_group']:
			cur_str += diction['village_group']
			if len(diction['village_group']) == 1:
				tag_str += 'S-village_group '
			else:
				for i in diction['village_group']:
					if i == diction['village_group'][0]:
						tag_str += 'B-' + 'village_group' + ' '
					elif i == diction['village_group'][-1]:
						tag_str += 'E-' + 'village_group' + ' '
					elif i in diction['village_group'][1:-1]:
						tag_str += 'I-' + 'village_group' + ' '
			return cur_str,tag_str
	if 'distance' in diction.keys():
		if diction_sort[addr] + 1 == diction_sort['distance']:
			cur_str += diction['distance']
			if len(diction['distance']) == 1:
				tag_str += 'S-distance '
			else:
				for i in diction['distance']:
					if i == diction['distance'][0]:
						tag_str += 'B-' + 'distance' + ' '
					elif i == diction['distance'][-1]:
						tag_str += 'E-' + 'distance' + ' '
					elif i in diction['distance'][1:-1]:
						tag_str += 'I-' + 'distance' + ' '
			return cur_str,tag_str
	return cur_str,tag_str




#开头
def f1_data(diction,diction_sort):
	###f1添加
	f1_len = len(question_prov_city_list)
	kaitou_random_ask = random.randint(0,f1_len-1)
	f_w.write(question_prov_city_list[kaitou_random_ask])
	tag_str = 'O '*len(question_prov_city_list[kaitou_random_ask])
	f_tag.write(tag_str[:-1]+'\n')
	if len(diction) > 3:
		random_num = random.randint(1,3)
	else:
		random_num = 1
	kaitou_str = ''
	tag_str = ''
	kaitou_count = 0
	for t,s in diction.items():
		kaitou_str += s
		for i in range(len(s)):
			if i == 0:
				tag_str += 'B-'+ t + ' '
			elif i == len(s)-1:
				tag_str += 'E-'+ t + ' '
			else:
				tag_str += 'I-'+ t + ' '
		if random.randint(0,5) == 0:
			kaitou_str += ','
			tag_str += 'O '
		elif random.randint(0,4) == 2:
			kaitou_str += '嗯,'
			tag_str += 'O '*2
		kaitou_count += 1
		if kaitou_count == random_num:
			f_w.write(kaitou_str+'\n')
			f_tag.write(tag_str[:-1]+'\n')
			break

#city
def f2_data(diction,diction_sort):
	addr = 'city'
	if addr in diction.keys():
		f2_len = len(question_city_list)
		city_random_ask = random.randint(0,f2_len-1)
		f_w.write(question_city_list[city_random_ask])
		tag_str = 'O '*len(question_city_list[city_random_ask])
		f_tag.write(tag_str[:-1]+'\n')

		city_str = ''
		tag_str = ''
		if random.randint(0,4) == 0:
			city_str += '在'
			tag_str += 'O '
		if random.randint(0,2) == 0:
			city_str += diction[addr][0]
			tag_str += 'O '
		city_str += diction[addr]
		for i in range(len(diction[addr])):
			if i == 0:
				tag_str += 'B-'+ addr + ' '
			elif i == len(diction[addr])-1:
				tag_str += 'E-'+ addr + ' '
			else:
				tag_str += 'I-'+ addr + ' '
		if random.randint(0,5) == 0:
			city_str += ','
			tag_str += 'O '
		elif random.randint(0,5) == 0:
			city_str += '嗯'
			tag_str += 'O '
		f_w.write(city_str+'\n')
		f_tag.write(tag_str[:-1]+'\n')

#district 区县
def f3_data(diction,diction_sort,error_addr):
	addr = 'district'
	if addr in diction.keys():
		district_1 = [] #symbol
		district_2 = [] #nonsymbol
		#f3_len = len(question_district_list)
		if '县' in diction[addr]:
			for q in question_district_list2:
				if '@' in q:
					district_1.append(q)
				else:
					district_2.append(q)
			if 'city' in diction.keys():
				f3_len = len(district_1)
				district_random_ask = random.randint(0,f3_len-1)
				question_write = district_1[district_random_ask].replace('@',diction['city'])
				f_w.write(question_write)
				tag_str = ''
				for i in question_write:
					if i == diction['city'][0]:
						tag_str += 'B-' + 'city' + ' '
					elif i == diction['city'][-1]:
						tag_str += 'E-' + 'city' + ' '
					elif i in diction['city'][1:-1]:
						tag_str += 'I-' + 'city' + ' '
					else:
						tag_str += 'O' + ' '
				f_tag.write(tag_str[:-1]+'\n')
			else:
				f3_len = len(district_2)
				district_random_ask = random.randint(0,f3_len-1)
				f_w.write(district_2[district_random_ask])
				tag_str = 'O '*len(district_2[district_random_ask])
				f_tag.write(tag_str[:-1]+'\n')
		else:
			for q in question_district_list1:
				if '@' in q:
					district_1.append(q)
				else:
					district_2.append(q)
			if 'city' in diction.keys():
				f3_len = len(district_1)
				district_random_ask = random.randint(0,f3_len-1)
				question_write = district_1[district_random_ask].replace('@',diction['city'])
				f_w.write(question_write)
				tag_str = ''
				for i in question_write:
					if i == diction['city'][0]:
						tag_str += 'B-' + 'city' + ' '
					elif i == diction['city'][-1]:
						tag_str += 'E-' + 'city' + ' '
					elif i in diction['city'][1:-1]:
						tag_str += 'I-' + 'city' + ' '
					else:
						tag_str += 'O' + ' '
				f_tag.write(tag_str[:-1]+'\n')
			else:
				f3_len = len(district_2)
				district_random_ask = random.randint(0,f3_len-1)
				f_w.write(district_2[district_random_ask])
				tag_str = 'O '*len(district_2[district_random_ask])
				f_tag.write(tag_str[:-1]+'\n')

		district_str = ''
		tag_str = ''
		if random.randint(0,4) == 0:
			district_str += '在'
			tag_str += 'O '
		if random.randint(0,4) == 0:
			district_str += '在,'
			tag_str += 'O O '
		if random.randint(0,5) == 0:
			district_str += '那个'
			tag_str += 'O O '

		
		if random.randint(0,2) == 0:
			district_str += diction[addr][0]
			tag_str += 'O '
			if random.randint(0,4) == 0:
				district_str += ','
			tag_str += 'O '
		if random.randint(0,23) == 0:
			district_str += diction[addr]
			for i in range(len(diction[addr])):
				if i == 0:
					tag_str += 'B-'+ addr + ' '
				elif i == len(diction[addr])-1:
					tag_str += 'E-'+ addr + ' '
				else:
					tag_str += 'I-'+ addr + ' '
			district_str,tag_str = supplyment(district_str,tag_str,addr,diction,diction_sort)
			if random.randint(0,5) == 0:
				district_str += '嗯'
				tag_str += 'O '
			f_w.write(district_str +'\n')
			f_tag.write(tag_str[:-1]+'\n')
		else:
			if random.randint(0,1) == 0:
				district_str += error_addr['district'][random.randint(0,len(error_addr['district'])-1)][0]
				tag_str += 'B-district '
			random_district = random.randint(0,len(error_addr['district'])-1)	
			district_str += error_addr['district'][random_district]
			for i in range(len(error_addr['district'][random_district])):
				if i == 0:
					tag_str += 'B-'+ addr + ' '
				elif i == len(error_addr['district'][random_district])-1:
					tag_str += 'E-'+ addr + ' '
				else:
					tag_str += 'I-'+ addr + ' '
			district_str,tag_str = supplyment(district_str,tag_str,addr,diction,diction_sort)

			if random.randint(0,1) == 0:
				district_str += error_addr['district'][random_district][-1]
				tag_str += 'E-district '
			if random.randint(0,5) == 0:
				district_str += '啊'
				tag_str += 'O '
			if random.randint(0,4) == 0:
				district_str += '额'
				tag_str += 'O '
			f_w.write(district_str +'\n')
			f_tag.write(tag_str[:-1]+'\n')

			fe_len = len(question_error_list)
			roadno_random_ask = random.randint(0,fe_len-1)
			question_write = question_error_list[roadno_random_ask]
			tag_str = ''
			if '#' in question_write:
				random_district = random.randint(0,len(error_addr['district'])-1)
				question_write = question_write.replace('#',error_addr['district'][random_district])
				for i in question_write:
					if i == error_addr['district'][random_district][0]:
						tag_str += 'B-' + addr + ' '
					elif i == error_addr['district'][random_district][-1]:
						tag_str += 'E-' + addr + ' '
					elif i in error_addr['district'][random_district][1:-1]:
						tag_str += 'I-' + addr + ' '
					else:
						tag_str += 'O' + ' '
			else:
				tag_str = ('O' + ' ') * len(question_write)
			f_w.write(question_write)
			f_tag.write(tag_str[:-1]+'\n')

			district_str = ''
			tag_str = ''
			if random.randint(0,4) == 0:
				district_str += '啊'
				tag_str += 'O '
			if random.randint(0,4) == 0:
				district_str += '不,'
				tag_str += 'O O '
			
			#@@@
			if random.randint(0,23) == 0:
				diction_len_addr = len(diction[addr]) - 1
				for len_addr in range(diction_len_addr):
					if random.randint(0,2) == 0:
						if diction[addr][len_addr] in chinese_dic.keys():
							cur_dic_list = chinese_dic[diction[addr][len_addr]]
							cur_dic_district = cur_dic_list[random.randint(0,len(cur_dic_list)-1)]
							district_str += cur_dic_district
							tag_str += 'O '*len(cur_dic_district)
							district_str += '的'
							tag_str += 'O '
							district_str += diction[addr][len_addr]
							tag_str += 'O '
							if random.randint(0,300) == 0:
								district_str += ','
								tag_str += 'O '

			district_str += diction[addr]
			for i in range(len(diction[addr])):
				if i == 0:
					tag_str += 'B-'+ addr + ' '
				elif i == len(diction[addr])-1:
					tag_str += 'E-'+ addr + ' '
				else:
					tag_str += 'I-'+ addr + ' '
			district_str,tag_str = supplyment(district_str,tag_str,addr,diction,diction_sort)
			if random.randint(0,4) == 0:
				district_str += '嗯'
				tag_str += 'O '
			if random.randint(0,5) == 0:
				district_str += '啊'
				tag_str += 'O '
			f_w.write(district_str +'\n')
			f_tag.write(tag_str[:-1]+'\n')




#town 乡镇街道
def f4_data(diction,diction_sort,error_addr):
	addr = 'town'
	if addr in diction.keys():
		town_1 = [] #symbol
		town_2 = [] #nonsymbol
		#f3_len = len(question_district_list)
		if '镇' in diction[addr]:
			for q in question_town_list1:
				if '&' in q:
					town_1.append(q)
				else:
					town_2.append(q)
		elif '道' in diction[addr]:
			for q in question_town_list3:
				if '&' in q:
					town_1.append(q)
				else:
					town_2.append(q)
		else:
			for q in question_town_list2:
				if '&' in q:
					town_1.append(q)
				else:
					town_2.append(q)
		if 'district' in diction.keys():
			f3_len = len(town_1)
			town_random_ask = random.randint(0,f3_len-1)
			question_write = town_1[town_random_ask].replace('&',diction['district'])
			if '@' in question_write:
				if 'city' in diction.keys():
					question_write = question_write.replace('@',diction['city'])
			f_w.write(question_write)
			tag_str = ''
			print(question_write)
			if 'city' in diction.keys():
				for i in question_write:
					if i == diction['district'][0]:
						tag_str += 'B-' + 'district' + ' '
					elif i == diction['district'][-1]:
						tag_str += 'E-' + 'district' + ' '
					elif i in diction['district'][1:-1]:
						tag_str += 'I-' + 'district' + ' '
					elif i == diction['city'][0]:
						tag_str += 'B-' + 'city' + ' '
					elif i == diction['city'][-1]:
						tag_str += 'E-' + 'city' + ' '
					elif i in diction['city'][1:-1]:
						tag_str += 'I-' + 'city' + ' '
					else:
						tag_str += 'O' + ' '
			else:
				for i in question_write:
					if i == diction['district'][0]:
						tag_str += 'B-' + 'district' + ' '
					elif i == diction['district'][-1]:
						tag_str += 'E-' + 'district' + ' '
					elif i in diction['district'][1:-1]:
						tag_str += 'I-' + 'district' + ' '
					else:
						tag_str += 'O' + ' '
			f_tag.write(tag_str[:-1]+'\n')
		else:
			f3_len = len(town_2)
			town_random_ask = random.randint(0,f3_len-1)
			f_w.write(town_2[town_random_ask])
			tag_str = 'O '*len(town_2[town_random_ask])
			f_tag.write(tag_str[:-1]+'\n')
		

		town_str = ''
		tag_str = ''
		if random.randint(0,4) == 0:
			town_str += '在'
			tag_str += 'O '
		if random.randint(0,5) == 0:
			town_str += '在,'
			tag_str += 'O O '
		if random.randint(0,5) == 0:
			town_str += '额'
			tag_str += 'O '
		if random.randint(0,5) == 0:
			town_str += '在那个'
			tag_str += 'O '*3

		if random.randint(0,5) == 0:
			town_str += diction[addr][0]
			tag_str += 'B-town '
			if random.randint(0,5) == 0:
				town_str += ','
			tag_str += 'O '

		if random.randint(0,23) == 0:
			town_str += diction[addr]
			for i in range(len(diction[addr])):
				if i == 0:
					tag_str += 'B-'+ addr + ' '
				elif i == len(diction[addr])-1:
					tag_str += 'E-'+ addr + ' '
				else:
					tag_str += 'I-'+ addr + ' '
			town_str,tag_str = supplyment(town_str,tag_str,addr,diction,diction_sort)
			if random.randint(0,4) == 0:
				town_str += '嗯'
				tag_str += 'O '
			f_w.write(town_str +'\n')
			f_tag.write(tag_str[:-1]+'\n')
		else:
			if random.randint(0,1) == 0:
				town_str += error_addr['town'][random.randint(0,len(error_addr['town'])-1)][0]
				tag_str += 'B-town '
			random_town = random.randint(0,len(error_addr['town'])-1)	
			town_str += error_addr['town'][random_town]
			for i in range(len(error_addr['town'][random_town])):
				if i == 0:
					tag_str += 'B-'+ addr + ' '
				elif i == len(error_addr['town'][random_town])-1:
					tag_str += 'E-'+ addr + ' '
				else:
					tag_str += 'I-'+ addr + ' '
			town_str,tag_str = supplyment(town_str,tag_str,addr,diction,diction_sort)

			if random.randint(0,1) == 0:
				town_str += error_addr['town'][random_town][-1]
				tag_str += 'E-town '
			if random.randint(0,5) == 0:
				town_str += '啊'
				tag_str += 'O '
			if random.randint(0,5) == 0:
				town_str += '额'
				tag_str += 'O '
			f_w.write(town_str +'\n')
			f_tag.write(tag_str[:-1]+'\n')

			fe_len = len(question_error_list)
			roadno_random_ask = random.randint(0,fe_len-1)
			question_write = question_error_list[roadno_random_ask]
			tag_str = ''
			if '#' in question_write:
				random_town = random.randint(0,len(error_addr['town'])-1)
				question_write = question_write.replace('#',error_addr['town'][random_town])
				for i in question_write:
					if i == error_addr['town'][random_town][0]:
						tag_str += 'B-' + addr + ' '
					elif i == error_addr['town'][random_town][-1]:
						tag_str += 'E-' + addr + ' '
					elif i in error_addr['town'][random_town][1:-1]:
						tag_str += 'I-' + addr + ' '
					else:
						tag_str += 'O' + ' '
			else:
				tag_str = ('O' + ' ') * len(question_write)
			f_w.write(question_write)
			f_tag.write(tag_str[:-1]+'\n')

			town_str = ''
			tag_str = ''
			if random.randint(0,5) == 0:
				town_str += '啊'
				tag_str += 'O '
			if random.randint(0,4) == 0:
				town_str += '不,'
				tag_str += 'O O '

			#@@@
			if random.randint(0,23) == 0:
				diction_len_addr = len(diction[addr]) - 1
				for len_addr in range(diction_len_addr):
					if random.randint(0,2) == 0:
						if diction[addr][len_addr] in chinese_dic.keys():
							cur_dic_list = chinese_dic[diction[addr][len_addr]]
							cur_dic_town = cur_dic_list[random.randint(0,len(cur_dic_list)-1)]
							town_str += cur_dic_town
							tag_str += 'O '*len(cur_dic_town)
							town_str += '的'
							tag_str += 'O '
							town_str += diction[addr][len_addr]
							tag_str += 'O '
							if random.randint(0,300) == 0:
								town_str += '嗯'
								tag_str += 'O '
							elif random.randint(0,300) == 0:
								town_str += ','
								tag_str += 'O '

			town_str += diction[addr]
			for i in range(len(diction[addr])):
				if i == 0:
					tag_str += 'B-'+ addr + ' '
				elif i == len(diction[addr])-1:
					tag_str += 'E-'+ addr + ' '
				else:
					tag_str += 'I-'+ addr + ' '
			town_str,tag_str = supplyment(town_str,tag_str,addr,diction,diction_sort)
			if random.randint(0,4) == 0:
				town_str += '嗯'
				tag_str += 'O '
			if random.randint(0,5) == 0:
				town_str += '啊'
				tag_str += 'O '
			f_w.write(town_str +'\n')
			f_tag.write(tag_str[:-1]+'\n')

#roadno
def f5_roadno_data(flag,diction_):
	addr = 'roadno'
	f5_len = len(question_road_list4)
	roadno_random_ask = random.randint(0,f5_len-1)
	question_write = question_road_list4[roadno_random_ask]
	if flag == 1:
		road = '路'
	elif flag == 2:
		road = '巷'
	else:
		road = '街'
	if '+' in question_write:
		question_write = question_write.replace('+',road)
	if '/' in question_write:
		question_write = question_write.replace('/',diction_['road'])
	f_w.write(question_write)
	tag_str = ''
	for i in question_write:
		if i == diction_['road'][0]:
			tag_str += 'B-' + 'road' + ' '
		elif i == diction_['road'][-1]:
			tag_str += 'E-' + 'road' + ' '
		elif i in diction_['road'][1:-1]:
			tag_str += 'I-' + 'road' + ' '
		else:
			tag_str += 'O' + ' '
	f_tag.write(tag_str[:-1]+'\n')

	roadno_str = ''
	tag_str = ''
	if random.randint(0,4) == 0:
		roadno_str += '在'
		tag_str += 'O '
	if random.randint(0,5) == 0:
		roadno_str += '在那个'
		tag_str += 'O '*3
	if random.randint(0,4) == 0:
		roadno_str += '额,'
		tag_str += 'O O '

	roadno_str += diction_['road']
	for i in range(len(diction_['road'])):
		if i == 0:
			tag_str += 'B-'+ 'road' + ' '
		elif i == len(diction_['road'])-1:
			tag_str += 'E-'+ 'road' + ' '
		else:
			tag_str += 'I-'+ 'road' + ' '
	
	roadno_str += diction_[addr]
	for i in range(len(diction_[addr])):
		if i == 0:
			tag_str += 'B-'+ addr + ' '
		elif i == len(diction_[addr])-1:
			tag_str += 'E-'+ addr + ' '
		else:
			tag_str += 'I-'+ addr + ' '
	if random.randint(0,4) == 0:
		roadno_str += '嗯'
		tag_str += 'O '
	f_w.write(roadno_str +'\n')
	f_tag.write(tag_str[:-1]+'\n')

#road 路巷街 
def f5_data(diction,diction_sort,error_addr):
	addr = 'road'
	if addr in diction.keys():
		road_1 = [] #symbol
		road_2 = [] #nonsymbol
		#f3_len = len(question_district_list)
		roadno_flag = -1 
		if '路' in diction[addr]:
			roadno_flag = 1
			for q in question_road_list1:
				if '#' in q:
					road_1.append(q)
				else:
					road_2.append(q)
		elif '巷' in diction[addr]:
			roadno_flag = 2
			for q in question_road_list2:
				if '#' in q:
					road_1.append(q)
				else:
					road_2.append(q)
		else:
			roadno_flag = 3
			for q in question_road_list3:
				if '#' in q:
					road_1.append(q)
				else:
					road_2.append(q)
		if 'town' in diction.keys():
			f5_len = len(road_1)
			road_random_ask = random.randint(0,f5_len-1)
			question_write = road_1[road_random_ask].replace('#',diction['town'])
			
			f_w.write(question_write)
			tag_str = ''
			for i in question_write:
				if i == diction['town'][0]:
					tag_str += 'B-' + 'town' + ' '
				elif i == diction['town'][-1]:
					tag_str += 'E-' + 'town' + ' '
				elif i in diction['town'][1:-1]:
					tag_str += 'I-' + 'town' + ' '
				else:
					tag_str += 'O' + ' '
			f_tag.write(tag_str[:-1]+'\n')
		else:
			f5_len = len(road_2)
			road_random_ask = random.randint(0,f5_len-1)
			f_w.write(road_2[road_random_ask])
			tag_str = 'O '*len(road_2[road_random_ask])
			f_tag.write(tag_str[:-1]+'\n')
		
		road_str = ''
		tag_str = ''
		if random.randint(0,4) == 0:
			road_str += '在'
			tag_str += 'O '
		if random.randint(0,5) == 0:
			road_str += '在那个'
			tag_str += 'O '*3
		if random.randint(0,3) == 0:
			road_str += '嗯,'
			tag_str += 'O O '

		if 'town' in diction.keys():
			if random.randint(0,1) == 0:
				road_str += diction['town']
				for i in range(len(diction['town'])):
					if i == 0:
						tag_str += 'B-'+ 'town' + ' '
					elif i == len(diction['town'])-1:
						tag_str += 'E-'+ 'town' + ' '
					else:
						tag_str += 'I-'+ 'town' + ' '
		if random.randint(0,1) == 0:
			random_road_num = random.randint(0,len(error_addr['road'])-1)
			random_road = error_addr['road'][random_road_num]
			print('!!:',random_road)
			add_road = random.randint(0,len(random_road)-1)
			road_str += random_road[:add_road]
			if add_road != 0: 
				tag_str += 'B-road '
				if add_road != len(random_road)-1:
					tag_str += 'I-road '* (add_road-1)
				else:
					tag_str += 'I-road '* (add_road-2)
					tag_str += 'E-road '
			if random.randint(0,5) == 0:
				road_str += ','
				tag_str += 'O '
			if random.randint(0,5) == 0:
				road_str += '不对'
				tag_str += 'O O '

		road_str += diction[addr]
		for i in range(len(diction[addr])):
			if i == 0:
				tag_str += 'B-'+ addr + ' '
			elif i == len(diction[addr])-1:
				tag_str += 'E-'+ addr + ' '
			else:
				tag_str += 'I-'+ addr + ' '

		#@@@
		if random.randint(0,23) == 0:
			diction_len_addr = len(diction[addr]) - 1
			count_road = 0
			for len_addr in range(diction_len_addr):
				if random.randint(0,2) == 0:
					if diction[addr][len_addr] in chinese_dic.keys():
						cur_dic_list = chinese_dic[diction[addr][len_addr]]
						cur_dic_road = cur_dic_list[random.randint(0,len(cur_dic_list)-1)]
						road_str += cur_dic_road
						tag_str += 'O '*len(cur_dic_road)
						road_str += '的'
						tag_str += 'O '
						road_str += diction[addr][len_addr]
						tag_str += 'O '
						if random.randint(0,300) == 0:
							road_str += ','
							tag_str += 'O '
						count_road += 1
				if count_road == 2:
					break

		for a in diction.keys():
			if (addr != a) and (addr in a) and len(addr)+1 == len(a):
				road_str += '和' + diction[a]
				road_str,tag_str = supplyment(road_str,tag_str,a,diction,diction_sort)
				tag_str += 'O '
				for i in range(len(diction[a])):
					if i == 0:
						tag_str += 'B-'+ addr + ' '
					elif i == len(diction[addr])-1:
						tag_str += 'E-'+ addr + ' '
					else:
						tag_str += 'I-'+ addr + ' '
				for x in diction_sort.keys():
					if diction_sort[x] == diction_sort[a] + 1:
						if 'roadno' in x:
							road_str += diction[x]
							for i in range(len(diction[x])):
								if i == 0:
									tag_str += 'B-'+ 'roadno' + ' '
								elif i == len(diction[x])-1:
									tag_str += 'E-'+ 'roadno' + ' '
								else:
									tag_str += 'I-'+ 'roadno' + ' '


		road_str,tag_str = supplyment(road_str,tag_str,addr,diction,diction_sort)

		if random.randint(0,4) == 0:
			road_str += '嗯'
			tag_str += 'O '

		f_w.write(road_str +'\n')
		f_tag.write(tag_str[:-1]+'\n')
		if addr+'no' in diction.keys():
			if diction_sort['road'] + 1 == diction_sort['roadno']:
				f5_roadno_data(roadno_flag,diction)

def f6_data(diction,diction_sort,error_addr):
	if ('community' in diction.keys()) or ('poi' in diction.keys()) or ('subpoi' in diction.keys()) or ('devzone' in diction.keys()) or ('houseno' in diction.keys()) or ('cellno' in diction.keys()) or ('floorno' in diction.keys()):
		f6_len = len(question_community_list)
		community_random_ask = random.randint(0,f6_len-1)
		f_w.write(question_community_list[community_random_ask])
		tag_str = 'O '*len(question_community_list[community_random_ask])
		f_tag.write(tag_str[:-1]+'\n')

		cur_str = ''
		tag_str = ''
		if random.randint(0,4) == 0:
			cur_str += '在'
			tag_str += 'O '
		if random.randint(0,5) == 0:
			cur_str += '在那个'
			tag_str += 'O '*3
		addr_flag = ''

		if 'community' in diction.keys():
			poi_list = ['community']
			for x in diction.keys():
				if 'community' in x and len('community') + 1 == len(x):
					poi_list.append(x)
			for p in poi_list:
				cur_str += diction[p]
				for i in range(len(diction[p])):
					if i == 0:
						tag_str += 'B-'+ 'community' + ' '
					elif i == len(diction[p])-1:
						tag_str += 'E-'+ 'community' + ' '
					else:
						tag_str += 'I-'+ 'community' + ' '
				cur_str,tag_str = supplyment(cur_str,tag_str,p,diction,diction_sort)
			if random.randint(0,5) == 0:
				cur_str += ','
				tag_str += 'O '
			addr_flag = 'community'
			#@@@
			if random.randint(0,23) == 0:
				count_commu = 0
				diction_len_addr = len(diction['community']) - 1
				for len_addr in range(diction_len_addr):
					if random.randint(0,2) == 0:
						if diction['community'][len_addr] in chinese_dic.keys():
							cur_dic_list = chinese_dic[diction['community'][len_addr]]
							cur_dic_comm = cur_dic_list[random.randint(0,len(cur_dic_list)-1)]
							cur_str += cur_dic_comm
							tag_str += 'O '*len(cur_dic_comm)
							cur_str += '的'
							tag_str += 'O '
							cur_str += diction['community'][len_addr]
							tag_str += 'O '
							if random.randint(0,300) == 0:
								cur_str += ','
								tag_str += 'O '
							count_commu += 1
					if count_commu == 4:
						break

		if 'devzone' in diction.keys():
			cur_str += diction['devzone']
			for i in range(len(diction['devzone'])):
				if i == 0:
					tag_str += 'B-'+ 'devzone' + ' '
				elif i == len(diction['devzone'])-1:
					tag_str += 'E-'+ 'devzone' + ' '
				else:
					tag_str += 'I-'+ 'devzone' + ' '
				cur_str,tag_str = supplyment(cur_str,tag_str,'devzone',diction,diction_sort)
			if random.randint(0,5) == 0:
				cur_str += ','
				tag_str += 'O '
			addr_flag = 'devzone'
		if 'poi' in diction.keys():
			poi_list = ['poi']
			for x in diction.keys():
				if 'poi' in x and len('poi') + 1 == len(x):
					poi_list.append(x)
			for p in poi_list:
				cur_str += diction[p]
				for i in range(len(diction[p])):
					if i == 0:
						tag_str += 'B-'+ 'poi' + ' '
					elif i == len(diction[p])-1:
						tag_str += 'E-'+ 'poi' + ' '
					else:
						tag_str += 'I-'+ 'poi' + ' '
				cur_str,tag_str = supplyment(cur_str,tag_str,p,diction,diction_sort)
			if random.randint(0,5) == 0:
				cur_str += '额,'
				tag_str += 'O O '
			addr_flag = 'poi'
			if random.randint(0,5) == 0:
				cur_str += ','
				tag_str += 'O '
			#@@@
			if random.randint(0,23) == 0:
				count_poi = 0
				diction_len_addr = len(diction['poi']) - 1
				for len_addr in range(diction_len_addr):
					if random.randint(0,2) == 0:
						if diction['poi'][len_addr] in chinese_dic.keys():
							cur_dic_list = chinese_dic[diction['poi'][len_addr]]
							cur_dic_poi = cur_dic_list[random.randint(0,len(cur_dic_list)-1)]
							cur_str += cur_dic_poi
							tag_str += 'O '*len(cur_dic_poi)
							cur_str += '的'
							tag_str += 'O '
							cur_str += diction['poi'][len_addr]
							tag_str += 'O '
							if random.randint(0,300) == 0:
								cur_str += ','
								tag_str += 'O '
							count_poi += 1
					if count_poi == 3:
						break

		if 'subpoi' in diction.keys():
			poi_list = ['subpoi']
			for x in diction.keys():
				if 'subpoi' in x and len('subpoi') + 1 == len(x):
					poi_list.append(x)
			for p in poi_list:
				cur_str += diction[p]
				for i in range(len(diction[p])):
					if i == 0:
						tag_str += 'B-'+ 'subpoi' + ' '
					elif i == len(diction[p])-1:
						tag_str += 'E-'+ 'subpoi' + ' '
					else:
						tag_str += 'I-'+ 'subpoi' + ' '
				cur_str,tag_str = supplyment(cur_str,tag_str,p,diction,diction_sort)
			addr_flag = 'subpoi'


		if 'houseno' in diction.keys() or 'cellno' in diction.keys() or 'floorno' in diction.keys():
			if random.randint(0,23) != 0:
				if 'houseno' in diction.keys():
					cur_str += diction['houseno']
					for i in range(len(diction['houseno'])):
						if i == 0:
							tag_str += 'B-'+ 'houseno' + ' '
						elif i == len(diction['houseno'])-1:
							tag_str += 'E-'+ 'houseno' + ' '
						else:
							tag_str += 'I-'+ 'houseno' + ' '
					cur_str,tag_str = supplyment(cur_str,tag_str,'houseno',diction,diction_sort)
				if 'cellno' in diction.keys():
					cur_str += diction['cellno']
					for i in range(len(diction['cellno'])):
						if i == 0:
							tag_str += 'B-'+ 'cellno' + ' '
						elif i == len(diction['cellno'])-1:
							tag_str += 'E-'+ 'cellno' + ' '
						else:
							tag_str += 'I-'+ 'cellno' + ' '
					cur_str,tag_str = supplyment(cur_str,tag_str,'cellno',diction,diction_sort)
				if 'floorno' in diction.keys():
					cur_str += diction['floorno']
					for i in range(len(diction['floorno'])):
						if i == 0:
							tag_str += 'B-'+ 'floorno' + ' '
						elif i == len(diction['floorno'])-1:
							tag_str += 'E-'+ 'floorno' + ' '
						else:
							tag_str += 'I-'+ 'floorno' + ' '
					cur_str,tag_str = supplyment(cur_str,tag_str,'floorno',diction,diction_sort)
				if random.randint(0,5) == 0:
					cur_str += '啊'
					tag_str += 'O '
				if not cur_str:
					cur_str += '啊?'
					tag_str += 'O O '
				f_w.write(cur_str +'\n')
				f_tag.write(tag_str[:-1]+'\n')
				if 'community' in diction.keys():
					if random.randint(0,1) == 0:
						fe_len = len(question_error_list)
						roadno_random_ask = random.randint(0,fe_len-1)
						question_write = question_error_list[roadno_random_ask]
						tag_str = ''
						if '#' in question_write:
							random_community = random.randint(0,len(error_addr['community'])-1)
							question_write = question_write.replace('#',error_addr['community'][random_community])
							for i in question_write:
								if i == error_addr['community'][random_community][0]:
									tag_str += 'B-' + 'community' + ' '
								elif i == error_addr['community'][random_community][-1]:
									tag_str += 'E-' + 'community' + ' '
								elif i in error_addr['community'][random_community][1:-1]:
									tag_str += 'I-' + 'community' + ' '
								else:
									tag_str += 'O' + ' '
						else:
							tag_str = ('O' + ' ') * len(question_write)
						f_w.write(question_write)
						f_tag.write(tag_str[:-1]+'\n')
						cur_str = ''
						tag_str = ''
						if random.randint(0,4) == 0:
							cur_str += '不,'
							tag_str += 'O O '
						if random.randint(0,4) == 0:
							cur_str += '是'
							tag_str += 'O '

						#@@@
						if random.randint(0,23) == 0:
							count_commu = 0
							diction_len_addr = len(diction['community']) - 1
							for len_addr in range(diction_len_addr):
								if random.randint(0,2) == 0:
									if diction['community'][len_addr] in chinese_dic.keys():
										cur_dic_list = chinese_dic[diction['community'][len_addr]]
										cur_dic_comm = cur_dic_list[random.randint(0,len(cur_dic_list)-1)]
										cur_str += cur_dic_comm
										tag_str += 'O '*len(cur_dic_comm)
										cur_str += '的'
										tag_str += 'O '
										cur_str += diction['community'][len_addr]
										tag_str += 'O '
										if random.randint(0,300) == 0:
											cur_str += ','
											tag_str += 'O '
										count_commu += 1
								if count_commu == 3:
									break
						cur_str += diction['community']
						for i in range(len(diction['community'])):
							if i == 0:
								tag_str += 'B-'+ 'community' + ' '
							elif i == len(diction['community'])-1:
								tag_str += 'E-'+ 'community' + ' '
							else:
								tag_str += 'I-'+ 'community' + ' '
						if random.randint(0,4) == 0:
							cur_str += '啊'
							tag_str += 'O '
						f_w.write(cur_str +'\n')
						f_tag.write(tag_str[:-1]+'\n')


			else:
				if not cur_str:
					cur_str += '啊?'
					tag_str += 'O O '
				f_w.write(cur_str +'\n')
				f_tag.write(tag_str[:-1]+'\n')
				f7_len = len(question_detail_list)
				roadno_random_ask = random.randint(0,f7_len-1)
				question_write = question_detail_list[roadno_random_ask]
				if '/' in question_write:
					if addr_flag:
						question_write = question_write.replace('/',diction[addr_flag])
					else:
						question_write = question_write.replace('/','')
				f_w.write(question_write)
				tag_str = ''
				if addr_flag:
					for i in question_write:
						if i == diction[addr_flag][0]:
							tag_str += 'B-' + addr_flag + ' '
						elif i == diction[addr_flag][-1]:
							tag_str += 'E-' + addr_flag + ' '
						elif i in diction[addr_flag][1:-1]:
							tag_str += 'I-' + addr_flag + ' '
						else:
							tag_str += 'O' + ' '
				else:
					tag_str = ('O ') * len(question_write)
				f_tag.write(tag_str[:-1]+'\n')
				cur_str = ''
				tag_str = ''
				if random.randint(0,5) == 0:
					cur_str += '在,'
					tag_str += 'O O '
				if random.randint(0,4) == 0:
					cur_str += '在'
					tag_str += 'O '
				if random.randint(0,3) == 0:
					cur_str += '呃'
					tag_str += 'O '
				if 'houseno' in diction.keys():
					cur_str += diction['houseno']
					for i in range(len(diction['houseno'])):
						if i == 0:
							tag_str += 'B-'+ 'houseno' + ' '
						elif i == len(diction['houseno'])-1:
							tag_str += 'E-'+ 'houseno' + ' '
						else:
							tag_str += 'I-'+ 'houseno' + ' '
					cur_str,tag_str = supplyment(cur_str,tag_str,'houseno',diction,diction_sort)
				if 'cellno' in diction.keys():
					cur_str += diction['cellno']
					for i in range(len(diction['cellno'])):
						if i == 0:
							tag_str += 'B-'+ 'cellno' + ' '
						elif i == len(diction['cellno'])-1:
							tag_str += 'E-'+ 'cellno' + ' '
						else:
							tag_str += 'I-'+ 'cellno' + ' '
					cur_str,tag_str = supplyment(cur_str,tag_str,'cellno',diction,diction_sort)
				if 'floorno' in diction.keys():
					cur_str += diction['floorno']
					for i in range(len(diction['floorno'])):
						if i == 0:
							tag_str += 'B-'+ 'floorno' + ' '
						elif i == len(diction['floorno'])-1:
							tag_str += 'E-'+ 'floorno' + ' '
						else:
							tag_str += 'I-'+ 'floorno' + ' '
					cur_str,tag_str = supplyment(cur_str,tag_str,'floorno',diction,diction_sort)
				if random.randint(0,3) == 0:
					cur_str += '啊'
					tag_str += 'O '
				if random.randint(0,5) == 0:
					cur_str += '嗯'
					tag_str += 'O '
				if random.randint(0,5) == 0:
					cur_str += ','
					tag_str += 'O '
				f_w.write(cur_str +'\n')
				f_tag.write(tag_str[:-1]+'\n')
		else:
			f_w.write(cur_str +'\n')
			f_tag.write(tag_str[:-1]+'\n')




	
if __name__ == '__main__':
	chinese_dic = diction_chinese()
	list_constrct(f_list)
	cur_str = ''
	cur_addr_dic = {}
	cur_key_sort = {}
	cur_key_count = {}
	key_count = 0
	for line in f_address:
		if line != '\n':
			line = line.strip('\n')
			line = line.split(' ')
			tag_list = line[1].split('-')
			if tag_list[0] == 'S':
				cur_addr_dic[tag_list[1]] = line[0]
				cur_key_sort[tag_list[1]] = key_count
				key_count += 1
			elif tag_list[0] != 'E' and tag_list[0] != 'O':
				cur_str += line[0]
			elif tag_list[0] == 'E':
				cur_str += line[0]
				if tag_list[1] not in cur_key_count.keys():
					cur_addr_dic[tag_list[1]] = cur_str
					cur_key_sort[tag_list[1]] = key_count
					key_count += 1
					cur_str = ''
					cur_key_count[tag_list[1]] = 1
				else:
					cur_key_count[tag_list[1]] += 1
					cur_key = tag_list[1] + str(cur_key_count[tag_list[1]])
					cur_addr_dic[cur_key] = cur_str
					cur_key_sort[cur_key] = key_count
					key_count += 1
					cur_str = ''


		else:
			print(cur_addr_dic)
			print(cur_key_sort)
			error_tag_addr = {}
			for l in f_ty:
				if l != '\n':
					l = l.strip('\n')
					if l.split(':')[1]:
						error_tag_addr[l.split(':')[0]] = l.split(':')[1].split(',')
				else:
					break
			print('##',error_tag_addr)
			f1_data(cur_addr_dic,cur_key_sort)
			f2_data(cur_addr_dic,cur_key_sort)
			f3_data(cur_addr_dic,cur_key_sort,error_tag_addr)
			f4_data(cur_addr_dic,cur_key_sort,error_tag_addr)
			f5_data(cur_addr_dic,cur_key_sort,error_tag_addr)
			f6_data(cur_addr_dic,cur_key_sort,error_tag_addr)
			f_w.write('\n')
			f_tag.write('\n')
			cur_addr_dic = {}
			cur_key_sort = {}
			cur_key_count = {}
			key_count = 0
