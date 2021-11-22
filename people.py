class Mentor:
	def __init__(self, mentor_dictionary):
		
		mentor = mentor_dictionary

		self.name = mentor['name']
		self.comm = mentor["comm"]
		self.email = mentor['email']
		self.city = mentor["city"]
		self.timezone = mentor["timezone"]
		self.personality = mentor["personality"]
		self.linkedin = mentor["linkedin"]
		
		if mentor.get("pic"):
			mentor["pic"] = mentor["pic"].replace('open', 'thumbnail')
		self.pic = mentor["pic"]
		
		self.job = mentor["job"]
		self.daily_work = mentor["daily_work"]
		self.technical_passion = mentor["technical_passion"]

		self.why = mentor["why"]
		self.advice = mentor["advice"]
		self.experience = mentor["experience"]
		self.hb_exp = mentor["hb_exp"]
		self.strengths = mentor["strengths"]


		if mentor.get("help_topics"):
			mentor["help_topics"] = mentor["help_topics"].strip().split(',')
		self.help_topics = mentor["help_topics"]
		
		
		self.mentee = mentor["mentee"]
		
	def __repr__(self):
		return "<Mentor {self.name}>"


class Student:
	def __init__(self, student_dictionary):
		
		student = student_dictionary 

		keys = ["pic", "name", "comm", "email", "city", "timezone", 
		        "personality", "linkedin", "before_hb", "roles", "worry", 
		        "mentor", "saying"]

		for k in keys:
			if not k in student:
				student[k] = None

		self.pic = student["pic"]
		self.name = student["name"]
		self.comm = student["comm"]
		self.email = student["email"]
		self.city = student["city"]
		self.timezone = student["timezone"]
		self.personality = student["personality"]
		self.linkedin = student["linkedin"]
		self.before_hb = student["before_hb"]
		self.roles = student["roles"]
		self.worry = student["worry"]
		self.mentor = student["mentor"]
		self.saying = student["saying"]
		
	def __repr__(self):
		return "<Student {self.name}>"
		


