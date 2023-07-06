import os
def main(debug,venv):
	os.system("cls")
	tg = '''
 ▄▄▄▄         ██░ ██      ▒███████▒     ▄▄▄█████▓      ██ ▄█▀
▓█████▄      ▓██░ ██▒     ▒ ▒ ▒ ▄▀░     ▓  ██▒ ▓▒      ██▄█▒ 
▒██▒ ▄██     ▒██▀▀██░     ░ ▒ ▄▀▒░      ▒ ▓██░ ▒░     ▓███▄░ 
▒██░█▀       ░▓█ ░██        ▄▀▒   ░     ░ ▓██▓ ░      ▓██ █▄ 
░▓█  ▀█▓ ██▓ ░▓█▒░██▓ ██▓ ▒███████▒ ██▓   ▒██▒ ░  ██▓ ▒██▒ █▄
░▒▓███▀▒ ▒▓▒  ▒ ░░▒░▒ ▒▓▒ ░▒▒ ▓░▒░▒ ▒▓▒   ▒ ░░    ▒▓▒ ▒ ▒▒ ▓▒
▒░▒   ░  ░▒   ▒ ░▒░ ░ ░▒  ░░▒ ▒ ░ ▒ ░▒      ░     ░▒  ░ ░▒ ▒░
 ░    ░  ░    ░  ░░ ░ ░   ░ ░ ░ ░ ░ ░     ░       ░   ░ ░░ ░ 
 ░        ░   ░  ░  ░  ░    ░ ░      ░             ░  ░  ░   
      ░   ░            ░  ░          ░             ░        
        BHZEYE TOOL-KIT: select python version lmao\n\n'''
	'''This is a script that takes the path of mutiple python versions instalation directory
	and changes them on the ambient variables so diferent versions can be used and switched easily
	to use it u will have to create a "paths.txt" file inside the program root directory and put the
	python and pthon/scripts paths inside the txt(remember to always leave a new line on the end of the txts)
	and u will create a folder called "paths" and create a txt file for every version u want to use
	and inside the txt u will put the path of the python and python/scripts of the selected version
	thats it. run the program on admin privileges otherwise it wont change anything. . .'''
	with open(f"{os.getcwd()}/paths.txt","r") as pathfile:
		path_list = pathfile.readlines()
		clean_path_list = []
		for i in path_list:
			clean_path_list.append(i[:len(i)-1])
	
	env_var = os.environ["PATH"]
	env_var_list = env_var.split(";")

	NEGATIVE_LIST = []
	# loop troguh all env variables
	for item in env_var_list:
		for user_path in clean_path_list: #check if its a python path
			if item == user_path:
				NEGATIVE_LIST.append(item)

	# cleans the list of env variables to be rebuilt wihout python paths
	for i in range(len(NEGATIVE_LIST)):
		env_var_list.remove(NEGATIVE_LIST[i])
	#remove the item from the virtualenv
	# maybe change when running for real
	if venv == True:
		env_var_list.pop(0)
	else:
		pass

	new_env_var_item = ""
	for var1 in env_var_list:
		new_env_var_item += f"{var1};"
		
	c_new_env_var_item = new_env_var_item[:len(new_env_var_item)-1]

	print(tg)

	available_versions = os.listdir(f"{os.getcwd()}/paths")

	if debug == True:
		print("Raw env_var_item:",env_var)
		print("Items to be removed:",clean_path_list)
		print("Clean env_var_item:",c_new_env_var_item)
		print("available_versions:",available_versions)

	for i in range(len(available_versions)):
		print(f"Version:{available_versions[i]}-ID={i}")

	version_input = input("Select the version (ID)->")

	if version_input.isdigit() == True:
		with open(f"{os.getcwd()}/paths/{available_versions[int(version_input)]}","r") as pathfile_in:
			path_list_in = pathfile_in.readlines()
			clean_path_list_in = []
			for i_in in path_list_in:
				clean_path_list_in.append(i_in[:len(i_in)-1])

		if debug == True:		
			print("Paths to be added:",clean_path_list_in)

		version_string = ""
		for var2 in clean_path_list_in:
			version_string += f"{var2};"
		modified_env_var_item = f"{version_string}{c_new_env_var_item}"

		print("Final env_var_item:",modified_env_var_item)
		confirm = input("Modify? (y/n): ")
		if confirm.upper() == "Y":
			os.system(f'setx /m PATH "{modified_env_var_item}"')
			input("Enter to continue. . .")
			main(debug,venv)
		else:
			main(debug,venv)

if __name__ == "__main__":
	#Debug,virtualenv
	main(True,False)