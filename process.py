#author: Ahmad Zafar Khan
#date: 22.01.2020

import glob, os


current_dir = os.path.dirname(os.path.abspath(__file__)) # Current directory

path_data = '/data-and-labels' # directory of dataset
# path_data = input("enter path: ")

percentage_test = 10; # set train test split here

file_train = open('temp-train.txt', 'w')
file_test = open('temp-test.txt', 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)
# os.chdir("../..")
print(str(os.getcwd()))
path = current_dir + path_data
# path = path_data

server_type = int(input("press 1 for remote server, press 2 for local server: "))

for image_path in os.listdir(path):
	if not image_path.startswith('.') and not image_path.endswith('.txt') and image_path != 'Thumbs.db':
		print(image_path)
		if counter == index_test:
			counter = 1
			if server_type == 2:
				file_test.write(current_dir + path_data + "/" + image_path + "\n")
			if server_type == 1:
				file_test.write("/home/ubuntu/darknet" + path_data + "/" + image_path + "\n")
		else:
			if server_type == 2:
				file_train.write(current_dir + path_data + "/" + image_path + "\n")
			if server_type == 1:
				file_train.write("/home/ubuntu/darknet" + path_data + "/" + image_path + "\n")
			counter = counter + 1
