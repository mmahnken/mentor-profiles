import csv

HEADER_ROW = ['name', 'pic', 'email', 'Are you currently employed?', 'job', 'daily_work', 'help_topics', 'technical_passion', 'why', 'mentee', 'Have you mentored students before?', 'experience', 'comm', 'city', 'timezone', 'hb_exp', 'strengths', 'personality', 'advice', 'It there any additional support we can give you? ', 'linkedin', 'What is your Tech Stack? ', 'Select the following that applies......', '', 'Timestamp']
STUDENT_HEADER_ROW = ['Timestamp', 'email', 'linkedin', 'name', 'pic', 'Mentorship options: Option 1 - two mentors throughout the program, Option 2 - One mentor now and one mentor during the job search', 'worry', 'before_hb', 'mentor', 'comm', 'roles', 'city', 'timezone', 'saying', 'personality']
DATA = "data/perf-1-2.csv"
OUTPUT = "output/data5.csv"

MENTOR_ATTRS = ["name",
				"comm",
				"email",
				"city",
				"timezone",
				"personality",
				"linkedin",
				"pic",
				"job",
				"daily_work",
				"technical_passion",
				"why",
				"advice",
				"experience",
				"hb_exp",
				"strengths",
				"help_topics",
				"mentee",
]

STUDENT_ATTRS = ["pic",
				"name",
				"comm",
				"email",
				"city",
				"timezone",
				"personality",
				"linkedin",
				"before_hb",
				"roles",
				"worry",
				"mentor",
				"saying",
]


def get_new_header_row(headers, attrs):
	

	new_headers = []

	for i, val in enumerate(headers):
		print()
		print()
		print(val, '\n\n')
		print('choose a name for this')
		print('hit ENTER to skip')
		for j, nickname in enumerate(attrs):
			print(j, nickname)

		choice = input("> ")
		if choice:
			new_headers.append(attrs[int(choice)])
		else:
			new_headers.append(val)

	return new_headers

def replace_header_row(header):

	with open(DATA, 'r') as fp:
	    reader = csv.DictReader(fp, fieldnames=header)

	    # use newline='' to avoid adding new CR at end of line
	    with open(OUTPUT, 'w', newline='') as fh: 
	        writer = csv.DictWriter(fh, fieldnames=reader.fieldnames)
	        writer.writeheader()
	        header_mapping = next(reader)
	        writer.writerows(reader)

def get_headers(filename):
	f = open(filename)
	spamreader = csv.reader(f, delimiter=',', quotechar='"')
	return next(spamreader)

if __name__ == "__main__":
	print("Re create header row? y/n")
	choice = input("> ")
	
	f = open(DATA)
	

	if choice == "y" or not HEADER_ROW:


		current_headers = get_headers(DATA)
		new_headers = get_new_header_row(current_headers, STUDENT_ATTRS)
		print(f"\n\n\nNEW HEADER ROW\n\n\n{new_headers}\n\n")
	
	replace_header_row(new_headers)
	