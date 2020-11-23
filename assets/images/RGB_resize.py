from PIL import Image
import math
import os, sys
#for reading the image orientation
# from PIL import ExifTags

def is_correct_file_type(fname):
	
	return (fname[-3:] == 'JPG') or (fname[-3:] == 'jpg')


def cvt_size(img, h, w):
	_, _, orig_h, orig_w = img.getbbox()
	
	if (w == -1) and (h == -1):
		h = orig_h
		w = orig_w

	elif w == -1:

		w = math.floor(h * orig_w / orig_h)
		#print("new width: ", w)

	elif h == -1:
		h = math.floor(w * orig_h / orig_w)

	img_size = (h,w)

	img.thumbnail(img_size)
	
	return img


def main(argv):
	if (len(argv) != 4):
	    print("please give following info: input_file_name, output_file_name, output_size_h, output_size_w")
	    print("Want to process all files? --> leave input fname as '-A', and give random output file names")
	    print("Want to keep aspect ratio? --> leave width as '-1'")
	    return

	#get Exif key corresponding to "Orientation"
	# for attr in ExifTags.TAGS.keys():
	# 	if ExifTags.TAGS[attr]=='Orientation':
	# 		attrKey = attr
	# 		break


	fname = argv[0]
	out_file_name = argv[1]
	size_h = int(argv[2])
	size_w = int(argv[3])

	if not fname == "-A":
		#file_name = "HW3Q2_1.jpg"
		img = Image.open(fname)
		img = cvt_size(img, size_h, size_w)
		#img.save('ECE493-02.jpg')
		img.save(out_file_name)

	else:
		for fname in os.listdir(u'.'):

			if not is_correct_file_type(fname):
				continue

			print("processing:", fname)
			img = Image.open(fname)
			exif = img.info['exif']
			img = cvt_size(img, size_h, size_w)

			fname_list = fname.split('.')
			img.save('.'.join(fname_list[:-1]) + "-BW"+"_"+str(size_w) + "_" + str(size_h) + "." + fname_list[-1], exif = exif)
	
if __name__ == "__main__":
   main(sys.argv[1:])