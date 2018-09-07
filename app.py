from database import *

db = DatabaseConnection()
print(db)

# count = db.create_user('Jane', 'Nantongo', 26, '2018-08-25')
# print(count)


users = db.get_all_users()
print(users)

print("####################")

for user in users:
    print(user)



print("####################")

mylist = []

for user in users:
	user_row = ''
	for item in user:
		user_row += " " + str(item)
	print('\nITEM')
	print(user_row)
	mylist.append(user_dict)


json_string = {'data': mylist}
print(json_string)

import json
print('RETURN THIS TO API CLIENT\n\n\n\n')
print(json.dumps(json_string))