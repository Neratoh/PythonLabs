def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except Exception as e:
        print(f"File {file_name} wasn't opened! Error: {e}")
        return None
    else:
        print(f"File {file_name} was opened!")
        return file

def create_files():
    file1_name = "TF18_1.txt"
    file2_name = "TF18_2.txt"

    file1 = Open(file1_name, "w")
    file2 = Open(file2_name, "w")

    if file1 and file2:
        file1.write("This is text file TF18_1 with different length strings.\nSecond line of TF18_1.\n")
        file2.write("This is text file TF18_2 with different content.\nSecond line of TF18_2.\n")
        file1.close()
        file2.close()
        print("Files TF18_1 and TF18_2 successfully created and closed!")

def swap_contents():
    file1_name = "TF18_1.txt"
    file2_name = "TF18_2.txt"
    temp_file_name = "TF18_3.txt"

    file1 = Open(file1_name, "r")
    file2 = Open(file2_name, "r")
    temp_file = Open(temp_file_name, "w")

    if file1 and file2 and temp_file:
        while True:
            chunk1 = file1.read(20)
            if not chunk1:
                break
            temp_file.write(chunk1)

        while True:
            chunk2 = file2.read(20)
            if not chunk2:
                break
            temp_file.write(chunk2)

        file1.close()
        file2.close()
        temp_file.close()

        temp_file = Open(temp_file_name, "r")
        file1 = Open(file1_name, "w")

        if temp_file and file1:
            while True:
                chunk2 = temp_file.read(20)
                if not chunk2:
                    break
                file1.write(chunk2)

            temp_file.close()
            file1.close()

        temp_file = Open(temp_file_name, "r")
        file2 = Open(file2_name, "w")

        if temp_file and file2:
            while True:
                chunk1 = temp_file.read(20)
                if not chunk1:
                    break
                file2.write(chunk1)

            temp_file.close()
            file2.close()

        print("Contents of TF18_1 and TF18_2 successfully swapped in 20-character chunks!")

def read_and_print_files():
    file1_name = "TF18_1.txt"
    file2_name = "TF18_2.txt"

    file1 = Open(file1_name, "r")
    file2 = Open(file2_name, "r")

    if file1:
        print("Contents of TF18_1:")
        for line in file1:
            print(line, end="")
        file1.close()

    if file2:
        print("Contents of TF18_2:")
        for line in file2:
            print(line, end="")
        file2.close()

create_files()
swap_contents()
read_and_print_files()
