#! /usr/bin/python3
import sys 

clique=[[0,1,2,3,4,5,6,7,8],\
[9,10,11,12,13,14,15,16,17],\
[18,19,20,21,22,23,24,25,26],\
[27,28,29,30,31,32,33,34,35],\
[36,37,38,39,40,41,42,43,44],\
[45,46,47,48,49,50,51,52,53],\
[54,55,56,57,58,59,60,61,62],\
[63,64,65,66,67,68,69,70,71],\
[72,73,74,75,76,77,78,79,80],\
[0,9,18,27,36,45,54,63,72],\
[1,10,19,28,37,46,55,64,73],\
[2,11,20,29,38,47,56,65,74],\
[3,12,21,30,39,48,57,66,75],\
[4,13,22,31,40,49,58,67,76],\
[5,14,23,32,41,50,59,68,77],\
[6,15,24,33,42,51,60,69,78],\
[7,16,25,34,43,52,61,70,79],\
[8,17,26,35,44,53,62,71,80],\
[0,1,2,9,10,11,18,19,20],\
[3,4,5,12,13,14,21,22,23],\
[6,7,8,15,16,17,24,25,26],\
[27,28,29,36,37,38,45,46,47],\
[30,31,32,39,40,41,48,49,50],\
[33,34,35,42,43,44,51,52,53],\
[54,55,56,63,64,65,72,73,74],\
[57,58,59,66,67,68,75,76,77],\
[60,61,62,69,70,71,78,79,80]\
]

def checker(chek):
	#print(chek)
	wrong = 0
	for i in clique:
		count = 0
		for ii in i:
			#print(ii)
				count += int(chek[ii])
		#print(count)
		if count != 45:
			wrong += 1
			wrong += 1
			print(i)
	#print(wrong)
	if wrong == 0:
		return True
	else:
		return False

def finder(dup, woo):
	#print(dup)
	for i in dup:
		for j in dup:
			weewoo = woo.copy()
			#print(woo[i],woo[j])
			weewoo[i] = str(woo[j])
			weewoo[j] = str(woo[i])
			if checker(weewoo) == True:
				#print(i,j)
				return i,j
				
	
def missingStuff(wee):
	dup = []
	store = {}
	res = []
	for ii in clique:
		temp2 = {}
		for iii in ii:
			if wee[iii] in temp2:
				temp2[wee[iii]].append(iii)
				dup.append(temp2[wee[iii]][0])
				dup.append(iii)
				#print(temp2)
			else:
				temp2[wee[iii]] = [iii]
	#print(temp2)
	dup = set(dup)
	#finder(dup)
	return dup
	#for i in range (len(dup)-1):
		#if dup[i] == dup[i+1]:
			#res.append(dup[i])
	#return (res)
	
with open(sys.argv[1], "r") as fp:
	content = fp.read().split('\n')
	#total = content.split(',')
	totnum = []
	
	for b in content:
		for a in b.split(','):
			if a.isdigit():
				totnum.append(a)
	print(totnum)
			
	#for i in range(int(len(content)/11)):
	while len(totnum)> 0:
		arr = []
		arr = totnum[:81]
		totnum = totnum[81:]

		
		#print(title, puzzle)
		#for j in range(9):
			#temp = [x for x in puzzle[j] if x != ","]
			#arr += temp
		print(arr)
		potential = missingStuff(arr)
		beepbop = finder(potential,arr)
		boop = []
		for v in beepbop:
			boop.append(str(v))
		with open (sys.argv[2], "a") as wawaeewa:
			wawaeewa.write(",".join(boop))
			wawaeewa.write("\n")
		
		
		

			
			
		
		
	
	