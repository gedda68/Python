def copy_function() :    
	print ("copy function")

def print_function() :    
	print ("print function")

def exit_function() :    
	print ("exit function")

# Definition piece. 
func_dict = {} 
func_dict["copy"] = copy_function 
func_dict["print"] = print_function 
func_dict["exit"] = exit_function

print(func_dict)

# Processing piece 
#command = input("Enter command: ") 
#if func_dict.has_key(command) :    
#	func_dict[command]() 
#else :    
#	print ("invalid command: ") +command
