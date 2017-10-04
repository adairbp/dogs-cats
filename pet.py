class Pet(object):
    def __init__(self, id, name, type, birthday, owner):
    	self.id = id
        self.type = type
        self.name = name
        self.birthday = birthday
        self.owner = owner

    def __str__(self):
        return "%sThis is a %s" % (self.id, self.type, self.name, self.owner)

    def save(self):
    	pass

    def delete(self):
    	pass

class Dog(Pet):
    def __init__(self, id, name, birthday, owner):
        Pet.__init__(self, id, name, "Dog", birthday, owner)

class Cat(Pet):
    def __init__(self, id, name, birthday, owner):
        Pet.__init__(self, id, name, "Cat", birthday, owner)
       





