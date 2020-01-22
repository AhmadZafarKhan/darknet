import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Directory where the data will reside, relative to 'darknet.exe'
path_data = '/data-and-labels'
# path_data = input("enter path: ")

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
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
