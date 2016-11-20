"""Write a program that creates a directory containing course numbers and the
room numbers of the rooms where the courses meet. The dictionary should have
the following key-value pairs:"""

def main():
	#Setup class information
	room = {'CS101' : "3004",'CS102' : "4501",'CS103' : "6755",'NT110' : "1244", 'CM241' : "1411"}
	instructor = {'CS101' : 'Haynes', 'CS102' : 'Alvarado','CS103' : 'Rich','NT110' : 'Burke','CM241' : 'Lee'}
	time = {'CS101' : '8:00am', 'CS102' : '9:00am', 'CS103' : '10:00am', 'NT110' : '11:00am', 'CM241' : '1:00pm'}
	#user prompt
	user_class = input('Enter a class name:').upper()
	#output user schedule
	print('Class:',user_class)
	print('Room:', room.get(user_class))
	print('Instructor:', instructor.get(user_class))
	print('Time:', time.get(user_class))
	
main()
