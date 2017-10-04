# importing locals
from pet import Pet, Dog, Cat
from owners import Owner
# importing libs
import uuid
import csv

# creating owners
name = 'Alex'
lastname = 'Villanueva'

owner = Owner(name, lastname)
jorge = Owner('Jorge', 'Negron')

# creating pets
polly = Dog(uuid.uuid4(), 'polly', '21/5', owner.id)
patty = Cat(uuid.uuid4(), 'Patty', '7/12', jorge.id)

owner.pets.append(polly)
jorge.pets.append(patty)

dic = {"owner": owner.first_name, "lastname": owner.second_name} #dictionary

download_dir = "owners.csv" #where you want the file to be downloaded to 

csv = open(download_dir, "w") 
#"w" indicates that you're writing strings to the file

columnTitleRow = "name, lastname\n"
csv.write(columnTitleRow)

for key in dic.keys():
	name = dic[key]
	lastname = dic[key]
	row = name + "," + lastname + ""
	csv.write(row)










