import uuid
import csv
import collections

class Owner(object):
    def __init__(self, first_name, second_name, pets=[], id=uuid.uuid4()):
    	self.id = id
        self.first_name = first_name
        self.second_name = second_name
    	self.pets = pets

    def __str__(self):
        return "ID: %i Name %s %s" % (self.id, self.first_name, self.second_name)  

	def delete(self):
		pass

	def save(self):
		pass


