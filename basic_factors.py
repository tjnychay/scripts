#!/usr/bin/env python

#import sys

#def caching_file_properties(n):
#	separator = "="

#	with open('factors.properties') as f:
#
#		for line in f:
#			if separator in line:
#				line = line.rstrip()
#				if "=" not in line: continue #skips blanks and comments w/o =
#				if line.startswith("#"): continue #skips comments which contain =
#				# Find the name and value by splitting the string
#				name, value = line.split(separator)
#				name = name.strip()
#				value = value.strip()
#				print name
#				if name == n:
#					print name, value
#				print n
#
#	print(keys)
#### This would be caching algorithm, to figure out if the new array already exists in the properties file, if so then use that instead of running the rest of the program
#### Not working due to inability to read the 'n' input


def factors():
	data=[]
	returned_list = {}
	n=int(input("How many: "))
	for i in range(0,n):
		x=int(input("Enter"))
		data.append(x)
#	print(data)
#	caching_file_properties(data)

	for number in data :
		test_data = []
		for n in data :
			if ( data.index(number) != data.index(n) ) :
				if ( number % n ) == 0:
					test_data.append(n)
#		print test_data
		returned_list[number] = test_data
	f = open('factors.properties', 'ab')
	print >> f, data,"=",returned_list
	f.close()
	print data,"=",returned_list

def reverse_factors():
	data=[]
	returned_list = {}
	n=int(input("How many: "))
	for i in range(0,n):
		x=int(input("Enter"))
		data.append(x)
#	print(data)
	for number in data :
		test_data = []
		for n in data :
			if ( data.index(number) != data.index(n) ) :
				if ( n % number ) == 0:
					test_data.append(n)
#		print test_data
		returned_list[number] = test_data
#	print returned_list
	f = open('reverse_factors.properties', 'ab')
	print >> f, data,"=",returned_list
	f.close()
	print data,"=",returned_list

answer = raw_input("Please type 'factors' or 'reverse_factors' and hit enter. ").lower()
if answer == "factors":
	factors()
elif answer == "reverse_factors":
	reverse_factors()
else:
	print "This is not a correct selection"
## simple setup for input to decide if you want to run factors or reverse_factors then calls the correct function based on input

#caching_file_properties()