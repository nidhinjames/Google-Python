import sys
import random
def mimic_dict(filename):
	print filename
	mimic_dict = {}
	f = open(filename, 'r')
	text = f.read()	
#	print text
	words = text.split()
#	print words
	prev = ''
	for word in words:
		if not prev in mimic_dict:
			mimic_dict[prev] = [word]
		else:
			mimic_dict[prev].append(word)
		prev = word
	return  mimic_dict


def print_mimic(mimic_dict, word):
	"""Given mimic dict and start word, prints 200 random words."""
  	# +++your code here+++
  	# LAB(begin solution)
	for unused_i in range(200):
    		print word,
    		nexts = mimic_dict.get(word)          # Returns None if not found
    		if not nexts:
      			nexts = mimic_dict['']  # Fallback to '' if not found
    		word = random.choice(nexts)




#mimic_dict("alice2.txt")

def main():
	if len(sys.argv) != 2:
    		print 'usage: ./mimic.py file-to-read'
    		sys.exit(1)

	dict = mimic_dict(sys.argv[1])
  	print_mimic(dict, '')


if __name__ == '__main__':
  main()

