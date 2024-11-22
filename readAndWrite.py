def read_and_modify_file(input_filename, output_filename):
    try:
       
        with open(input_filename, "r") as input_file:
            content = input_file.read()
        
        modified_content = content.upper()

        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)

        print(f"File '{input_filename}' has been read and modified content has been written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: An issue occurred while reading or writing to the file.")


input_file = "input.txt"
output_file = "output.txt"
read_and_modify_file(input_file, output_file)
