try:
    file = open("new_file2.txt")
    test_dict = {"Name": "Saksham"}
    print(test_dict["age"])
except FileNotFoundError:
    file = open("new_file2.txt", "w")
    print("New File Created")
except KeyError as error_message:
    print(f"The requested key {error_message} does not exist!")
# This else block runs when try block executes successfully
else:
    print("This is else block")
finally:
    raise KeyError("User raised error!")
    file.close()
    print("Execution Completed!")