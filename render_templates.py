import csv
from jinja2 import Template, Environment, FileSystemLoader
from people import Mentor, Student

env = Environment(loader=FileSystemLoader('templates'))
# t = Template(open("templates/profile.html").read())

OUTPUT_DIR = "profiles/perf-1-students/"
DATA_FILE = "output/data5.csv"


def create_dict_with_headers(line, headers):
	person_data = {}
	for i, val in enumerate(line):
		if val == "":
			val = None

		person_data[headers[i]] = val

	return person_data


def write_content(content, name):
	
	# create profile
	filename = OUTPUT_DIR + name.replace(' ', '')
	f2 = open(filename+".html", "w+")
	f2.write(content)
	f2.close()


def get_csv_reader(filename):
	f = open(filename)
	lines = f.read().splitlines()
	
	return csv.reader(lines, quotechar='"', delimiter=',',
                         quoting=csv.QUOTE_ALL, 
                         skipinitialspace=True)

def get_objects(filename, cls):
	objects = []
	reader = get_csv_reader(filename)
	headers = next(reader)

	for line in reader:
		d = create_dict_with_headers(line, headers)
		objects.append(cls(d))

	return objects


def make_mentor_profiles():
	mentors = get_objects(DATA_FILE, Mentor)
	# create_profiles(mentors, t)

	template = env.get_template("mentor-individual.html")

	for m in mentors:
		content = template.render(mentor=m)
		write_content(content, m.name)


def make_student_profiles():
	students = get_objects(DATA_FILE, Student)

	template = env.get_template("short-profile.html")

	for s in students:
		content = template.render(student=s)
		write_content(content, s.name)

def make_student_packet():
	students = get_objects(DATA_FILE, Student)

	template = env.get_template("short-profile-packet.html")

	content = template.render(students=students)
	write_content(content, "packet")

# make_mentor_profiles()
# make_student_profiles()
make_student_packet()
