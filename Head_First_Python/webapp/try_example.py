try:
    with open('my_file.txt') as fh:
        file_data = fh.read()
except FileNotFoundError:
    print("The data file is missing!")
except PermissionError:
    print("The data file is not accessible!")
except Exception as err:
    print(f"Something went wrong:", str(err))
