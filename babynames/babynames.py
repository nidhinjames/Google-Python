import re
import sys

def extract_names(filename):
	names = []
	sorted_names = []	
	f = open(filename, 'r')
	txt = f.read()
	year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', txt)
	
	if year_match:
		tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', txt)
	else:
		sys.stderr.write('Couldn\'t find the year!\n')
    		sys.exit(1)
	
	#for i in tuples:
	#	print i[0], i[1], i[2]
	names_to_rank = {}
	for rank_tuple in tuples:
		(rank, boyname, girlname) = rank_tuple
		if boyname not in names_to_rank:
			names_to_rank[boyname] = rank
		if girlname not in names_to_rank:
			names_to_rank[girlname] = rank
	
	sorted_names = sorted(names_to_rank.keys())
	print sorted_names
	for name in sorted_names:
	 	names.append(name +" "+ names_to_rank[name])
	
	for i in names:
		print i

def main():
	

	extract_names(sys.argv[1])


if __name__=='__main__':
	main()
