import os
import shutil
import sys
import commands
import re
import zipfile
import glob

def get_special_paths(dirname):
#	print dirname
	result = []
	paths = os.listdir(dirname)
	for fname in paths:
		match = re.search(r'__(\w+)__', fname)
		if match:
			result.append(os.path.abspath(os.path.join(dirname, fname)))
	
	return result


def copy_to(paths, to_dir):
#	print to_dir
#	print paths
	if not os.path.exists(to_dir):
		os.mkdir(to_dir)
	for path in paths:
		fname = os.path.basename(path)
		shutil.copy(path, os.path.join(to_dir, fname))


def zip_to(paths, tozip):
#	print paths
#	print zipfile
#	print "nidhin kuttan"
	zipper = zipfile.ZipFile(tozip , "w")
	for file in paths:
		zipper.write(file, os.path.basename(file), zipfile.ZIP_DEFLATED)
	
	zipper.close()


def main():
  
  	args = sys.argv[1:]
	if not args:
    		print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    		sys.exit(1)

  	todir = ''
  	if args[0] == '--todir':
    		todir = args[1]
    		del args[0:2]

  	tozip = ''
  	if args[0] == '--tozip':
    		tozip = args[1]
 		del args[0:2]

  	if len(args) == 0:
    		print "error: must specify one or more dirs"
    		sys.exit(1)
  	
	paths = []
	for dirname in args:
   		paths.extend(get_special_paths(dirname))

  	if todir:
    		copy_to(paths, todir)
	elif tozip:
		zip_to(paths, tozip)
  	else:
#		print "nidhin"
    		print '\n'.join(paths)
  # LAB(end solution)

if __name__ == "__main__":
  main()
                                                                                   

