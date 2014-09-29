idef match_words(words):
	count = 0
	for i in words:
		if len(i) >= 2 and i[0] == i[-1]:
			count +=1
	return count
def front_x(words):
	z = []
	y = []
	for i in words:
		if i[0] == 'z':
			z.append(i)
		else:
			y.append(i)
	return  sorted(z) + sorted(y)		

def sorted_last(words):
	
	
		
		





##### print match_words(["nidhin","a","james","nidhinkuttan"])
#####print front_x(["zandu","opopo","apple","app","zyz"])
print sorted_last([(1,7),(1,2),(1,2,8)])
