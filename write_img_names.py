import argparse, glob, os


def write_filenames(pathfiles, type_file, verbose):
	files = glob.glob(os.path.join(pathfiles, '*.jpg'))

	if files:
		fileWrite = open("{}.txt".format(type_file),"w")

		cont = 1
		for filename in files:
			filename = "data/img/{}".format(os.path.basename(filename))

			if verbose:
				print("writing in {}.txt '{}'".format(type_file, filename))

			fileWrite.write("{}\n".format(filename))

			cont += 1
		fileWrite.close()
		print("Num files to {}: {}".format(type_file, cont))

	else:
		print("No images to {}".format(type_file))


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-ptr", "--pathTrain", type=str, help="images path to write in the train file")
	parser.add_argument("-ptes", "--pathTest", type=str, help="images path to write in the train file")
	parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")

	args = parser.parse_args()

	if args.ptr
		write_filenames(args.ptr, "train", args.verbose)

	if args.ptes
		write_filenames(args.ptes, "test", args.verbose)