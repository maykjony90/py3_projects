class Patient:
	def __init__(self, first, last, grafts):
		self.first = first
		self.last = last
		self.grafts = grafts


	@property
	def email(self):
		return "{}.{}@drkeser.com".format(self.first, self.last)

	@property
	def fullname(self):
		return "{} {}".format(self.first, self.last)

	def __repr__(self):
		return "Patients('{}', '{}', '{}'".format(self.first, self.last, self.grafts)
