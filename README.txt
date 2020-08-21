This program includes both indexing and a randomized search functionality (i.e. pick a random video file that matches the given pattern). Note that, when searching, the chosen file will open automatically. Supported file formats are: .mkv, .wmv, .mp4, .m4v, .mov, and .avi. Currently only supports one search term.

Syntax for the Indexer:
indexer.py [directory path] [index file(optional)]

Syntax for the search:
opener.py [index file] [arguments (optional)]

optional extra search arguments (add before search term):
	fullpath - search the full file path, rather than just file names. Useful if you want to choose randomly from a sub-directory
	add "-" (without quotes) to the start of a search term to exclude matching files from the possibilities