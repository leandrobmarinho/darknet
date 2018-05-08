import argparse, glob, os, numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", type=str, help="images path to write in the file")
parser.add_argument("-ptrain", "--ptrain", type=float, help="percentage for training between 0 and 1")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")


args = parser.parse_args()

if args.path:
	files = glob.glob(os.path.join(args.path, '*.jpg'))
	np.random.shuffle(files)

	ptrain = 0.95
	if args.ptrain:
		ptrain = args.ptrain


	if files:
		print("Num train: \t{}\nNum test: \t{}".format(int(len(files)*ptrain), len(files) - int(len(files)*(ptrain))))
		
		file_train = open("train.txt","w")
		file_test = open("test.txt","w")		
		
		cont = 1
		for filename in files:
			filename = "data/img/{}".format(os.path.basename(filename))
			if args.verbose:
				type_file = ("train" if cont <= int(len(files)*ptrain) else "test")
				print("writing in {}.txt '{}'".format(type_file, filename))

			if cont <= int(len(files)*ptrain):
				file_train.write("{}\n".format(filename))
			else:
				file_test.write("{}\n".format(filename))

			cont += 1

		file_train.close()
		file_test.close()
		print("done")

	else:
		print("No images")